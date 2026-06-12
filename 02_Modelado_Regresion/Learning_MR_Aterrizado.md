# Chuleta de Estudio (Versión Aterrizada): Modelado, Evaluación y Despliegue

> **El Resumen del Caso:** Entrenamos tres modelos (Lineal, Ridge y Árbol de Decisión) para predecir el rendimiento de los jugadores. Al evaluarlos, notamos algo rarísimo: un puntaje perfecto de $R^2 = 1.00$ (cero errores). Para confirmar que no estábamos haciendo trampa sin querer (Target Leakage), quitamos variables del final de la partida. ¡El puntaje seguía perfecto! Con esto demostramos que el dataset no es de humanos reales, sino que es artificial (creado con una fórmula matemática exacta). Por ser tan directo, nos quedamos con la Regresión Lineal para crear nuestra aplicación interactiva.

---

## Fase Previa: Los cimientos del proyecto (CRISP-DM 1 al 3)

Antes de modelar, hicimos el trabajo pesado. Estas son las fases previas que tenés que saber defender si el profe te pregunta de dónde salieron los datos:

* **1. Comprensión del Negocio:** El objetivo era darle a los entrenadores de eSports una herramienta para predecir el score de los jugadores basándose en sus métricas (Kills, Daño, etc.), para que puedan tomar mejores decisiones y afinar sus estrategias.
* **2. Comprensión de los Datos (EDA):** Exploramos los datos y graficamos para entenderlos. Vimos relaciones lógicas: más kills suben el score, un mal tiempo de reacción lo baja.
* **3. Preparación de los Datos (Limpieza):** Acá limpiamos la basura. Aplicamos un filtro biológico (eliminando a cualquiera con un tiempo de reacción menor a 120ms porque humanamente es imposible) y usamos el método IQR para eliminar "Outliers" (valores atípicos extremos). Lo más importante: **solo tuvimos que borrar 8 registros**. Nos quedó el 98.4% de la base prácticamente impecable. *(Esta fue la primera gran pista que nos adelantaba que los datos eran sintéticos y no humanos).*

---
## 1. ¿Qué modelos entrenamos y qué hace cada uno en términos simples?

* **Regresión Lineal (El modelo base):**
  * **¿Qué hace?** Intenta trazar la mejor "línea recta" posible justo por el medio de todos los datos.
  * **¿Por qué usarlo?** Es súper fácil de entender y directo. Te dice exactamente cuánto afecta cada variable (ej. "por cada kill extra, el score sube 5 puntos").

* **Regresión Ridge (El suavizador):**
  * **¿Qué hace?** Es igual a la Regresión Lineal, pero con un "freno de mano". Si hay variables que hacen mucho ruido o están muy correlacionadas entre sí y tratan de "gritar más fuerte", Ridge les baja la importancia para que el modelo no se vuelva loco aprendiéndose cosas de memoria (evita el sobreajuste).

* **Árbol de Decisión (El juego de las preguntas):**
  * **¿Qué hace?** Funciona como el juego de "¿Quién soy?". Empieza a hacer preguntas de sí/no a los datos (ej. "¿Tiene más de 10 kills?", "¿Su tiempo de reacción es menor a 200ms?") y los va dividiendo en ramas hasta llegar a un resultado final.
  * **¿Por qué no dio perfecto aquí?** Los árboles predicen haciendo "escalones" cuadrados, no pueden trazar una línea diagonal matemática perfecta, por lo que siempre tendrán un pequeño margen de error en este tipo de datasets matemáticos lineales.

* **SVM / SVR (La "Calle" Inteligente - *No usado pero evaluado*):**
  * **¿Qué hace exactamente?** En lugar de trazar solo una simple línea, SVM busca dibujar una **"calle"** (o un tubo) lo más ancha posible que atrape la mayor cantidad de datos válidos. A los puntos de datos que quedan justo tocando los bordes de esta calle se les llama **"Vectores de Soporte"**, porque son los que dictan por dónde debe pasar el camino. Además, si los datos son muy complejos y no caben en una calle recta, usa trucos matemáticos avanzados (Kernels) para "doblar" el espacio y crear calles curvas.
  * **¿Por qué no lo usamos?** Porque es matar una mosca con un cañón (sobreingeniería). Nuestra información era tan sencilla (una línea recta perfecta) que no necesitábamos toda la complejidad y el alto costo computacional del SVM. Además, el SVM funciona un poco como una "caja negra" matemática, lo que nos impediría explicarle de forma sencilla a los entrenadores cómo influye cada variable en el rendimiento.

---

## 2. Los Datos: División y Trampas

* **¿Para qué dividir en Entrenamiento (80%) y Prueba (20%)?**
  Es como en el colegio. El 80% son los ejercicios de la clase (para que el modelo aprenda los conceptos), y el 20% es el examen sorpresa (datos nuevos que nunca ha visto para comprobar si de verdad aprendió a generalizar o solo memorizó la clase).

* **¿Qué es el Target Leakage (Fuga de Datos)?**
  Es tener "las respuestas del examen" mientras estudias. Por ejemplo, intentar predecir si alguien ganará usando la variable "recibió el premio al MVP", ¡cosa que solo se sabe al finalizar el partido! En nuestra segunda revisión quitamos estas variables trampa para estar seguros.

---

## 3. Midiendo el Éxito (Métricas en fácil)

* **$R^2$ (El Porcentaje de Acierto):** Va de 0 a 1. Un 1.00 significa que el modelo entendió al 100% cómo se comportan los datos. (Por eso sospechamos que eran sintéticos, ¡nadie tiene rendimiento perfecto en la vida real!).
* **MAE (Error Promedio Simple):** Te dice de forma súper intuitiva, en promedio, por cuántos puntos te equivocaste en la predicción.
* **RMSE (El Castigador de Errores Grandes):** Igual que el MAE, pero como eleva los errores al cuadrado antes de promediarlos, penaliza y castiga mucho más si te equivocas por diferencias enormes.

---

## 4. Despliegue: Poniendo el modelo a trabajar

* **El Prototipo Interno (ipywidgets):** Unos botones deslizables en el mismo código Jupyter para jugar un rato y probar que el modelo predijera bien bajo el capó.
* **La App Final (Streamlit):** Una página web real, bonita y fácil de usar, donde alguien que no sabe programar (como un entrenador de eSports) puede ingresar datos y obtener predicciones del jugador. Para conectar ambos mundos, empaquetamos nuestro modelo matemático entrenado en un archivo (usando `joblib`) y lo cargamos directo en la web.

---

## 5. Guión Paso a Paso para la Presentación (El "Elevator Pitch")

> **Tip:** Leelo con naturalidad mientras vas mostrando la pantalla. Si el profe te frena o te pide que le muestres algo del código, usá los puntos de más arriba para responderle con seguridad.

**Vos:** "Profe, el proyecto lo estructuramos siguiendo la metodología CRISP-DM. Arrancamos entendiendo que el negocio necesitaba predecir el rendimiento para mejorar entrenamientos *(Fase 1)*. Exploramos los datos y sus correlaciones *(Fase 2)*, y en la limpieza *(Fase 3)* aplicamos filtros lógicos como un límite biológico de 120ms para el tiempo de reacción y el método IQR para valores atípicos. Pero un detalle clave: **solo tuvimos que limpiar 8 registros de toda la base**."

**Vos:** "Ya con esa data súper limpia, pasamos a la Fase de Modelado. Para no atarnos a una sola idea, pusimos a competir tres algoritmos: una Regresión Lineal clásica, una Ridge por si había mucho ruido, y un Árbol de Decisión para ver si las relaciones eran no lineales."

*(Pausa, mostrás la celda donde hacés el `fit` de los modelos)*

**Vos:** "Acá saltó algo súper interesante. Al evaluar con los datos de prueba (test), la Regresión Lineal nos arrojó un $R^2$ de 1.0000. Cero error absoluto. En el mundo real, con datos de comportamiento humano, un ajuste perfecto es estadísticamente imposible. Inmediatamente levantamos una bandera roja: ¿Estábamos sufriendo de Target Leakage? ¿Teníamos variables del futuro prediciendo el presente?"

*(Mostrás la segunda iteración o explicás la limpieza de datos)*

**Vos:** "Aplicamos el ciclo iterativo de CRISP-DM, volvimos atrás y sacamos columnas como `win_probability` y `mvp_award` por las dudas. Volvimos a entrenar... y el resultado siguió siendo perfecto. Con esto demostramos científicamente que este dataset es 100% sintético y determinista; la variable objetivo se calculó con una fórmula matemática exacta."

*(Pasás a mostrar el resultado final / Streamlit)*

**Vos:** "Al confirmar que el problema se resolvía con una línea recta perfecta, aplicar algoritmos complejos o cajas negras como SVM iba a ser pura sobreingeniería, matando moscas con cañones. Nos quedamos con la Regresión Lineal, que además nos permite explicar exactamente cómo impacta cada variable. Exportamos el pipeline con `joblib` y lo conectamos a esta interfaz interactiva en Streamlit para que un analista pueda cargar los datos y ver la predicción en tiempo real."
