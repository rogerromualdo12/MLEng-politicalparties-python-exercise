# Módulo 3 — ETL distribuido

## Objetivo

Construir un pipeline Extract → Transform → Load sobre tweets.

## Transformaciones pedidas

- Normalizar `Party` → `party_norm`
- Limpiar texto → `tweet_clean`
- Extraer `hashtags`, `word_count`, `hashtag_count`
- Filtrar tweets vacíos tras limpieza
- Escribir Parquet particionado por `party_norm`

## Pista

La biblioteca `taller_bigdata.etl` ya tiene helpers. Puedes reutilizarlos o reimplementar para practicar.

## Cómo ejecutar

```bash
source .venv/bin/activate
PYTHONPATH=src python modulos/03_etl_distribuido/ejercicio.py
```

Salida esperada: `data/processed/tweets_silver/`
