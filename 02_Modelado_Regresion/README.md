# Fase 4, 5 & 6: Modelado, Evaluación y Despliegue (Regresión)

Este directorio contiene el desarrollo de las etapas finales de la metodología CRISP-DM, donde se entrenan modelos de aprendizaje automático para predecir el score de rendimiento de los jugadores de eSports, se evalúan frente a métricas estándar y se despliega una interfaz interactiva.

---

## 🎮 Caso de Estudio: Predicción de Desempeño

El objetivo de esta fase es implementar un modelo de regresión robusto capaz de predecir el **Score de Rendimiento** (`performance_score`) basado en estadísticas físicas y de partida del jugador.

### 📁 Estructura de esta Etapa

* **[`HectorAguila_Ev03_Regresion_eSports.ipynb`](file:///home/hector/Escritorio/FundamentosML/02_Modelado_Regresion/HectorAguila_Ev03_Regresion_eSports.ipynb):** Jupyter Notebook con el flujo completo de:
  1. Replicación del preprocesamiento y limpieza definidos en el EDA.
  2. Modelamiento y entrenamiento de algoritmos (**Regresión Lineal**, **Regresión Ridge** y **Árbol de Decisión**).
  3. Evaluación matemática del rendimiento en entrenamiento y prueba.
  4. Formulario interactivo integrado usando `ipywidgets`.
* **[`INFORME_TECNICO.md`](file:///home/hector/Escritorio/FundamentosML/02_Modelado_Regresion/INFORME_TECNICO.md):** Reporte técnico formal que detalla el modelado, la justificación de algoritmos y el análisis del ajuste perfecto ($R^2 = 1.0000$).
* **[`app.py`](file:///home/hector/Escritorio/FundamentosML/02_Modelado_Regresion/app.py):** Aplicación interactiva construida en **Streamlit** que expone una interfaz gráfica para predecir en tiempo real fuera del entorno de Jupyter.
* **[`esports_player_performance_clean.csv`](file:///home/hector/Escritorio/FundamentosML/02_Modelado_Regresion/esports_player_performance_clean.csv):** Dataset depurado después de la limpieza de outliers (filtro neurofisiológico e IQR) y transformaciones.
* **[`best_model.joblib`](file:///home/hector/Escritorio/FundamentosML/02_Modelado_Regresion/best_model.joblib):** Pipeline del mejor modelo entrenado serializado en disco (incluye el preprocesador `StandardScaler` y el regresor lineal final).

---

## 🔬 Descubrimientos de la Iteración y Validación de Leakage

Durante las pruebas iniciales, los modelos de **Regresión Lineal** y **Regresión Ridge** arrojaron un coeficiente de determinación perfecto ($R^2 = 1.0000$ y errores de $0.00$). Para verificar si esto se debía a una fuga de datos (*target leakage*):

1. Se removieron del entrenamiento las variables del resultado de partida como `win_probability` y `mvp_award` (que registran información de post-partida).
2. Tras la remoción, los modelos lineales **mantuvieron un $R^2 = 1.0000$**.
3. **Conclusión:** Se determinó que el dataset provisto es **100% sintético y determinista**. La variable objetivo se calcula mediante una combinación lineal exacta de los atributos del jugador sin ruido aleatorio ($\epsilon = 0$). Por ello, los modelos lineales logran el ajuste perfecto, mientras que los modelos basados en árboles (Árboles de Decisión, Random Forest) logran un $R^2$ alto pero imperfecto al aproximar funciones continuas mediante funciones escalonadas.

---

## 🛠️ Tecnologías y Librerías

* **Lenguaje:** Python 3.12+
* **Modelamiento:** `pandas`, `numpy`, `scikit-learn`
* **Persistencia:** `joblib`
* **Interactividad:** `ipywidgets` (interno) y `streamlit` (externo)

---

## 🚀 Cómo Ejecutar la Aplicación Web (Streamlit)

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
