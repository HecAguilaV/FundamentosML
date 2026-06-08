# Informe Técnico: Comprensión y Preparación de Datos (Fases 1-3 CRISP-DM)

**Autor:** Héctor Aguila  
**Proyecto:** Predicción de Desempeño en eSports  
**Metodología:** CRISP-DM  

---

## 1. Fase: Comprensión del Negocio (Business Understanding)

### 1.1. Objetivos del Proyecto
El objetivo del negocio es optimizar el rendimiento de las escuadras de eSports mediante analítica de datos. Para ello, se definieron dos líneas de acción:
* **Predicción de Rendimiento (Enfoque Adoptado):** Utilizar modelos de regresión para estimar el `performance_score` (variable continua) a partir de métricas intra-partida y físicas del jugador.
* **Detección de Talento:** Evaluar el perfil de jugadores sobresalientes para reclutamiento o selección de MVPs.

### 1.2. Brechas de Datos Identificadas
El dataset provisto contiene métricas básicas, pero en eSports de alto rendimiento, la toma de decisiones requiere factores del entorno del jugador. Se propone incorporar a futuro:
* **Latencia de Red (Ping):** La fluctuación en el tiempo de respuesta del servidor (jitter/lag) es un factor crítico en el desempeño de un jugador profesional.
* **Tasa de Refresco del Monitor (Hz):** El hardware utilizado (frecuencia de muestreo y refresco del periférico/pantalla) influye directamente en los tiempos de respuesta medidos.
* **Carga Cognitiva y Fatiga:** Horas acumuladas de entrenamiento y horas de sueño previo al torneo.

---

## 2. Fase: Comprensión de los Datos (Data Understanding)

### 2.1. Clasificación Metodológica de Variables
Para estructurar el análisis y elegir las transformaciones correctas, las variables se clasificaron según su tipo estadístico:
* **Nominales:** `player_role`, `team_name`, `map_played`, `match_type`, `player_id` (administrativa).
* **Ordinales:** `tournament_stage`.
* **Continuas (Métricas de Desempeño):** `reaction_time_ms`, `win_probability`, `performance_score` (Target).
* **Discretas:** `kills`, `deaths`, `assists`, `headshot_accuracy` (porcentaje/proporción), `kda_ratio`.

### 2.2. Análisis Crítico de la Variable `match_outcome`
Al analizar la distribución de `match_outcome`, se detectó que aproximadamente el **100% de los registros corresponden a victorias**. 
* **Decisión Técnica:** Se determinó excluir esta variable. La ausencia total de varianza (clase negativa) impide que cualquier modelo aprenda patrones de derrota, induciendo un sesgo de generalización severo.

---

## 3. Fase: Preparación de Datos (Data Preparation)

### 3.1. Tratamiento de Outliers (Filtro Físico y Estadístico)
La limpieza de valores atípicos se abordó bajo dos criterios complementarios:

1. **Umbral Neurofisiológico Humano (Filtro Biológico):**
   * Se eliminaron todos los registros donde `reaction_time_ms < 120`. 
   * **Justificación:** Según investigaciones de la IAAF (World Athletics) para la detección de salidas en falso, el tiempo mínimo de reacción humana ante un estímulo táctil/auditivo es de 120 ms. Valores inferiores representan ruido del hardware de captura, fallas de sincronización o anomalías del motor de juego, y su presencia distorsiona la relación real del rendimiento físico.
2. **Filtro Estadístico (Rango Intercuartílico - IQR):**
   * Para los tiempos de reacción extremadamente altos (jugadores inusualmente lentos), se aplicó el método IQR en las colas de la distribución para asegurar que el modelo se entrene con datos representativos del juego competitivo estándar.

### 3.2. Exclusión de Atributos Ruidores
* Se removió la variable `player_id`. 
* **Justificación:** Los identificadores únicos generan alta cardinalidad sin valor predictivo real. El modelo debe aprender a inferir el rendimiento en base a habilidades de juego (precisión, bajas, tiempo de reacción) y no memorizar un código de identificación.

### 3.3. Estandarización y Escalamiento
* Se aplicó la transformación `StandardScaler` (Media = 0, Desviación Estándar = 1) a los atributos numéricos continuos.
* **Justificación:** Variables como `reaction_time_ms` (cientos de unidades) y `kills` (decenas) tienen escalas marcadamente dispares. La estandarización previene el sesgo de magnitud, garantizando que el optimizador del modelo evalúe cada variable por su varianza y no por su escala numérica.

---

## 4. Conclusiones y Siguientes Pasos
El proceso de EDA e ingeniería de características transformó un dataset crudo y ruidoso en un conjunto de datos estandarizado y libre de variables administrativas o sesgadas. Los datos limpios proveen la base sólida requerida para el entrenamiento robusto de algoritmos de regresión.
