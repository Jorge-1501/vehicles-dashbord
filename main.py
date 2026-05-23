# app.py
import streamlit as st
from sidebar_config import render_sidebar

st.set_page_config(
    page_title="Dashboard de análisis de partículas",
    page_icon="⚛️",
    layout="wide"
)

render_sidebar()

st.title("Bienvenido al Dashboard de análisis de jets de partículas")
st.markdown("""
Esta herramienta permite el análisis exploratorio de datos provenientes de 
colisiones de partículas, enfocándose en la identificación de jets 
de quarks y gluones. 
Utiliza el menú lateral para navegar entre las distintas secciones:
- **Introducción:** Descripción general del proyecto y fenómenos físicos involucrados.
- **Análisis Crudo:** Visualización directa de las features extraídas.
- **Datos Procesados:** Análisis post-normalización.
- **Resultados Finales:** Modelado y métricas de desempeño.
- **Colisiones interactivas:** Simulaciones y visualizaciones dinámicas de colisiones.
""")

# cita de la fuente de datos apa
st.markdown("""
**Base de datos utilizada:** \n
Kansal, R., Duarte, J., Su, H., Orzari, B., Tomei, T., Pierini, M., Touranakou, M., 
Vlimant, J.-R., & Gunopulos, D. (2022). JetNet (Version 2) [Data set]. Zenodo.
 https://doi.org/10.5281/zenodo.6975118""")

# Puedes poner aquí algún dato global si quieres
st.info("Selecciona una página en la barra lateral para comenzar.")
