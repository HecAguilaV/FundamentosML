# Fundamentos de Machine Learning — CRISP-DM

Este repositorio contiene los proyectos prácticos y evaluaciones desarrollados para la asignatura **Fundamentos de Machine Learning**, estructurados bajo la metodología estándar de la industria **CRISP-DM** (Cross-Industry Standard Process for Data Mining) y validados por pruebas de calidad de código automáticas.

---

## 🎮 Caso de Estudio: Predicción de Desempeño en eSports (Evaluación 3)

El proyecto principal consiste en desarrollar un sistema predictivo para estimar el **Score de Rendimiento** (`performance_score`) de jugadores profesionales de eSports basado en métricas físicas, de partida y neurofisiológicas.

### 📁 Estructura del Proyecto

*   **[`HectorAguila_Ev03_Regresion_eSports.ipynb`](file:///home/hector/Escritorio/FundamentosML/HectorAguila_Ev03_Regresion_eSports.ipynb):** Notebook Jupyter principal con las fases CRISP-DM completas:
    1.  *Business Understanding* (Comprensión del Negocio)
    2.  *Data Understanding* (Comprensión de los Datos)
    3.  *Data Preparation* (Tratamiento de nulos, exclusión neurofisiológica, remoción de outliers con IQR, codificación y escalamiento).
    4.  *Modeling* (Entrenamiento de Regresión Lineal, Árbol de Decisión y Random Forest).
    5.  *Evaluation* (Comparativa de métricas: $R^2$, MAE, MSE, RMSE).
    6.  *Deployment* (Formulario interactivo interno con `ipywidgets` y serialización del modelo).
    7.  *Iteración 2* (Diagnóstico crítico de target leakage y validación de la naturaleza sintética del dataset).
*   **[`app.py`](file:///home/hector/Escritorio/FundamentosML/app.py):** Aplicación interactiva externa construida en **Streamlit** que proporciona una interfaz web premium para que entrenadores o usuarios finales realicen simulaciones predictivas.
*   **[`esports_player_performance_clean.csv`](file:///home/hector/Escritorio/FundamentosML/esports_player_performance_clean.csv):** Dataset depurado y exportado durante la fase de preparación de datos.
*   **[`best_model.joblib`](file:///home/hector/Escritorio/FundamentosML/best_model.joblib):** Pipeline del mejor modelo entrenado serializado en disco (incluye el preprocesamiento y el regresor lineal).
*   **[`legacy/`](file:///home/hector/Escritorio/FundamentosML/legacy):** Directorio de respaldo que contiene el análisis exploratorio inicial (Ev2) y el dataset crudo original.

---

## 🔬 Descubrimientos de la Iteración 2 (CRISP-DM Iterative Loop)

Durante la evaluación inicial, el modelo de **Regresión Lineal** logró un coeficiente de determinación perfecto ($R^2 = 1.0000$ y errores absolutos de $0.00$). Para validar este resultado, se realizó una segunda iteración de CRISP-DM:
1.  **Diagnóstico de Target Leakage:** Se removieron las variables de resultado de partida `win_probability` y `mvp_award` para verificar si filtraban información futura del target.
2.  **Resultado:** El modelo lineal **mantuvo el $R^2 = 1.0000$**.
3.  **Conclusión Científica:** Esto demuestra la ausencia de target leakage y confirma que el dataset es **100% sintético y determinista**. La variable de rendimiento se genera mediante una fórmula matemática lineal sin ruido aleatorio ($\epsilon = 0$) a partir de los atributos de juego.

---

## 🛠️ Tecnologías y Librerías

*   **Lenguaje:** Python 3.12+
*   **Modelamiento:** `pandas`, `numpy`, `scikit-learn`
*   **Visualización:** `matplotlib`, `seaborn`
*   **Interactividad:** `ipywidgets` (interno) y `streamlit` (externo)
*   **Persistencia:** `joblib`

---

## 🚀 Cómo Ejecutar la Aplicación Web (Streamlit)

Para levantar el simulador interactivo en tu entorno local, sigue estos pasos:

1.  **Activar el entorno virtual:**
    ```bash
    source .venv/bin/activate
    ```
2.  **Asegurar que el modelo esté entrenado:**
    Asegúrate de que el archivo `best_model.joblib` exista en la raíz del proyecto. Si no existe, ejecuta todas las celdas del Jupyter Notebook para generarlo.
3.  **Iniciar el servidor de Streamlit:**
    ```bash
    streamlit run app.py
    ```
4.  **Acceder al navegador:**
    Abre la URL local generada (normalmente `http://localhost:8501`).

---

## 🛡️ Calidad de Código (Gentleman Guardian Angel)

Este repositorio utiliza **GGA** (Gentleman Guardian Angel) para automatizar la revisión de código basada en IA antes de cada confirmación de cambios.
*   Directrices de revisión en [`AGENTS.md`](file:///home/hector/Escritorio/FundamentosML/AGENTS.md).
*   Configuración en [`.gga`](file:///home/hector/Escritorio/FundamentosML/.gga).
