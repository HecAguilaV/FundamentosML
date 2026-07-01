# Fase 4, 5 & 6: Modelado, Evaluación y Despliegue (Regresión)

Este directorio contiene el desarrollo de las etapas finales de la metodología CRISP-DM, donde se entrenan modelos de aprendizaje automático para predecir el score de rendimiento de los jugadores de eSports, se evalúan frente a métricas estándar y se despliega una interfaz interactiva.

---

## Caso de Estudio: Predicción de Desempeño

El objetivo de esta fase es implementar un modelo de regresión robusto capaz de predecir el Score de Rendimiento (performance_score) basado en estadísticas físicas y de partida del jugador.

### Rol de los Archivos en este Directorio

*   **[HectorAguila_Ev03_Regresion_eSports.ipynb](HectorAguila_Ev03_Regresion_eSports.ipynb):** Jupyter Notebook con el flujo completo de modelado de regresión, incluyendo el entrenamiento de regresiones lineales (MCO, Ridge) y no lineales (Árboles de Decisión), cálculo de métricas de generalización (R², MAE, MSE, RMSE) e interfaz interactiva embebida con ipywidgets.
*   **[PROCESO_DE_ANALISIS_MR.md](PROCESO_DE_ANALISIS_MR.md):** Reporte técnico formal en Markdown que detalla el entrenamiento de los 3 modelos, la interpretación del ajuste perfecto (R² = 1.0000) por el carácter sintético del dataset y la justificación del modelo campeón.
*   **[PROCESO_DE_ANALISIS_MR.pdf](PROCESO_DE_ANALISIS_MR.pdf):** Copia en PDF del reporte técnico de regresión, optimizada para descarga directa y evaluación formal de la asignatura.
*   **[app.py](app.py):** Código de la interfaz interactiva web construida con Streamlit para realizar predicciones del Score de Rendimiento de forma visual y fuera del entorno de desarrollo.
*   **[run_streamlit.sh](run_streamlit.sh):** Script bash ejecutable que levanta la aplicación web de Streamlit resolviendo las rutas y el entorno virtual correspondiente de forma automática.
*   **[best_model.joblib](best_model.joblib):** Pipeline del modelo campeón de regresión (Regresión Lineal) serializado para producción (incluye el escalador de variables y el estimador ajustado).
*   **[esports_player_performance_clean.csv](esports_player_performance_clean.csv):** Dataset limpio y depurado tras los filtros del EDA, utilizado directamente como entrada para los modelos de regresión.
*   **[Learning_MR.md](Learning_MR.md):** Guía conceptual de estudio personal que reúne fórmulas de regularización Ridge/Lasso, análisis de sobreajuste y métricas de error. *(Nota: Archivo local personal, ignorado en Git).*
*   **[Learning_MR_Aterrizado.md](Learning_MR_Aterrizado.md):** Bitácora complementaria de estudio personal con un enfoque pragmático para preparar la defensa oral. *(Nota: Archivo local personal, ignorado en Git).*
*   **[Instrucciones/](Instrucciones/):** Directorio local que contiene las pautas y rúbricas correspondientes a la Parcial 3 de la universidad. *(Nota: Directorio local, ignorado en Git).*
*   **[receipt-*.txt](receipt-2026_1_PM_FMY0100_24489350_PCT-Evaluacio%CC%81n%20Parcial%203%20Modelos%20de%20Regresio%CC%81n%2025.txt):** Comprobante oficial de recepción de la entrega en el portal digital de la universidad. *(Nota: Archivo local, ignorado en Git).*

---

## Descubrimientos de la Iteración y Validación de Leakage

Durante las pruebas iniciales, los modelos de Regresión Lineal y Regresión Ridge arrojaron un coeficiente de determinación perfecto (R^2 = 1.0000 y errores de 0.00). Para verificar si esto se debía a una fuga de datos (target leakage):

1. Se removieron del entrenamiento las variables del resultado de partida como `win_probability` y `mvp_award` (que registran información de post-partida).
2. Tras la remoción, los modelos lineales mantuvieron un R^2 = 1.0000.
3. **Conclusión:** Se determinó que el dataset provisto es 100% sintético y determinista. La variable objetivo se calcula mediante una combinación lineal exacta de los atributos del jugador sin ruido aleatorio (\epsilon = 0). Por ello, los modelos lineales logran el ajuste perfecto, mientras que los modelos basados en árboles (Árboles de Decisión, Random Forest) logran un R^2 alto pero imperfecto al aproximar funciones continuas mediante funciones escalonadas.

---

## Tecnologías y Librerías

* **Lenguaje:** Python 3.12+
* **Modelamiento:** `pandas`, `numpy`, `scikit-learn`
* **Persistencia:** `joblib`
* **Interactividad:** `ipywidgets` (interno) y `streamlit` (externo)

---

## Cómo Ejecutar la Aplicación Web (Streamlit)

Para levantar el simulador predictivo en tu entorno local:

1. **Activar el entorno virtual:**
   ```bash
   source .venv/bin/activate
   ```
2. **Asegurar dependencias:**
   Asegúrate de que el archivo `02_Modelado_Regresion/best_model.joblib` exista. Si no, ejecuta las celdas del Jupyter Notebook para generarlo.
3. **Iniciar Streamlit:**
   Ejecuta el servidor apuntando al archivo en su nueva ubicación:
   ```bash
   streamlit run 02_Modelado_Regresion/app.py
   ```
4. **Acceso:**
   Abre la URL local generada (normalmente `http://localhost:8501`).

---

**Héctor Aguila**  
*Fundamentos de Machine Learning*
