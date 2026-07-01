# Fase 1, 2 & 3: Comprensión del Negocio, de los Datos y Preparación de Datos (EDA)

Este directorio contiene el desarrollo de las etapas de Comprensión del Negocio (Business Understanding), Comprensión de los Datos (Data Understanding) y Preparación de los Datos (Data Preparation) bajo la metodología CRISP-DM, enfocada en el rendimiento competitivo en eSports.

---

## Caso de Estudio y Objetivos

El análisis exploratorio tiene como objetivo comprender la estructura del dataset de eSports y preparar las variables para modelar el rendimiento de los jugadores (performance_score).

### Rol de los Archivos en este Directorio

*   **[HectorAguila_Ev02_001D_EDA_eSports.ipynb](HectorAguila_Ev02_001D_EDA_eSports.ipynb):** Jupyter Notebook que contiene el flujo completo del análisis exploratorio (EDA), visualizaciones estadísticas, identificación de correlaciones y filtros de limpieza neurofisiológica e IQR.
*   **[PROCESO_DE_ANALISIS_EDA.md](PROCESO_DE_ANALISIS_EDA.md):** Reporte técnico formal en formato Markdown que documenta los hallazgos del EDA, decisiones de ingeniería de características, análisis de outliers y el diseño conceptual inicial.
*   **[PROCESO_DE_ANALISIS_EDA.pdf](PROCESO_DE_ANALISIS_EDA.pdf):** Copia en PDF del reporte técnico de análisis, optimizada para la descarga directa, lectura externa y evaluación formal de la asignatura.
*   **[esports_player_performance_tournament_analytics.csv](esports_player_performance_tournament_analytics.csv):** Dataset original bruto en formato CSV con el histórico de estadísticas de partida de los jugadores competitivos.
*   **[Learning_EDA.md](Learning_EDA.md):** Bitácora teórica de estudio personal que compendia conceptos clave sobre análisis exploratorio, tipos de gráficos y métricas descriptivas. *(Nota: Archivo local de uso personal, ignorado en Git).*
*   **[Instrucciones Evaluación Parcial 2 - Análisis exploratorio.pdf](Instrucciones%20Evaluacio%CC%81n%20Parcial%202%20-%20Ana%CC%81lisis%20exploratorio.pdf):** Documento oficial de la asignatura con la rúbrica y pauta formal de evaluación provista por la universidad. *(Nota: Archivo local de uso personal, ignorado en Git).*

---

## Decisiones Técnicas y Hallazgos Clave

### 1. Comprensión del Negocio y Datos
* **Variables Faltantes en el Dataset Físico:** Se identificó que, para un análisis predictivo real en eSports, el dataset se beneficiaría de variables de entorno crítico como la latencia (ping), el hardware empleado (tasa de refresco del monitor) y la carga acumulada de fatiga/horas de entrenamiento.
* **Sesgo en match_outcome:** Se detectó que aproximadamente el 100% de los registros corresponden a victorias. Debido a esta nula variabilidad (clase mayoritaria absoluta), se determinó descartar esta variable para evitar sesgos graves en cualquier modelo posterior.

### 2. Preparación y Depuración de Datos
* **Remoción de Outliers (El Límite Humano):** 
  * Se aplicó un **filtro biológico de 120 ms** a la variable `reaction_time_ms`. Tiempos de reacción inferiores a este umbral violan las capacidades neurofisiológicas humanas según estándares de la IAAF (World Athletics) y fueron tratados como fallos de registro o ruido de hardware.
  * Para los valores atípicos del extremo superior (tiempos de respuesta inusualmente lentos), se empleó el método del **Rango Intercuartílico (IQR)** para estabilizar el modelo sin perder representatividad.
* **Selección de Atributos:** Se eliminó la característica `player_id`. Al ser una variable puramente administrativa, su inclusión podría causar sobreajuste (el modelo aprendería a identificar nombres o códigos únicos en lugar de patrones generales de juego).
* **Estandarización:** Se aplicó `StandardScaler` a los datos numéricos continuos. Debido a que las variables poseen unidades y magnitudes muy distintas (milisegundos vs. número de bajas), la estandarización evita que el modelo pondere incorrectamente las características basándose únicamente en la escala de sus valores numéricos.

---

**Héctor Aguila**  
*Fundamentos de Machine Learning*
