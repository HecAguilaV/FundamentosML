# Informe Técnico: Modelado, Evaluación y Despliegue (Fases 4-6 CRISP-DM)

**Autor:** Héctor Aguila  
**Proyecto:** Predicción de Desempeño en eSports  
**Metodología:** CRISP-DM  

---

## 1. Fase: Modelamiento (Modeling)

### 1.1. Estrategia de Validación
Se empleó una partición estándar de datos:
* **Train/Test Split:** 80% de los datos para entrenamiento y 20% para evaluación externa.
* **Reproducibilidad:** Se fijó una semilla aleatoria (`random_state = 42`) para asegurar consistencia en las comparaciones de los modelos.

### 1.2. Selección de Algoritmos
Se seleccionaron tres alternativas de modelos con diferentes arquitecturas para evaluar su comportamiento frente a los datos:
1. **Regresión Lineal (Baseline):** Modelo fundamental para capturar relaciones lineales y proveer máxima interpretabilidad en la ponderación de coeficientes.
2. **Regresión Ridge (Regularización L2):** Variante lineal que introduce una penalización sobre los coeficientes grandes para prevenir el sobreajuste y mitigar problemas de multicolinealidad.
3. **Árbol de Decisión Regresor (No Lineal):** Algoritmo no paramétrico que divide el espacio de características en regiones ortogonales, útil para capturar interacciones no lineales complejas sin necesidad de escalamiento de datos.

---

## 2. Fase: Evaluación (Evaluation)

### 2.1. Métricas de Evaluación
Para comparar la precisión y generalización de los modelos, se calcularon las siguientes métricas estadísticas en los conjuntos de entrenamiento y prueba:
* **Coeficiente de Determinación ($R^2$):** Proporción de la varianza del target explicada por el modelo.
* **Error Absoluto Medio (MAE):** Promedio de las diferencias absolutas entre las predicciones y los valores reales.
* **Error Cuadrático Medio (MSE) y su Raíz (RMSE):** Penaliza los errores de mayor magnitud, midiendo la desviación estándar de los residuos.

### 2.2. Resultados y Comparación de Modelos

| Modelo                | $R^2$ (Train) | $R^2$ (Test) | MAE (Test) | RMSE (Test) |            Generalización            |
| :-------------------- | :-----------: | :----------: | :--------: | :---------: | :----------------------------------: |
| **Regresión Lineal**  |    1.0000     |    1.0000    |   0.0000   |   0.0000    |     Excelente (Ajuste Perfecto)      |
| **Regresión Ridge**   |    1.0000     |    1.0000    |   0.0001   |   0.0001    |     Excelente (Ajuste Perfecto)      |
| **Árbol de Decisión** |    1.0000     |    0.9412    |   2.5120   |   3.1245    | Sobreajuste leve (Típico de árboles) |

### 2.3. Análisis Crítico del Ajuste Perfecto ($R^2 = 1.0000$) y Segunda Iteración
Obtener un error de cero absoluto ($MAE = 0.00$ y $R^2 = 1.0000$) en datos de rendimiento humano es una anomalía estadística severa. Un factor clave que despertó sospechas fue que, durante la fase de depuración y limpieza de outliers (tanto por el filtro biológico de 120 ms como por el método IQR), **solo se eliminaron 8 registros en total**, entrenando con el 98.4% del dataset original. 

Con casi todo el dataset intacto y sin ruido típico de la conducta humana, un ajuste perfecto indicaba una de dos opciones: *Target Leakage* (fuga de información) o un dataset sintético determinista. Esto motivó una segunda iteración de CRISP-DM para auditar el flujo:
1. **Auditoría:** Se identificaron las variables de resultado de partida (`win_probability` y `mvp_award`) como posibles variables filtradoras del target.
2. **Prueba:** Se reentrenaron los modelos excluyendo estas variables del conjunto de entrenamiento.
3. **Resultado:** Los modelos lineales (Regresión Lineal y Ridge) **siguieron obteniendo un $R^2 = 1.0000$ perfecto**.
4. **Conclusión Científica:** Se demostró matemáticamente que el dataset es **100% sintético y determinista lineal**. La variable objetivo `performance_score` se calcula mediante una combinación lineal exacta de los atributos del jugador sin un término de error aleatorio ($\epsilon = 0$). Los algoritmos lineales descubren esta fórmula exacta, mientras que el Árbol de Decisión obtiene un $R^2$ menor debido a que aproxima una función continua mediante escalones.

**Decisión del Mejor Modelo:** Se seleccionó **Regresión Lineal** (o Ridge con regularización despreciable) por su capacidad de reproducir de manera exacta la función generadora de datos con costo computacional mínimo.

---

## 3. Fase: Despliegue (Deployment)

Para dar valor práctico al modelo desarrollado y permitir simulaciones interactivas por parte del cuerpo técnico de eSports, se implementaron dos niveles de despliegue:

* **Despliegue Interno (Jupyter):** Un formulario dinámico construido en el notebook mediante `ipywidgets` que permite cambiar parámetros de juego y observar la predicción del modelo de forma instantánea.
* **Despliegue Externo (Web App):** Una aplicación independiente en **Streamlit** ([`app.py`](file:///home/hector/Escritorio/FundamentosML/02_Modelado_Regresion/app.py)) que carga el pipeline serializado en [`best_model.joblib`](file:///home/hector/Escritorio/FundamentosML/02_Modelado_Regresion/best_model.joblib). Esta interfaz limpia y amigable permite simular escenarios de rendimiento de jugadores competitivos en tiempo real fuera de cualquier entorno de código.

---

## 4. Declaración de Uso de IA Generativa

De acuerdo con las buenas prácticas de honestidad académica y uso responsable de tecnologías:
* **Uso de Herramientas:** Se declara el uso de asistentes de IA generativa como soporte para el refinamiento de la documentación técnica (Markdown), optimización estética de las visualizaciones y asistencia en el desarrollo de la interfaz interactiva en Streamlit.
* **Validación Humana:** Toda decisión de diseño arquitectónico, análisis de métricas ($R^2$, MAE, RMSE), depuración de outliers (método IQR y filtro biológico) y justificación de selección de modelos (Regresión Lineal por Parsimonia) fue auditada, validada y liderada en su totalidad por el autor del trabajo.
