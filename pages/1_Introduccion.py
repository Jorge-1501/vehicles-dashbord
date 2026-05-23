import streamlit as st
from sidebar_config import render_sidebar

render_sidebar()

st.title("Background: La física de los Jets")

# Crear los tabs
tab1, tab2 = st.tabs(["General", "Técnico"])

with tab1:
    st.header("El Escenario: El CERN y el LHC")
    c_intro1, c_intro2 = st.columns([1, 1])
    with c_intro1:
        st.write("""
        El **CERN** (Organización Europea para la Investigación Nuclear) alberga al 
        **LHC** (Gran Colisionador de Hadrones), el acelerador de partículas más 
        potente del mundo. Aquí, enviamos haces de protones en direcciones opuestas 
        a energías extremas.
        
        Cuando estos protones chocan en el corazón de detectores como **CMS**, 
        crean un entorno que replica las condiciones del universo una fracción 
        de segundo después del Big Bang.
        """)
    #with c_intro2:
        #st.image("img/img_lhc_diagram.svg", caption="Esquema del acelerador LHC")
    
    st.divider()

    st.header("¿Qué es un Jet y por qué nos importa?")
    
    # Paso 1: La Colisión
    st.subheader("1. La colisión")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("Imagina dos protones chocando a velocidades cercanas a la luz. Es como romper un reloj para entender cómo funcionan sus engranajes.")
    with col2:
        st.image("img/img_1.svg", caption="Esquema de colisión")
        
    st.divider()
    
    # Paso 2: La Cascada
    st.subheader("2. La cascada de energía")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("Debido a las leyes de la naturaleza, las partículas elementales no pueden existir solas; se agrupan instantáneamente, creando una 'lluvia' o cascada de energía.")
    with col2:
        st.image("img/img_2.svg", caption="Formación de la cascada")

    st.divider()
    
    # Paso 3: El Detector (Aquí insertamos el simulador que construimos)
    st.subheader("3. El resultado: el jet")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("En nuestro detector, lo que realmente vemos no son las partículas individuales, sino un 'cono' de energía que representa la cascada completa.")
    with col2:
        st.image("img/img_4.svg", caption="Cono de energía (Jet)")
        st.image("img/img_5.svg", caption="Detectores")
    
    st.write("Puedes dirigirte a la pestaña de 'Colisiones interactivas' para explorar \
                algunos jets que fueron estudiados.")
    # Aquí insertarías el código de visualización de eventos de JetNet que definimos antes
    # st.plotly_chart(fig_del_visor) 

with tab2:
    st.header("Background técnico.")
    st.info("🚧 Sección en progreso: Documentación técnica de la arquitectura Q-KAN, métricas de discriminación quark-gluón y validación con datos CMS.")
    #st.write("Próximamente: Análisis de distribuciones de variables de forma de jet (Jet Shape Variables).")
