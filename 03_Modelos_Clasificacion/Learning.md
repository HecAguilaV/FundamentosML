# Guía de Preparación y Defensa Oral: Modelos de Clasificación

Esta guía explica en un lenguaje sencillo, didáctico y directo los conceptos clave del informe técnico y del notebook de clasificación. Su objetivo es proporcionar las herramientas conceptuales para defender exitosamente el proyecto ante una interrogación oral del docente.

---

## 1. El Concepto de Data Leakage (Fuga de Datos) y la División Temprana

### ¿Qué es de forma sencilla?
El *Data Leakage* ocurre cuando el modelo de Machine Learning, durante su entrenamiento, tiene acceso a información que en el mundo real no debería conocer (información del conjunto de prueba o "del futuro"). Es el equivalente a que un alumno tenga las respuestas del examen antes de rendirlo; su nota será perfecta, pero no sabrá nada cuando le pregunten otra cosa.

### ¿Cómo se previene en el código y por qué se hace una "división temprana"?
1. **El Split Primero:** Lo primero que se hace es separar los datos (80% entrenamiento, 20% prueba). No se calcula ninguna media, escala ni valor promedio antes de esto.
2. **El Pipeline al Rescate:** En el código se utiliza un `Pipeline` que envuelve el preprocesamiento (`StandardScaler`) y el modelo.
   * Al hacer `pipeline.fit(X_train, y_train)`, el escalador calcula la media y desviación estándar **únicamente usando el 80% de entrenamiento**.
   * Cuando se evalúa en el conjunto de prueba (`X_test`), el escalador aplica esos parámetros calculados en el entrenamiento, sin enterarse de las estadísticas reales del conjunto de prueba.
3. **Defensa ante el Docente:** 
   > *"Profesor, la división temprana y el uso de Pipelines garantizan que el preprocesamiento de datos se ajuste estrictamente sobre el conjunto de entrenamiento. Esto evita la fuga de información (data leakage) hacia el conjunto de prueba, asegurando una evaluación honesta de la capacidad de generalización del modelo."*

### 🔍 Dónde ubicarlo en el Notebook:
* **División Temprana (Train/Test Split):**
  * Se encuentra en el bloque de código de las **líneas 324 a 334**.
  * Verás la importación de `train_test_split` y la partición usando `stratify=y` y `random_state=42`.
* **Configuración del Preprocesador (Pipeline):**
  * Se detalla a partir de la **línea 349** (sección `3.3. Configuración del Preprocesador`) y se define formalmente en el bloque de código de las **líneas 435 a 451**.
  * Ahí se crean `pipeline_lr`, `pipeline_knn` y `pipeline_rf`, encadenando el escalado numérico (`StandardScaler`), la codificación categórica (`OneHotEncoder`) y sus respectivos algoritmos.
* **Entrenamiento con `fit`:**
  * En las **líneas 458 a 464**, verás que se ejecuta `.fit(X_train, y_train)` por separado para cada uno de los pipelines.

---

## 2. La Justificación del Cambio de Target (Variable Objetivo)

### ¿Qué problema había con el target inicial?
Originalmente, el objetivo era predecir el resultado de la partida (`match_outcome` - Victoria/Derrota). Sin embargo, al auditar los datos se encontró una distribución de:
* **2793 victorias**
* **7 derrotas**

### ¿Por qué esto es inservible para Machine Learning?
Esto se conoce como un **desbalance extremo de clases**. Si un modelo simplemente predice siempre "victoria" (sin mirar ninguna estadística del jugador), tendrá un **99.75% de exactitud (Accuracy)**. El modelo no aprendería nada y la evaluación sería engañosa.

### ¿Por qué se eligió `mvp_award`?
Al cambiar la variable objetivo a `mvp_award` (2561 registros "No" vs. 239 "Sí"), el desbalance es de aproximadamente 90% a 10%. Esto es un escenario de clasificación binaria real donde la clase minoritaria (obtener el MVP) tiene suficiente volumen para que el modelo aprenda a identificar los patrones que diferencian a un MVP de un jugador común.

### 🔍 Dónde ubicarlo en el Notebook:
* Esto se explica teórica y visualmente en la **Fase 1.3** del bloque inicial del informe embebido (el markdown introductorio del notebook, **líneas 31 en adelante**), bajo el título *"Auditoría del Dataset y Decisión de Ingeniería de Cambio de Target"*.

---

## 3. Entendiendo los Tres Algoritmos con "Peras y Manzanas"

Si el profesor pregunta: *"¿Cómo funciona este modelo que usaste?"*, las respuestas clave son:

### A. Regresión Logística
* **Explicación sencilla:** No es una regresión para predecir números continuos, es un clasificador. Traza una línea (o hiperplano) para separar las clases (MVP de No MVP). Luego, aplica una función matemática (sigmoide) que convierte la distancia de cada punto a esa línea en una probabilidad entre 0 y 1. Si la probabilidad es mayor a 0.5, clasifica como MVP.
* **Defensa:** *"Es un modelo lineal, simple y muy rápido, que sirve como una excelente línea base (baseline) probabilística".*

### B. K-Nearest Neighbors (KNN - K-Vecinos más Cercanos)
* **Explicación sencilla:** Clasifica buscando la similitud geométrica. Si queremos predecir un jugador nuevo, el algoritmo busca a los $K$ jugadores más parecidos (en este caso, 5 vecinos) en el espacio de características. Si 4 de esos 5 vecinos son "No MVP", el nuevo jugador se clasifica como "No MVP".
* **Defensa:** *"Es un modelo no paramétrico basado en distancias. Es muy sensible a la escala de los datos (por eso requiere estandarización obligatoria) y al desbalance de clases".*

### C. Random Forest Classifier (Bosque Aleatorio)
* **Explicación sencilla:** En lugar de confiar en un solo árbol de decisión (que suele equivocarse o sobreajustar), entrena un "bosque" de muchos árboles independientes. Cada árbol se entrena con una muestra aleatoria de los datos y una selección aleatoria de variables. Al final, cada árbol emite su predicción y el modelo elige el resultado por votación de la mayoría.
* **Defensa:** *"Es un modelo no lineal basado en ensamble por Bagging. Es robusto ante datos ruidosos y desbalanceados gracias a la doble aleatoriedad que introduce durante el entrenamiento".*

---

## 4. ¿Por qué KNN falló (tuvo bajo rendimiento) en comparación a los otros?

En los resultados del test set se observa que KNN obtuvo un **Recall muy bajo (52.08%)** para predecir MVPs.
* **Explicación:** Al haber un desbalanceo (90% No MVP vs. 10% MVP), el espacio de datos está inundado de puntos de la clase mayoritaria (No MVP). Cuando KNN calcula las distancias para buscar los 5 vecinos más cercanos de un jugador MVP, es muy probable que algunos de esos vecinos sean "No MVP" simplemente porque hay muchos más en el mapa. Esto sesga al modelo hacia la clase mayoritaria, haciendo que no logre identificar a casi la mitad de los MVPs reales.

### 🔍 Dónde ubicarlo en el Notebook:
* Los diccionarios donde se evalúan los modelos y las matrices de confusión que demuestran este comportamiento se encuentran en la sección **4.1 (Evaluación en el conjunto de prueba)** en las **líneas 546 a 548**.
* Los gráficos y reporte de métricas donde se evidencia esta caída del Recall para KNN están inmediatamente a continuación.

---

## 5. La Explicación del Rendimiento Perfecto (100% de Métricas)

Un F1-Score y Accuracy de 1.0 (100%) en Random Forest suele ser sospechoso en la vida real. Sin embargo, aquí tiene una justificación científica clara:
* **Hipótesis del Dataset Sintético:** El dataset provisto para el curso es un dataset sintético (generado artificialmente mediante código). Las reglas para asignar la etiqueta de `mvp_award` son deterministas y perfectas (por ejemplo: si el jugador ganó la partida AND su puntaje es superior a cierto umbral).
* Al no existir ruido aleatorio en los datos de origen (el error aleatorio $\epsilon$ es cero), los cortes ortogonales de los árboles de Random Forest logran replicar y memorizar matemáticamente la regla exacta de generación.
* **Defensa:** *"Profesor, el rendimiento perfecto se debe a que el target `mvp_award` se comporta de manera determinista en este dataset sintético. La validación cruzada descarta el sobreajuste al arrojar métricas estables en todos los pliegues."*

---

## 6. ¿Qué es la Validación Cruzada (Cross-Validation)?

### Explicación con una analogía:
Imagínese que prepara un examen utilizando un banco de 100 preguntas.
* Si siempre divide las preguntas de la misma manera (80 para estudiar y 20 para evaluarse, como el split simple), corre el riesgo de tener suerte con las 20 seleccionadas o de memorizarse el patrón específico de esa partición.
* La **Validación Cruzada de 5 pliegues (5-Fold CV)** divide las preguntas en 5 grupos iguales de 20. 
* El proceso se repite 5 veces de forma rotativa: cada vez, se seleccionan 4 grupos para entrenar (estudiar) y el grupo restante para validar (evaluar).
* Al final, se promedian las 5 calificaciones obtenidas.
* **¿Para qué sirve?** Si el promedio de las evaluaciones rotativas es alto y estable (como nuestro F1-Score promedio de 0.9947), se confirma científicamente que el modelo generaliza correctamente ante cualquier conjunto de datos no visto y que no depende de una partición de datos afortunada.

### 🔍 Dónde ubicarlo en el Notebook:
* La aplicación de la validación cruzada al Random Forest mediante `cross_val_score` se realiza en la **línea 696**.
* En el bloque de salida de esta celda podrás ver los F1-Scores de cada pliegue (`[1.0000, 0.9867, 1.0000, 1.0000, 0.9867]`) y el promedio de **0.9947**.

---

## 7. Fase de Despliegue (Production & Streamlit)

* **Serialización (`best_model.joblib`):** Permite guardar el modelo entrenado y su preprocesador en un archivo binario. Esto evita tener que volver a entrenar el modelo cada vez que se abre la aplicación Streamlit.
* **Streamlit (`app.py`):** Es una librería de Python para crear interfaces web de forma rápida. La aplicación toma los valores de entrada del usuario mediante controles interactivos, los introduce en el pipeline guardado (que aplica automáticamente la escala correcta a las variables) y realiza la predicción instantánea para mostrar en pantalla si el jugador es MVP o estándar.

### 🔍 Dónde ubicarlo en el Notebook:
* La serialización de nuestro pipeline campeón se realiza usando la librería `joblib` en las **líneas 745 a 751**.
