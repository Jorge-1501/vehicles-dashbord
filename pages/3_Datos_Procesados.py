"""
2_Analisis_Procesado.py
-----------------------
Página de Streamlit para el análisis exploratorio de 
datos procesados del dataset de partículas.

Permite visualizar la distribución de features, la correlación entre ellas 
y su relación con la clase (Quarks vs Gluones) a través de gráficos 
estáticos e interactivos.

Funciones principales:
- static_image(tipo): Genera gráficos estáticos según el tipo solicitado.

Interfaz:
- Botones para seleccionar la vista activa (Matriz de dispersión, Boxplot por clase
    o Mapa de calor de correlación).
- En la vista de Matriz de dispersión, se ofrecen opciones para configurar gráficos
    interactivos (scatter plot y histogramas) con filtros por clase.
"""
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from src.data_loader import get_preprocessed_data, load_raw_data
from sidebar_config import render_sidebar

st.set_page_config(page_title="Análisis de datos procesados", layout="wide")
render_sidebar()
st.header("Análisis de datos procesados")

df = load_raw_data()
df = get_preprocessed_data(df)
features = ['pT', 'eta', 'mass', 'No. particles']

# --- Imagen estática ---
def static_image(tipo):
    """
    Genera gráficos estáticos según el tipo solicitado:
    - "pairwise": Matriz de dispersión (pairplot) de las features.
    - "boxplot": Boxplot de las features por clase.
    - "correlation": Mapa de calor de correlación entre las features.
    """
    if tipo == "pairwise":
        #plt.close(fig)
        fig = sns.pairplot(df.sample(1000), hue='label', diag_kind='hist')
        return fig.fig
    elif tipo == "boxplot":
        fig, ax = plt.subplots(figsize=(8, 4))
        ax = fig.gca()
        colors = {'Quarks': 'blue', 'Gluones': 'red'}
        df_melted = df.melt(id_vars=['label'],
                            value_vars=features,
                            var_name='Feature',
                            value_name='Valor')
        g = sns.FacetGrid(df_melted, col="Feature", col_wrap=2, sharey=False, height=4)
        g.map_dataframe(sns.boxplot, x="label", y="Valor", palette=colors)
        g.set_titles("{col_name}")
        return g.fig
    elif tipo == "correlation":
        fig, ax = plt.subplots(figsize=(6, 8))
        ax = fig.gca()
        sns.heatmap(df[features].corr(), annot=True, cmap='coolwarm', ax=ax)
        ax.set_title("Mapa de calor de correlación")
        plt.tight_layout()
        return fig

if "vista_activa" not in st.session_state:
    st.session_state.vista_activa = None

# --- Interfaz ---
col1, col2, col3 = st.columns(3)

# Botones que actualizan la vista activa en el estado de la sesión
col1, col2, col3 = st.columns(3)
if col1.button("Matriz de dispersión", use_container_width=True):
    st.session_state.vista_activa = "pairwise"
if col2.button("Boxplot por clase", use_container_width=True):
    st.session_state.vista_activa = "boxplot"
if col3.button("Mapa de calor de correlación", use_container_width=True):
    st.session_state.vista_activa = "correlation"

# --- Lógica de renderiza ---
if st.session_state.vista_activa == "pairwise":
    tab1, tab2 = st.tabs(["Vista estática", "Vista interactiva"])
    with tab1:
        st.subheader("Matriz pairwise (estática)")
        st.pyplot(static_image('pairwise'))

    with tab2:
        st.subheader("Configuración de gráficos interactivos")
        c1, c2 = st.columns(2)
        with c1:
            scat_x = st.selectbox("Eje X", features, index=0)
            # Filtramos las opciones para que no aparezca el valor de scat_x
            opciones_y = [f for f in features if f != scat_x]
            scat_y = st.selectbox("Eje Y", opciones_y, index=0)
        with c2:
            hist_x = st.selectbox("Variable (Histograma)", features, index=0)
            particulas = st.multiselect("Filtrar partículas",
                                        options=df['label'].unique(),
                                        default=df['label'].unique())

        # OPTIMIZACIÓN: Cachear el filtrado
        @st.cache_data
        def get_filtered_data(particulas_tuple):
            '''Filtra el DataFrame según las partículas seleccionadas.'''
            return df[df['label'].isin(particulas_tuple)]

        df_filtered = get_filtered_data(tuple(particulas))
        df_display = df_filtered.sample(n=min(1000, len(df_filtered)), random_state=42)

        # Gráficos
        c1, c2 = st.columns(2)
        with c1:
            fig_s = px.scatter(df_display, x=scat_x, y=scat_y, color='label')
            st.plotly_chart(fig_s, use_container_width=True)
        with c2:
            fig_h = px.histogram(df_display, x=hist_x, color='label', barmode='overlay')
            st.plotly_chart(fig_h, use_container_width=True)

        st.subheader("Previsualización de datos filtrados")
        st.dataframe(df_display.head(100), use_container_width=True)

elif st.session_state.vista_activa == "boxplot":
    #Subsample para mejorar rendimiento
    df_sample = df.sample(n=min(20000, len(df)), random_state=42)
    st.subheader("Distribución de features por partícula")
    df_melted = df_sample.melt(id_vars=['label'],
                        value_vars=features,
                        var_name='Feature',
                        value_name='Value')

    # Colores personalizados para cada clase 
    # "Quarks" en azul y "Gluones" en rojo 
    color = {"Quarks": "#1f77b4", "Gluones": "#d62728"}

    # Gráfico interactivo con Plotly Express
    fig = px.box(df_melted,
                x='label',
                y='Value',
                color='label', # Color por clase
                facet_col='Feature',
                facet_col_wrap=2,
                color_discrete_map=color,
                template="plotly_white")

    # Personalización del diseño para mejorar legibilidad
    fig.update_xaxes(showline=True, linewidth=2, linecolor='black', gridcolor='lightgray')
    fig.update_yaxes(showline=True, linewidth=2, linecolor='black', gridcolor='lightgray')
    # Actualizamos el color de los labels de la gráfica para que sean legibles
    fig.update_layout(legend_title_text='Partícula', legend=dict(font=dict(size=12, color='black')))
    # Color de la caja
    fig.update_traces(boxmean= True, line_width = 2, opacity=0.85)
    # Layout
    fig.update_layout(legend_title_text='Partícula',
                        paper_bgcolor="white",
                        plot_bgcolor="white",
                        font=dict(size=12, color="black"),
                        height=800,
                        margin=dict(l=40, r=40, t=60, b=40))
    fig.for_each_yaxis(lambda yaxis: yaxis.update(matches=None,
                                                showticklabels=True,
                                                tickfont=dict(color='black')))
    st.plotly_chart(fig, use_container_width=True, key="boxplot_final_v2")

elif st.session_state.vista_activa == "correlation":
    st.subheader("Correlación con la Clase (Target)")
    df_temp = df.copy()
    df_temp['is_quark'] = df_temp['label'].map({'Quarks': 1, 'Gluones': 0})
    corr_matrix = df_temp[features + ['is_quark']].corr()
    fig = px.imshow(corr_matrix,
                    text_auto=".2f",
                    aspect="auto",
                    color_continuous_scale='RdBu_r',
                    range_color=[-1, 1])
    fig.update_layout(title="Correlación de cada feature con la clase (Quark=1)")
    st.plotly_chart(fig, use_container_width=True)

# Lógica fuera del flujo principal para abrir el modal de forma persistente
if "abrir_modal" in st.session_state and st.session_state.abrir_modal:
    st.session_state.abrir_modal = False # Reset
    abrir_modal_pairwise(df.sample(10000))
