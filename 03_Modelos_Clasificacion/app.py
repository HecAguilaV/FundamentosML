import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Configuración de la página con estética premium formal de eSports
st.set_page_config(
    page_title="eSports MVP Predictor",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados (navy blue con degradados eSports)
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #070B19 0%, #0F1C3F 60%, #1E3A70 100%);
            color: #ffffff;
        }
        .main {
            background: transparent;
        }
        /* Ajustes de campos de formulario */
        div[data-baseweb="select"] > div {
            background-color: #122146 !important;
            color: white !important;
            border: 1px solid #1E3A70 !important;
        }
        input {
            background-color: #122146 !important;
            color: white !important;
        }
        .stButton>button {
            background: linear-gradient(135deg, #3B82F6, #1D4ED8);
            color: white;
            border-radius: 8px;
            border: none;
            padding: 10px 24px;
            font-weight: bold;
            font-size: 16px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 10px rgba(29, 78, 216, 0.3);
        }
        .stButton>button:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 20px rgba(59, 130, 246, 0.6);
            background: linear-gradient(135deg, #60A5FA, #2563EB);
        }
        /* Tarjetas de predicción dinámicas */
        .prediction-card-win {
            background-color: #0B251D;
            padding: 24px;
            border-radius: 12px;
            border: 1px solid #10B981;
            border-left: 6px solid #10B981;
            margin-top: 20px;
            box-shadow: 0 8px 30px rgba(16, 185, 129, 0.2);
        }
        .prediction-card-loss {
            background-color: #1A2238;
            padding: 24px;
            border-radius: 12px;
            border: 1px solid #3B82F6;
            border-left: 6px solid #3B82F6;
            margin-top: 20px;
            box-shadow: 0 8px 30px rgba(59, 130, 246, 0.2);
        }
        .metric-value-win {
            font-size: 40px;
            font-weight: bold;
            color: #10B981;
            text-shadow: 0 0 10px rgba(16, 185, 129, 0.4);
        }
        .metric-value-loss {
            font-size: 40px;
            font-weight: bold;
            color: #60A5FA;
            text-shadow: 0 0 10px rgba(96, 165, 250, 0.4);
        }
    </style>
""", unsafe_allow_html=True)

# Título
st.title("eSports MVP Predictor")
st.markdown("---")

MODEL_PATH = 'checkpoints/best_model.joblib'

if not os.path.exists(MODEL_PATH):
    st.warning("Advertencia: No se encontró el archivo best_model.joblib en el directorio. Ejecuta por completo el notebook HectorAguila_Ev04_Clasificacion_eSports.ipynb para entrenar y serializar el modelo campeón.")
else:
    @st.cache_resource
    def load_model():
        return joblib.load(MODEL_PATH)
        
    pipeline = load_model()
    
    st.subheader("Simulador Predictivo de Jugador Más Valioso (MVP)")
    st.markdown("Ingresa las estadísticas y parámetros de rendimiento del jugador en la partida para predecir si será galardonado como MVP:")

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Variables Categóricas (Contexto)")
        team_name = st.selectbox(
            "Equipo del Jugador:",
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
            "Tipo / Fase de Partida:",
            options=["Playoff", "Final", "Semi-Final", "Qualifier", "Group Stage"]
        )
        match_outcome = st.selectbox(
            "Resultado de la Partida:",
            options=["Win", "Loss"]
        )
        
    with col2:
        st.markdown("### Variables Numéricas (Rendimiento)")
        col_stats1, col_stats2 = st.columns(2)
        with col_stats1:
            kills = st.slider("Kills:", min_value=0, max_value=50, value=15)
            assists = st.slider("Assists:", min_value=0, max_value=50, value=8)
            deaths = st.slider("Deaths:", min_value=0, max_value=50, value=10)
            accuracy_percent = st.slider("Precisión (%):", min_value=0.0, max_value=100.0, value=45.0, step=0.1)
        with col_stats2:
            reaction_time_ms = st.slider("Tiempo de Reacción (ms):", min_value=120.0, max_value=500.0, value=200.0, step=1.0)
            fatigue_index = st.slider("Índice de Fatiga:", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
            performance_score = st.slider("Score de Rendimiento Estimado:", min_value=0.0, max_value=100.0, value=50.0, step=0.1)
            win_probability = st.slider("Probabilidad de Victoria Inicial:", min_value=0.0, max_value=1.0, value=0.5, step=0.01)

    # Botón predictivo
    if st.button("Predecir MVP"):
        # Estructurar DataFrame con el mismo orden e identificadores que el pipeline espera
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
            'performance_score': performance_score,
            'win_probability': win_probability,
            'match_outcome': match_outcome
        }])
        
        # Inferencia a través del pipeline
        prediction = pipeline.predict(input_df)[0]
        
        # Renderizado de la predicción basado en el resultado binario
        if prediction == 1:
            st.markdown(
                f"""
                <div class="prediction-card-win">
                    <h3>Resultado de la Simulación</h3>
                    <p>El modelo clasificador predice que el jugador será galardonado como:</p>
                    <div class="metric-value-win">JUGADOR MVP (Yes)</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div class="prediction-card-loss">
                    <h3>Resultado de la Simulación</h3>
                    <p>El modelo clasificador predice que el jugador finalizará como:</p>
                    <div class="metric-value-loss">JUGADOR ESTÁNDAR (No)</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
        st.info(
            "Análisis del Predictor: La clasificación binaria estima la probabilidad de que "
            "un jugador reciba el reconocimiento MVP. Para ello, el modelo asocia de forma conjunta "
            "el score de rendimiento y la cantidad de kills en relación con las victorias del equipo."
        )
