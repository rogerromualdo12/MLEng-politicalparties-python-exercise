# Módulo 2 — Pandas vs Spark

## Objetivo

Ejecutar la misma agregación en pandas y PySpark y discutir diferencias.

## Tarea

1. Contar tweets por `Party` con pandas.
2. Contar tweets por `Party` con Spark.
3. Comparar resultados (deben coincidir).
4. Anotar: ¿qué cambia cuando el dataset crece 100x?

## Cómo ejecutar

```bash
source .venv/bin/activate
PYTHONPATH=src python modulos/02_pandas_vs_spark/ejercicio.py
```

## Nota

Spark arranca más lento por el JVM. En datasets pequeños pandas suele ganar; el valor de Spark aparece con volumen, paralelismo o pipelines complejos.
