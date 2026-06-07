# Bitácora de Decisiones Técnicas - Proyecto eSports

###### Héctor Aguila

###### Metodología: CRISP-DM

Este documento registro el "porqué" de cada paso que di en el Análisis Exploratorio de Datos (EDA), basándome en la materia y en mi propio crciterio según lo experimentado el semestre anterior.

---

## 1. Fase: Comprensión del Negocio

### 1.1. Qué  busqué

Al revisar el dataset, me queda claro que hay dos caminos potentes para generar valor:

- **Predecir el rendimiento**: Usar regresión para entender qué variables disparan el `performance_score`.
- **Detectar talento**: Usar clasificación para ver quién tiene perfil de MVP.

### 1.2. Sobre el Dataset

Asumo que al ser el dataset oficial con el que vamos a trabajar durante el semestre, la estructura es fija. Sin embargo, para que un modelo de este tipo sea realmente útil en la vida real, considero que debería ser complementado con los siguientes features:

- **Latencia (Ping)**: En eSports, el lag decide partidas. Sin esto, el análisis está incompleto.
- **Hardware y Periféricos**: No es lo mismo jugar a 60Hz que a 240Hz.
- **Carga de entrenamiento**: Para entender si la fatiga es por exceso de horas o por la intensidad del torneo.

Menciono esto, entendiendo medianamente el contexto competitivo, donde estos datos marcan  la diferencia.

---

## 2. Fase: Comprensión de los Datos

### 2.1. Clasificación de Variables

Primero separé las variables (Nominal, Ordinal, Continuo, Discreto). Esto me permitió decidir, que los Roles no tienen un orden (Nominal) pero las instancias del torneo sí (Ordinal).

### 2.2. El problema del match_outcome

Acá encontré un "ruido" importante: casi el 100% de los registros son victorias.

- Descarté esta variable para entrenar modelos de clasificación. Si el modelo solo ve victorias, va a aprender que "siempre se gana", y eso no sirve para predecir nada realmente.

---

## 3. Fase: Preparación de Datos

### 3.1. Limpieza de Outliers: El límite humano

Para la limpieza, según investigación, fundamenté mi decisión en: "el límitie humano", según la **IAAF (World Athletics)**

- **Filtro de 120ms**: Borré cualquier registro con un tiempo de respuesta menor a eso. Porque según la neurofisiología, un humano no puede reaccionar tan rápido. Esos datos son errores de captura o ruido, y si los dejo, el modelo se "rompe".
- **IQR**: Para el resto de los valores extremos (los que son muy lentos), use la limpieza de las colas para quedarme con el corazón de los datos.

### 3.2. Selección de Características

Saqué el `player_id` ya que lo consideré un dato administrativo que solo genera ruido. El modelo tiene que aprender a reconocer un buen jugador por su precisión y sus kills, no por su número de documento. Entonces, el modelo debe aprender **qué hacen** los jugadores, no **cómo se llaman**.

### 3.3. Transformaciones: Estandarización

Para estandarizar usé `StandardScaler`. Porque hay variables en milisegundos y otras en unidades de kills. Sin estandarizar, el modelo le daría más importancia a los números grandes solo por sesgo.

---

## 4. Conclusión

Al completar el EDA, me quedo con el reforzamiento de conceptos anteriores y una frase que leí/escuché: "Un dataset no se acepta, se cuestiona". El dataset en cuestión, pasó de un archivo crudo a una tabla de datos estadísticos estandarizada.
