# Fundamentos de Machine Learning - Proyecto eSports

Este repositorio contiene los proyectos prácticos desarrollados para la asignatura Fundamentos de Machine Learning, estructurados bajo la metodología estándar de la industria CRISP-DM (Cross-Industry Standard Process for Data Mining) para analizar y modelar el rendimiento de jugadores competitivos de eSports.

---

## Estructura del Proyecto

El ciclo del proyecto está dividido en etapas modulares correspondientes a las fases de la metodología CRISP-DM:

| Etapa        | Proceso Desarrollado                | Descripción                                                                                                                    | Enlace al Detalle                                                                            | Informe Técnico / Bitácora                                                 |
| :----------- | :---------------------------------- | :------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------- |
| **01** | **EDA eSports**               | Comprensión del Negocio, Comprensión de los Datos y Preparación de Datos. Limpieza neurofisiológica y filtros biológicos.  | [README 01_EDA_Esports](01_EDA_Esports/README.md)                                               | [PROCESO_DE_ANALISIS_EDA.md](01_EDA_Esports/PROCESO_DE_ANALISIS_EDA.md)         |
| **02** | **Modelado de Regresión**    | Entrenamiento de modelos lineales y basados en árboles, evaluación de generalización y despliegue interactivo con Streamlit. | [README 02_Modelado_Regresion](02_Modelado_Regresion/README.md)                                 | [PROCESO_DE_ANALISIS_MR.md](02_Modelado_Regresion/PROCESO_DE_ANALISIS_MR.md)    |
| **03** | **Modelos de Clasificación** | Modelado de clasificación binaria de victorias/derrotas. Mitigación de data leakage, curvas ROC/PR y despliegue en Streamlit. | [Jupyter Notebook Ev04](03_Modelos_Clasificacion/HectorAguila_Ev04_Clasificacion_eSports.ipynb) | [PROCESO_DE_ANALISIS_MC.md](03_Modelos_Clasificacion/PROCESO_DE_ANALISIS_MC.md) |

---

## Caso de Estudio: Predicción de Desempeño en eSports

El objetivo principal es predecir el Score de Rendimiento (performance_score) de los jugadores basándose en métricas físicas, neurofisiológicas y estadísticas de partidas anteriores.

### Métricas Clave y Preprocesamiento

* **Filtro Neurofisiológico de Reacción:** Remoción de registros con tiempos de reacción inferiores al límite biológico humano (~120 ms) según estándares de la IAAF, eliminando ruido de entrada.
* **Modelos Entrenados:** Regresión Lineal, Regresión Ridge, Árboles de Decisión y Ensembles (Random Forest).
* **Descubrimiento Científico:** Se demostró mediante un análisis iterativo de target leakage que el dataset provisto es de naturaleza sintética y determinista pura, permitiendo que los modelos lineales alcancen un ajuste perfecto (R^2 = 1.0000).

---

## Requisitos e Instalación

Para explorar los notebooks y levantar la aplicación web interactiva localmente, sigue estos pasos:

### 1. Clonar el repositorio y acceder a la carpeta

```bash
git clone https://github.com/HecAguilaV/FundamentosML.git
cd FundamentosML
```

### 2. Configurar el Entorno Virtual (Python 3.12+)

```bash
# Crear entorno virtual
python3 -m venv .venv

# Activar entorno virtual
source .venv/bin/activate

# Instalar las dependencias necesarias
pip install pandas numpy scikit-learn matplotlib seaborn streamlit joblib ipywidgets
```

### 3. Ejecutar las Etapas

* **Notebook de EDA:** Abre y ejecuta [01_EDA_Esports/HectorAguila_Ev02_001D_EDA_eSports.ipynb](01_EDA_Esports/HectorAguila_Ev02_001D_EDA_eSports.ipynb)
* **Notebook de Modelamiento (Regresión):** Abre y ejecuta [02_Modelado_Regresion/HectorAguila_Ev03_Regresion_eSports.ipynb](02_Modelado_Regresion/HectorAguila_Ev03_Regresion_eSports.ipynb)
* **Notebook de Modelamiento (Clasificación):** Abre y ejecuta [03_Modelos_Clasificacion/HectorAguila_Ev04_Clasificacion_eSports.ipynb](03_Modelos_Clasificacion/HectorAguila_Ev04_Clasificacion_eSports.ipynb)
* **Aplicación de Regresión (Streamlit):**
  ```bash
  streamlit run 02_Modelado_Regresion/app.py
  ```
* **Aplicación de Clasificación (Streamlit):**
  ```bash
  streamlit run 03_Modelos_Clasificacion/app.py
  ```

---

**Héctor Aguila**
*Fundamentos de Machine Learning*
