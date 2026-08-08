# Módulo 5 — Agregaciones analíticas

## Objetivo

Calcular métricas de negocio/texto sobre el dataset limpio.

## Métricas pedidas

1. Tweets por partido
2. Promedio de palabras y hashtags por partido
3. Top 15 hashtags globales

## Prerrequisito

Idealmente corre el módulo 3 (o `make demo-etl`) para tener `data/processed/tweets_silver`.

Si no existe, el ejercicio puede leer el CSV crudo y transformar al vuelo.

## Cómo ejecutar

```bash
source .venv/bin/activate
PYTHONPATH=src python modulos/05_agregaciones/ejercicio.py
```
