# Fase 4, 5 & 6: Modelado, Evaluación y Despliegue (Clasificación)

Este directorio contiene el desarrollo de las etapas finales de clasificación de la metodología CRISP-DM, donde se entrenan modelos de aprendizaje automático supervisado para clasificar y predecir si un jugador obtendrá el premio al Jugador Más Valioso (`mvp_award`), se evalúan frente a métricas estándar de clasificación y se despliega una interfaz interactiva en Streamlit.

---

## Caso de Estudio: Predicción de Jugador MVP

El objetivo de esta fase es implementar un modelo de clasificación robusto capaz de predecir si un jugador de eSports será galardonado como MVP (`Yes` = 1, `No` = 0) al finalizar una partida, basándose en sus métricas físicas y estadísticas competitivas de rendimiento individual.

### Estructura de esta Etapa

*   **[HectorAguila_Ev04_Clasificacion_eSports.ipynb](HectorAguila_Ev04_Clasificacion_eSports.ipynb):** Jupyter Notebook con el flujo experimental CRISP-DM completo:
    1.  Limpieza de datos (filtro de reacción humana de 120 ms y outliers lentos por IQR).
    2.  División temprana train/test ($80\% / 20\%$) para mitigar Data Leakage de manera rigurosa.
    3.  Preprocesamiento de datos aislado (StandardScaler + OneHotEncoder) dentro de Pipelines.
    4.  Entrenamiento y comparación de 3 clasificadores (Regresión Logística, KNN y Random Forest Classifier).
    5.  Evaluación cuantitativa mediante matrices de confusión, curvas ROC y curvas Precision-Recall (PR).
*   **[PROCESO_DE_ANALISIS_MC.md](PROCESO_DE_ANALISIS_MC.md):** Reporte técnico académico formal que detalla el modelado, los resultados reales del test set, la justificación de la debilidad de KNN y la Declaración de IA.
*   **[app.py](app.py):** Aplicación interactiva construida en Streamlit para la inferencia del MVP en tiempo real mediante sliders e inputs configurables.
*   **[run_streamlit.sh](run_streamlit.sh):** Script bash wrapper para levantar automáticamente la app de Streamlit de forma aislada y resolver la carga del entorno virtual de forma inteligente.
*   **[checkpoints/best_model.joblib](checkpoints/best_model.joblib):** Pipeline del modelo campeón (Random Forest Classifier) serializado y exportado para producción.
*   **[esports_player_performance_tournament_analytics.csv](esports_player_performance_tournament_analytics.csv):** Dataset original de eSports utilizado para la fase.

---

## Auditoría del Dataset y Decisión de Ingeniería de Cambio de Target

Al auditar la distribución de la variable objetivo inicial `match_outcome` (Victoria/Derrota), se reveló un desbalanceo extremo: **2793 victorias vs. solo 7 derrotas**. Con un desbalanceo del $99.75\%$, cualquier clasificador predice siempre la clase mayoritaria "Win" y obtiene una exactitud perfecta sin aprender nada, lo que invalida el experimento.

Por consiguiente, se tomó la decisión metodológica de usar **`mvp_award`** como target de clasificación. Cuenta con una distribución realista de **2561 registros "No" vs. 239 registros "Yes"** (un balance aproximado del $90\% / 10\%$), lo que expone a los modelos a una clasificación binaria real y permitió evidenciar empíricamente la debilidad de KNN en la clase minoritaria (F1-score de solo `0.6494` frente al `1.0000` de Random Forest).

---

## Tecnologías y Librerías

*   **Lenguaje:** Python 3.14+
*   **Modelamiento:** `pandas`, `numpy`, `scikit-learn`
*   **Persistencia:** `joblib`
*   **Visualizaciones:** `matplotlib`, `seaborn`
*   **Despliegue:** `streamlit`

---

## Cómo Ejecutar la Aplicación Web (Streamlit)

Para levantar el simulador predictivo localmente:

1.  **Opción A (Recomendada - Script Wrapper):**
    Ejecuta el script de arranque desde la raíz del proyecto (este detectará y activará tu entorno virtual automáticamente):
    ```bash
    ./03_Modelos_Clasificacion/run_streamlit.sh
    ```

2.  **Opción B (Manual):**
    Activa tu entorno virtual manualmente e inicia el servidor Streamlit:
    ```bash
    source .venv/bin/activate
    streamlit run 03_Modelos_Clasificacion/app.py
    ```

3.  **Acceso:**
    Abre en tu navegador la dirección local arrojada por la terminal (normalmente `http://localhost:8501`).

---

**Héctor Aguila**  
*Fundamentos de Machine Learning*
