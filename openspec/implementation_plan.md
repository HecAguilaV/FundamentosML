# Plan de Implementación: Evaluación 3 — Modelos de Regresión

Este plan detalla los pasos para abordar la Evaluación Parcial 3 (Ev3) del curso Fundamentos de Machine Learning, enfocada en las fases de Modelamiento, Evaluación y Despliegue de la metodología CRISP-DM.

## User Review Required

> [!IMPORTANT]
> **Selección de Modelos:** Proponemos entrenar los siguientes 3 modelos de regresión de `scikit-learn`:
> 1. **Regresión Lineal (Baseline):** Algoritmo simple y altamente interpretable.
> 2. **Árbol de Decisión (Regressor):** Captura relaciones no lineales y es intuitivo.
> 3. **Random Forest (Regressor):** Modelo de ensamble que mejora la generalización y reduce el sobreajuste.
> ¿Estás de acuerdo con esta selección de algoritmos o preferís incluir algún otro?

> [!NOTE]
> **División de Datos:** Se propone usar un split estándar de 80% entrenamiento y 20% prueba con una semilla fija (`random_state=42`) para asegurar la reproducibilidad de los resultados.

## Proposed Changes

Crearemos un nuevo Jupyter Notebook estructurado según CRISP-DM en la raíz del proyecto.

### FundamentosML

#### [NEW] [HectorAguila_Ev03_Regresion_eSports.ipynb](file:///home/hector/Escritorio/FundamentosML/HectorAguila_Ev03_Regresion_eSports.ipynb)
Este notebook contendrá el desarrollo completo de la Ev3:
- **Fase 1 & 2: Comprensión del Negocio y Datos (Resumen):** Documentación breve sobre el target `performance_score` y el problema de regresión.
- **Fase 3: Preparación de Datos (Replicación y Mejoras):**
  - Carga del dataset `esports_player_performance_tournament_analytics.csv`.
  - Limpieza de outliers en `reaction_time_ms` (filtro neurofisiológico de < 120ms y técnica IQR).
  - Eliminación de características ruidosas (`player_id`, `match_outcome`).
  - Codificación One-Hot de variables categóricas (`player_role`, `team_name`, `map_played`, `match_type`).
  - Escalamiento de variables numéricas mediante `StandardScaler`.
- **Fase 4: Modelamiento:**
  - División del dataset (80/20 train/test).
  - Entrenamiento de Regresión Lineal, Árbol de Decisión y Random Forest.
- **Fase 5: Evaluación:**
  - Cálculo de métricas ($R^2$, MAE, MSE, RMSE) para los tres modelos en entrenamiento y prueba.
  - Tabla comparativa de resultados.
  - Justificación detallada del mejor modelo basándose en la generalización.
- **Fase 6: Despliegue:**
  - Formulario interactivo en el notebook utilizando `ipywidgets` para ingresar nuevos registros y predecir el score de rendimiento en tiempo real.

---

## Verification Plan

### Automated Tests
- Validar la sintaxis de Python en el nuevo notebook mediante análisis estático.
- Ejecutar el notebook completo de principio a fin para confirmar que no ocurran excepciones.

### Manual Verification
- Probar el formulario interactivo en el notebook para asegurar que responde correctamente al cambiar los inputs.
- Validar las predicciones del modelo en tiempo real.
