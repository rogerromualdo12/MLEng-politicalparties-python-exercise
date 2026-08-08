# Agenda del taller

Duración sugerida: **4 horas** (adaptable a 3–6 h).

## Bloque 0 — Conceptos (30 min)

- Qué es Big Data (volumen, velocidad, variedad, veracidad)
- Cuándo NO hace falta Spark
- Ecosistema: almacenamiento, procesamiento, orquestación
- Lectura: `docs/conceptos/`

## Bloque 1 — Exploración (30 min)

- Perfilar `data/raw/Tweets.csv`
- Contar filas, nulos, distribución de partidos
- Módulo: `modulos/01_exploracion`

## Bloque 2 — Pandas vs Spark (40 min)

- Misma consulta en pandas y PySpark
- Medir tiempo y memoria (cualitativo)
- Discutir trade-offs
- Módulo: `modulos/02_pandas_vs_spark`

## Bloque 3 — ETL distribuido (45 min)

- Extract / Transform / Load
- Limpieza de texto y normalización de etiquetas
- Escritura particionada en Parquet
- Módulo: `modulos/03_etl_distribuido`

## Bloque 4 — Formatos columnares (30 min)

- CSV vs Parquet
- Compresión y predicate pushdown (idea)
- Módulo: `modulos/04_formatos_columnar`

## Bloque 5 — Agregaciones (30 min)

- GroupBy, top-N hashtags, métricas por partido
- Módulo: `modulos/05_agregaciones`

## Bloque 6 — Proyecto final (45 min)

- Pipeline completo sobre eventos sintéticos
- Entregable: tabla analítica + breve lectura de resultados
- Módulo: `modulos/06_proyecto_final`

## Cierre (10 min)

- Repaso de decisiones de arquitectura
- Lecturas y siguientes pasos
