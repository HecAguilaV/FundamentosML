import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Configuración de la página con estética premium
st.set_page_config(
    page_title="eSports Player Performance Predictor",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados para un diseño elegante (modo oscuro y tarjetas con HSL)
st.markdown("""
    <style>
        .main {
            background-color: #0e1117;
            color: #ffffff;
        }
        .stButton>button {
            background: linear-gradient(45deg, #FF4B4B, #FF8F8F);
            color: white;
            border-radius: 8px;
            border: none;
            padding: 10px 24px;
            font-weight: bold;
            font-size: 16px;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            transform: scale(1.05);
            box-shadow: 0 4px 15px rgba(255, 75, 75, 0.4);
        }
        .prediction-card {
            background-color: #1a1c24;
            padding: 24px;
            border-radius: 12px;
            border-left: 5px solid #FF4B4B;
            margin-top: 20px;
        }
        .metric-value {
            font-size: 36px;
            font-weight: bold;
            color: #FF4B4B;
        }
    </style>
""", unsafe_allow_html=True)

# Título de la Aplicación
st.title("🎮 eSports Player Performance Predictor")
st.markdown("---")

# Verificar si el modelo está exportado
MODEL_PATH = 'best_model.joblib'

if not os.path.exists(MODEL_PATH):
    st.warning("⚠️ No se encontró el archivo `best_model.joblib` en el directorio. Por favor, ejecuta por completo el notebook `HectorAguila_Ev03_Regresion_eSports.ipynb` primero para entrenar y guardar el modelo.")
else:
    # Cargar el pipeline del mejor modelo
    @st.cache_resource
    def load_model():
        return joblib.load(MODEL_PATH)
    
    pipeline = load_model()

    st.subheader("Simulador de Rendimiento del Jugador")
    st.markdown("Ingresa las estadísticas y parámetros de la partida en el formulario de abajo para predecir el score de desempeño final:")

    # Formulario dividido en dos columnas
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📋 Variables Categóricas (Contexto)")
        team_name = st.selectbox(
            "Equipo:",
            options=["Titan Esports", "Team Alpha", "Team Nova", "Phantom Squad", "Red Vortex", "CyberX"]
        )
        player_role = st.selectbox(
            "Rol del Jugador:",
            options=["Flex", "Support", "IGL", "Sniper", "Entry Fragger"]
        )
        map_played = st.selectbox(
            "Mapa Jugado:",
            options=["Dust Arena", "Neon City", "Desert Storm", "Skyline", "Frozen Base"]
        )
        match_type = st.selectbox(
            "Fase del Torneo:",
            options=["Playoff", "Final", "Semi-Final", "Qualifier", "Group Stage"]
        )
        mvp_award = st.selectbox(
            "MVP Award en partida anterior:",
            options=["No", "Yes"]
        )

    with col2:
        st.markdown("### 📊 Variables Numéricas (Estadísticas)")
        kills = st.slider("Kills:", min_value=0, max_value=50, value=15)
        assists = st.slider("Assists:", min_value=0, max_value=50, value=8)
        deaths = st.slider("Deaths:", min_value=0, max_value=50, value=10)
        accuracy_percent = st.slider("Precisión (%):", min_value=0.0, max_value=100.0, value=45.0, step=0.1)
        reaction_time_ms = st.slider("Tiempo de Reacción (ms):", min_value=120.0, max_value=500.0, value=200.0, step=1.0)
        fatigue_index = st.slider("Índice de Fatiga:", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        win_probability = st.slider("Probabilidad de Victoria del Equipo:", min_value=0.0, max_value=1.0, value=0.8, step=0.01)

    # Botón de predicción
    if st.button("Predecir Rendimiento"):
        # Armar el DataFrame de entrada tal como lo espera el pipeline
        input_df = pd.DataFrame([{
            'team_name': team_name,
            'player_role': player_role,
            'map_played': map_played,
            'match_type': match_type,
            'kills': kills,
            'assists': assists,
            'deaths': deaths,
            'accuracy_percent': accuracy_percent,
            'reaction_time_ms': reaction_time_ms,
            'fatigue_index': fatigue_index,
            'win_probability': win_probability,
            'mvp_award': mvp_award
        }])

        # Realizar la predicción a través del pipeline (que preprocesa y escala los datos automáticamente)
        prediction = pipeline.predict(input_df)[0]

        # Mostrar el resultado de forma elegante
        st.markdown(
            f"""
            <div class="prediction-card">
                <h3>🎯 Resultado de la Simulación</h3>
                <p>El score de rendimiento estimado para el jugador bajo estas condiciones es:</p>
                <div class="metric-value">{prediction:.2f}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.info(
            "💡 **Interpretación del Modelo:** El rendimiento estimado depende de forma estrictamente "
            "lineal de las estadísticas directas del jugador (kills, assists, deaths, precisión, fatiga y "
            "tiempo de reacción). Las variables contextuales como el equipo, mapa o fase del torneo no "
            "aportan peso a la ecuación, confirmando que en este dataset el rendimiento es puramente "
            "individual e independiente del entorno."
        )
