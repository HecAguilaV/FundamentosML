# Reglas de Revisión - Fundamentos de Machine Learning

Este documento define las directrices y estándares que el Gentleman Guardian Angel (GGA) validará en el código del proyecto.

## 1. Estructura y Metodología (CRISP-DM)
* El proyecto debe estructurarse siguiendo las fases de la metodología CRISP-DM (o CRISP-MM).
* Debe iterar dinámicamente entre la comprensión del negocio (*Business Understanding*) y la comprensión de los datos (*Data Understanding*).

## 2. Calidad del Jupyter Notebook
* Utilizar celdas estructuradas de código y Markdown.
* Incluir títulos, subtítulos, descripciones claras e índices cuando corresponda para mantener un orden lógico y legible.

## 3. Desarrollo del Modelo de Machine Learning (Regresión)
* **Target:** El objetivo debe ser una tarea de regresión con una variable numérica continua como target.
* **Librerías:** Utilizar estrictamente `scikit-learn`, `pandas` y `numpy`.
* **División de Datos:** Dividir el dataset en conjuntos de entrenamiento (*train*) y prueba (*test*) utilizando proporciones recomendadas (ej. 80/20 o 70/30).

## 4. Entrenamiento y Comparación
* Entrenar al menos **3 alternativas** de modelos de regresión.
* Justificar la elección del algoritmo basándose en la naturaleza de los datos y el comportamiento del modelo.

## 5. Evaluación e Interpretación de Métricas
* Evaluar los modelos e interpretar correctamente al menos las siguientes métricas:
  * Coeficiente de Determinación ($R^2$)
  * Error Absoluto Medio (MAE)
  * Error Cuadrático Medio (MSE)
  * Raíz del Error Cuadrático Medio (RMSE)
* Reconocer y argumentar claramente cuál es el mejor modelo basándose en la generalización de estas métricas.

## 6. Despliegue / Interactividad
* El modelo final debe aplicarse en un entorno interactivo (como un formulario interactivo en el notebook o interfaz web/local) para permitir el ingreso de nuevos registros y mostrar predicciones en tiempo real.
