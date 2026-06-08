# Fundamentos de Machine Learning — Proyecto eSports

Este repositorio contiene los proyectos prácticos desarrollados para la asignatura **Fundamentos de Machine Learning**, estructurados bajo la metodología estándar de la industria **CRISP-DM** (Cross-Industry Standard Process for Data Mining) para analizar y modelar el rendimiento de jugadores competitivos de eSports.

---

## 📌 Estructura del Proyecto

El ciclo del proyecto está dividido en etapas modulares correspondientes a las fases de la metodología CRISP-DM:

| Etapa | Proceso Desarrollado | Descripción | Enlace al Detalle |
| :--- | :--- | :--- | :--- |
| **01** | **EDA eSports** | Comprensión del Negocio, Comprensión de los Datos y Preparación de Datos. Limpieza neurofisiológica y filtros biológicos. | [📁 README 01_EDA_Esports](file:///home/hector/Escritorio/FundamentosML/01_EDA_Esports/README.md) |
| **02** | **Modelado de Regresión** | Entrenamiento de modelos lineales y basados en árboles, evaluación de generalización y despliegue interactivo con Streamlit. | [📁 README 02_Modelado_Regresion](file:///home/hector/Escritorio/FundamentosML/02_Modelado_Regresion/README.md) |

---

## 🎮 Caso de Estudio: Predicción de Desempeño en eSports

El objetivo principal es predecir el **Score de Rendimiento** (`performance_score`) de los jugadores basándose en métricas físicas, neurofisiológicas y estadísticas de partidas anteriores.

### Métricas Clave y Preprocesamiento
* **Filtro Neurofisiológico de Reacción:** Remoción de registros con tiempos de reacción inferiores al límite biológico humano (~120 ms) según estándares de la IAAF, eliminando ruido de entrada.
* **Modelos Entrenados:** Regresión Lineal, Regresión Ridge, Árboles de Decisión y Ensembles (Random Forest).
* **Descubrimiento Científico:** Se demostró mediante un análisis iterativo de *target leakage* que el dataset provisto es de naturaleza sintética y determinista pura, permitiendo que los modelos lineales alcancen un ajuste perfecto ($R^2 = 1.0000$).

---

## 🛠️ Requisitos e Instalación

Para explorar los notebooks y levantar la aplicación web interactiva localmente, sigue estos pasos:

### 1. Clonar el repositorio y acceder a la carpeta
```bash
git clone <url-del-repositorio>
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
* **Notebook de EDA:** Abre y ejecuta [01_EDA_Esports/HectorAguila_Ev02_001D_EDA_eSports.ipynb](file:///home/hector/Escritorio/FundamentosML/01_EDA_Esports/HectorAguila_Ev02_001D_EDA_eSports.ipynb)
* **Notebook de Modelamiento:** Abre y ejecuta [02_Modelado_Regresion/HectorAguila_Ev03_Regresion_eSports.ipynb](file:///home/hector/Escritorio/FundamentosML/02_Modelado_Regresion/HectorAguila_Ev03_Regresion_eSports.ipynb)
* **Aplicación Streamlit:**
  ```bash
  streamlit run 02_Modelado_Regresion/app.py
  ```

---

**Héctor Aguila**  
*Fundamentos de Machine Learning*
