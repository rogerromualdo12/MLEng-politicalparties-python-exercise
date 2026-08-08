# ¿Qué es Big Data?

Big Data no es “muchos CSV”. Es un conjunto de problemas donde el **volumen**, la **velocidad**, la **variedad** o la **veracidad** hacen que las herramientas tradicionales se queden cortas.

## Las 4 V (versión práctica)

| V | Pregunta útil |
|---|---------------|
| Volumen | ¿Cabe cómodamente en la RAM de una máquina? |
| Velocidad | ¿Llegan datos más rápido de lo que puedo procesar por lotes? |
| Variedad | ¿Hay JSON, logs, texto, imágenes, schemas cambiantes? |
| Veracidad | ¿Hay ruido, duplicados, etiquetas dudosas? |

## Anti-patrones comunes

- Usar un cluster Spark para 50 MB “porque es Big Data”.
- Ignorar calidad de datos y solo escalar cómputo.
- Medir éxito solo por “corre en el cluster”, no por valor analítico.

## Regla del taller

Empieza simple. Escala cuando el cuello de botella sea real (memoria, tiempo, concurrencia o fuentes heterogéneas).
