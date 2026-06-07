# Rúbrica de Evaluación: Proyecto de Aprendizaje Automático (Regresión)

**Puntuación Máxima:** 100 puntos

| Criterio | Muy Buen Desempeño (10 pts) | Desempeño Aceptable (6 pts) | Desempeño Incipiente (3 pts) | Desempeño No Logrado (0 pts) |
| :--- | :--- | :--- | :--- | :--- |
| **1. Estructura del Proyecto** | Sigue la estructura del proyecto basándose en la metodología CRISP-DM utilizando el formato dispuesto para la evaluación. | Sigue parcialmente la estructura o tiene desvíos menores respecto al formato. | Sigue de manera deficiente la estructura de la metodología. | No sigue la estructura ni el formato dispuesto. |
| **2. Identificación de Mejoras** | Identifica las oportunidades de mejora en el proyecto, de acuerdo con el orden de las fases de la metodología, moviéndose desde *business understanding* a *data understanding* y viceversa con el fin de profundizar de mejor manera en la problemática. | Identifica mejoras pero de forma lineal, sin iterar adecuadamente entre la comprensión del negocio y de los datos. | Identifica muy pocas mejoras o sin conexión con las fases de la metodología. | No identifica oportunidades de mejora en el proyecto. |
| **3. Formato Jupyter Notebook** | Utiliza correctamente el formato de Jupyter Notebook, aprovechando cuadros de código, markdown, títulos e índices cuando corresponde. | Utiliza el notebook pero el formato es descuidado, faltan títulos, índices o explicaciones en markdown. | El uso de celdas de código y markdown es desorganizado y dificulta la lectura del flujo. | No utiliza el formato de Jupyter Notebook ni estructura alguna. |
| **4. Problema de Regresión** | Reconoce las características que tiene un problema de regresión, eligiendo un target numérico continuo para el entrenamiento del modelo de ML. | Selecciona un target continuo pero no justifica adecuadamente las características del problema de regresión. | El target elegido o la justificación del problema de regresión muestran confusión conceptual. | No reconoce las características de un problema de regresión ni elige un target continuo. |
| **5. Uso de Librerías Core** | Utiliza librerías de Scikit-Learn, pandas y numpy para el desarrollo del modelo de ML en la tarea de regresión. | Utiliza las librerías pero de forma ineficiente o con redundancias de código. | Utiliza escasamente las librerías requeridas, limitando el desarrollo del modelo. | No utiliza las librerías requeridas para el desarrollo del modelo. |
| **6. División del Dataset** | Realiza la división del dataset en algún porcentaje recomendado por las buenas prácticas de la industria para el entrenamiento y las pruebas. | Realiza la división pero los porcentajes elegidos no siguen las mejores prácticas o carece de justificación. | Realiza una división incorrecta o que compromete la validación del modelo. | No realiza la división de datos para entrenamiento y pruebas. |
| **7. Entrenamiento de Modelos** | Entrena al menos 3 alternativas de modelos de regresión seleccionando cuál es el que se adapta mejor a los datos dada la naturaleza del algoritmo implementado. | Entrena menos de 3 modelos o los entrena sin justificar la selección según la naturaleza de los algoritmos. | Entrena modelos sin lógica clara de selección ni comparación estructurada. | No entrena alternativas de modelos de regresión. |
| **8. Métricas de Evaluación** | Utiliza las métricas y las interpreta correctamente basándose en el tipo de tarea desarrollada, considerando al menos: Coeficiente de Determinación ($R^2$), MAE, MSE y RMSE. | Utiliza las métricas pero su interpretación es incompleta o confunde algunos de los conceptos evaluados. | Presenta solo algunas métricas o las interpreta de manera errónea. | No calcula ni interpreta las métricas requeridas. |
| **9. Selección del Mejor Modelo** | Logra reconocer cuál es el mejor modelo entrenado dependiendo del resultado obtenido en la generalización con las métricas correspondientes. | Identifica el mejor modelo pero la argumentación basada en las métricas de generalización es débil. | La elección del mejor modelo no coincide con los resultados de las métricas obtenidas. | No reconoce cuál es el mejor modelo ni utiliza las métricas de generalización. |
| **10. Entorno Interactivo** | Aplica el modelo predictivo desarrollado en un entorno interactivo como un formulario, permitiendo el ingreso de un nuevo registro. | Implementa el entorno interactivo pero presenta fallas de usabilidad o errores menores en el formulario. | El entorno interactivo es extremadamente rudimentario o no procesa correctamente los datos de entrada. | No aplica el modelo en ningún entorno interactivo o formulario. |

---

## Representación Estructurada (JSON) para Automatización

```json
{
  "rubrica": "Proyecto de Aprendizaje Automático (Regresión)",
  "puntuacion_maxima": 100,
  "criterios": [
    {
      "id": 1,
      "nombre": "Estructura del Proyecto",
      "descripcion": "Sigue a la estructura del proyecto basándose en la metodología CRISP-DM utilizando el formato dispuesto para la evaluación.",
      "niveles": {
        "muy_bueno": { "puntos": 10, "descripcion": "Sigue la estructura del proyecto basándose en la metodología CRISP-DM utilizando el formato dispuesto para la evaluación." },
        "aceptable": { "puntos": 6, "descripcion": "Sigue parcialmente la estructura o tiene desvíos menores respecto al formato." },
        "incipiente": { "puntos": 3, "descripcion": "Sigue de manera deficiente la estructura de la metodología." },
        "no_logrado": { "puntos": 0, "descripcion": "No sigue la estructura ni el formato dispuesto." }
      }
    },
    {
      "id": 2,
      "nombre": "Identificación de Mejoras",
      "descripcion": "Identifica las oportunidades de mejora en el proyecto, de acuerdo con el orden de las fases de la metodología, moviéndose desde business understanding a data understanding y viceversa con el fin de profundizar de mejor manera en la problemática.",
      "niveles": {
        "muy_bueno": { "puntos": 10, "descripcion": "Identifica las oportunidades de mejora en el proyecto, iterando entre business y data understanding." },
        "aceptable": { "puntos": 6, "descripcion": "Identifica mejoras de forma lineal, sin iterar adecuadamente." },
        "incipiente": { "puntos": 3, "descripcion": "Identifica muy pocas mejoras o sin conexión clara con la metodología." },
        "no_logrado": { "puntos": 0, "descripcion": "No identifica oportunidades de mejora." }
      }
    },
    {
      "id": 3,
      "nombre": "Formato Jupyter Notebook",
      "descripcion": "Utiliza correctamente el formato de Jupyter Notebook, aprovechando cuadros de código, markdown, títulos e índices cuando corresponde.",
      "niveles": {
        "muy_bueno": { "puntos": 10, "descripcion": "Aprovecha al máximo cuadros de código, markdown, títulos e índices estructurados." },
        "aceptable": { "puntos": 6, "descripcion": "Usa notebook pero el formato es descuidado o incompleto." },
        "incipiente": { "puntos": 3, "descripcion": "Formato desorganizado que dificulta seguir el flujo lógico." },
        "no_logrado": { "puntos": 0, "descripcion": "No utiliza celdas de markdown ni formato estructurado." }
      }
    },
    {
      "id": 4,
      "nombre": "Problema de Regresión",
      "descripcion": "Reconoce las características que tiene un problema de regresión, eligiendo un target numérico continuo para el entrenamiento del modelo de ML.",
      "niveles": {
        "muy_bueno": { "puntos": 10, "descripcion": "Reconoce las características del problema y selecciona un target numérico continuo." },
        "aceptable": { "puntos": 6, "descripcion": "Selecciona el target continuo pero sin justificar el tipo de problema." },
        "incipiente": { "puntos": 3, "descripcion": "Muestra confusión al definir la naturaleza de la regresión o el target." },
        "no_logrado": { "puntos": 0, "descripcion": "No identifica el target ni las características de regresión." }
      }
    },
    {
      "id": 5,
      "nombre": "Uso de Librerías Core",
      "descripcion": "Utiliza librerías de Scikit-Learn, pandas y numpy para el desarrollo del modelo de ML en la tarea de regresión.",
      "niveles": {
        "muy_bueno": { "puntos": 10, "descripcion": "Uso limpio, eficiente e integrado de Scikit-Learn, pandas y numpy." },
        "aceptable": { "puntos": 6, "descripcion": "Usa las librerías pero con código redundante o ineficiente." },
        "incipiente": { "puntos": 3, "descripcion": "Uso mínimo o limitado que dificulta el desarrollo correcto." },
        "no_logrado": { "puntos": 0, "descripcion": "No utiliza las librerías requeridas." }
      }
    },
    {
      "id": 6,
      "nombre": "División del Dataset",
      "descripcion": "Realiza la división del dataset en algún porcentaje recomendado por las buenas prácticas de la industria para el entrenamiento y las pruebas.",
      "niveles": {
        "muy_bueno": { "puntos": 10, "descripcion": "Divide el dataset aplicando porcentajes estándar y buenas prácticas." },
        "aceptable": { "puntos": 6, "descripcion": "Divide el dataset pero sin justificación clara del criterio adoptado." },
        "incipiente": { "puntos": 3, "descripcion": "División incorrecta o desproporcionada que arriesga la validación." },
        "no_logrado": { "puntos": 0, "descripcion": "No realiza división de entrenamiento y pruebas." }
      }
    },
    {
      "id": 7,
      "nombre": "Entrenamiento de Modelos",
      "descripcion": "Entrena al menos 3 alternativas de modelos de regresión seleccionando cuál es el que se adapta mejor a los datos dada la naturaleza del algoritmo implementado.",
      "niveles": {
        "muy_bueno": { "puntos": 10, "descripcion": "Entrena y compara al menos 3 modelos basándose en su naturaleza algorítmica." },
        "aceptable": { "puntos": 6, "descripcion": "Entrena menos de 3 modelos o sin evaluar su idoneidad teórica." },
        "incipiente": { "puntos": 3, "descripcion": "Entrena modelos sin un criterio claro de comparación." },
        "no_logrado": { "puntos": 0, "descripcion": "No realiza el entrenamiento de modelos." }
      }
    },
    {
      "id": 8,
      "nombre": "Métricas de Evaluación",
      "descripcion": "Utiliza las métricas y las interpreta correctamente basándose en el tipo de tarea desarrollada, considerando al menos R2, MAE, MSE y RMSE.",
      "niveles": {
        "muy_bueno": { "puntos": 10, "descripcion": "Calcula e interpreta con precisión R2, MAE, MSE y RMSE." },
        "aceptable": { "puntos": 6, "descripcion": "Presenta todas las métricas pero con fallas leves de interpretación." },
        "incipiente": { "puntos": 3, "descripcion": "Métricas incompletas o errores graves en la interpretación." },
        "no_logrado": { "puntos": 0, "descripcion": "No calcula ni interpreta ninguna métrica." }
      }
    },
    {
      "id": 9,
      "nombre": "Selección del Mejor Modelo",
      "descripcion": "Logra reconocer cuál es el mejor modelo entrenado dependiendo del resultado obtenido en la generalización con las métricas correspondientes.",
      "niveles": {
        "muy_bueno": { "puntos": 10, "descripcion": "Identifica con rigor el mejor modelo basándose en métricas de generalización." },
        "aceptable": { "puntos": 6, "descripcion": "Identifica el modelo pero con argumentación débil o incompleta." },
        "incipiente": { "puntos": 3, "descripcion": "Selección del modelo contradictoria con las métricas obtenidas." },
        "no_logrado": { "puntos": 0, "descripcion": "No identifica el mejor modelo." }
      }
    },
    {
      "id": 10,
      "nombre": "Entorno Interactivo",
      "descripcion": "Aplica el modelo predictivo desarrollado en un entorno interactivo como un formulario, permitiendo el ingreso de un nuevo registro.",
      "niveles": {
        "muy_bueno": { "puntos": 10, "descripcion": "Formulario funcional y amigable que realiza predicciones correctamente." },
        "aceptable": { "puntos": 6, "descripcion": "Entorno interactivo funcional pero con errores menores de usabilidad." },
        "incipiente": { "puntos": 3, "descripcion": "Interfaz extremadamente básica o con fallas críticas de integración." },
        "no_logrado": { "puntos": 0, "descripcion": "No implementa entorno interactivo." }
      }
    }
  ]
}
```
