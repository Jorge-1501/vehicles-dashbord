# processor.py
from pathlib import Path
from sklearn.preprocessing import StandardScaler
import streamlit as st
import h5py
import numpy as np
import pandas as pd


# ============================================================================
# ============================================================================
# Load and preprocess data
# ============================================================================
# ============================================================================

features = ['pT', 'eta', 'mass', 'No. particles']

@st.cache_data
def load_raw_data():
    """
    Función para cargar los datos crudos desde los archivos .hdf5.
    """
    data_dir = Path("data")
    with h5py.File(data_dir / "q.hdf5", 'r') as f_q:
        q_data = f_q['jet_features'][()]
        q_data = pd.DataFrame(q_data, columns=features)
        q_data['label'] = "Quarks"  # Quarks como señal
    with h5py.File(data_dir / "g.hdf5", 'r') as f_g:
        g_data = f_g['jet_features'][()]
        g_data = pd.DataFrame(g_data, columns=features)
        g_data['label'] = "Gluones"  # Gluons como fondo
    return pd.concat([q_data, g_data], ignore_index=True)

@st.cache_data
def get_preprocessed_data(_df):
    """
    Función para preprocesar los datos: transformación logarítmica, 
    estandarización y normalización.
    """
    # Copiamos para no modificar el df original
    df = _df.copy()

    # Tranformación logarítmica para pT y mass
    for col in ['pT', 'mass']:
        df[col] = np.log1p(df[col])  # log(1 + x) para evitar problemas con ceros

    # StandardScaler y tanh para normalizar los datos
    scaler = StandardScaler()
    df[features] = scaler.fit_transform(df[features])
    df[features] = np.tanh(df[features])  # Limita los valores a [-1, 1]

    return df
