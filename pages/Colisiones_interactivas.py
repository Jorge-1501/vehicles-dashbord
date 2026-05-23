import streamlit as st
import h5py
import plotly.graph_objects as go
import os
import numpy as np
from sidebar_config import render_sidebar

render_sidebar()

st.title("Explorador de Eventos: JetNet")
st.markdown("Inspecciona la estructura real de los jets que utiliza tu modelo.")

# 1. Función para cargar datos de manera eficiente
@st.cache_data
def cargar_evento(tipo, index):
    # Ruta definida en la carpeta data/
    path = f"data/{tipo}.hdf5"
    if not os.path.exists(path):
        return None, None
    
    with h5py.File(path, 'r') as f:
        # Extraer particulas y features del jet
        particulas = f['particle_features'][index]
        jet_feat = f['jet_features'][index]
        return particulas, jet_feat

def procesar_particulas(particulas):
    # Usamos la máscara (columna 3: [eta_rel, phi_rel, pt_rel, mask])
    mask = particulas[:, 3] == 1
    return particulas[mask]

# 2. Interfaz de control
col_ctrl1, col_ctrl2 = st.columns(2)
with col_ctrl1:
    tipo = st.radio("Tipo de Jet:", ["q", "g"], format_func=lambda x: "Quark" if x=="q" else "Gluon")
with col_ctrl2:
    # Asumimos que los archivos tienen al menos 1000 eventos para el slider
    idx = st.slider("Seleccionar evento:", 0, 999, 0)

# 3. Procesamiento y Visualización
particulas, jet_f = cargar_evento(tipo, idx)

if particulas is not None:
    p_limpias = procesar_particulas(particulas)
    
    # Calcular los bordes del "cono" para visualización
    # Usamos el rango de los datos para que el cono envuelva al Jet
    max_eta = np.max(np.abs(p_limpias[:, 0])) + 0.1
    max_phi = np.max(np.abs(p_limpias[:, 1])) + 0.1
    
    fig = go.Figure()

    # A) Dibujar el CONO (Líneas que salen del origen)
    fig.add_trace(go.Scatter(
        x=[0, max_eta, 0, -max_eta, 0], 
        y=[0, max_phi, 0, -max_phi, 0],
        mode='lines',
        line=dict(color='white', width=1, dash='dot'),
        opacity=0.5,
        name='Cono de Jet'
    ))

    # B) Dibujar las partículas (puntos más grandes)
    fig.add_trace(go.Scatter(
        x=p_limpias[:, 0],
        y=p_limpias[:, 1],
        mode='markers',
        marker=dict(
            # Tamaño: base de 8 + escalado proporcional al pT
            size=8 + (p_limpias[:, 2] * 60), 
            color=p_limpias[:, 2],
            colorscale='Viridis',
            line=dict(width=1, color='white'), # Borde blanco para que resalten
            opacity=0.8
        )
    ))
    
    fig.update_layout(
        template="plotly_dark",
        height=450,
        title=f"Estructura del Jet ({'Quark' if tipo=='q' else 'Gluón'})",
        xaxis=dict(range=[-0.8, 0.8], title="η_rel"),
        yaxis=dict(range=[-0.8, 0.8], title="φ_rel"),
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)

# 4. Mostrar los Jet Features (la entrada del QKAN)
    st.subheader("Jet Features (Entrada al Modelo)")
    cols = st.columns(4)
    labels = ["pT", "η", "Masa", "Multiplicidad"]
    for i in range(4):
        cols[i].metric(label=labels[i], value=f"{jet_f[i]:.3f}")
else:
    st.error("No se encontraron los archivos en la carpeta 'data/'. Verifica la ruta.")
    