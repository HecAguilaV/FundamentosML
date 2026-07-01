# Fase 4, 5 & 6: Modelado, Evaluación y Despliegue (Clasificación)

Este directorio contiene el desarrollo de las etapas finales de clasificación de la metodología CRISP-DM, donde se entrenan modelos de aprendizaje automático supervisado para clasificar y predecir si un jugador obtendrá el premio al Jugador Más Valioso (`mvp_award`), se evalúan frente a métricas estándar de clasificación y se despliega una interfaz interactiva en Streamlit.

---

## Caso de Estudio: Predicción de Jugador MVP

El objetivo de esta fase es implementar un modelo de clasificación robusto capaz de predecir si un jugador de eSports será galardonado como MVP (`Yes` = 1, `No` = 0) al finalizar una partida, basándose en sus métricas físicas y estadísticas competitivas de rendimiento individual.

### Rol de los Archivos en este Directorio

*   **[HectorAguila_Ev04_Clasificacion_eSports.ipynb](HectorAguila_Ev04_Clasificacion_eSports.ipynb):** Jupyter Notebook con el flujo experimental CRISP-DM de clasificación (filtros IQR/neurofisiológico, split train/test aislado, pipelines y evaluación de Regresión Logística, KNN y Random Forest Classifier con curvas ROC/PR).
*   **[PROCESO_DE_ANALISIS_MC.md](PROCESO_DE_ANALISIS_MC.md):** Reporte técnico formal en Markdown que documenta la justificación del cambio de target a `mvp_award`, el análisis de métricas y la Declaración de IA.
*   **[PROCESO_DE_ANALISIS_MC.pdf](PROCESO_DE_ANALISIS_MC.pdf):** Copia en PDF del reporte técnico de clasificación, optimizada para descarga directa y lectura externa del docente.
*   **[app.py](app.py):** Código de la interfaz interactiva web construida con Streamlit para la simulación predictiva de obtención del premio MVP.
*   **[run_streamlit.sh](run_streamlit.sh):** Script bash wrapper ejecutable para inicializar Streamlit resolviendo las variables de ruta y el entorno virtual del proyecto.
*   **[checkpoints/best_model.joblib](checkpoints/best_model.joblib):** Pipeline del modelo campeón (Random Forest Classifier) serializado y exportado para producción.
*   **[esports_player_performance_tournament_analytics.csv](esports_player_performance_tournament_analytics.csv):** Dataset original bruto con las estadísticas competitivas históricas utilizadas para el modelado.
*   **[Learning_MC.md](Learning_MC.md):** Guía conceptual de estudio personal sobre clasificación (maldición de la dimensionalidad en KNN, media armónica de F1-Score y curvas ROC vs. PR). *(Nota: Archivo local personal, ignorado en Git).*

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
