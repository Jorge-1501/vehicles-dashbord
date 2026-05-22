# app.py
import streamlit as st

st.set_page_config(
    page_title="Dashboard de Análisis de Partículas",
    page_icon="⚛️",
    layout="wide"
)

st.title("Bienvenido al Dashboard de Análisis de Jets")
st.markdown("""
Esta herramienta permite el análisis exploratorio de datos de quarks y gluones. 
Utiliza el menú lateral para navegar entre las distintas secciones:
- **Análisis Crudo:** Visualización directa de las features extraídas.
- **Datos Procesados:** Análisis post-normalización.
- **Resultados Finales:** Modelado y métricas de desempeño.
""")

# Puedes poner aquí algún dato global si quieres
st.info("Selecciona una página en la barra lateral para comenzar.")