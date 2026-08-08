# Módulo 4 — Formatos columnares

## Objetivo

Comparar CSV y Parquet en tamaño y tiempo de lectura de un subconjunto de columnas.

## Tareas

1. Generar o usar un dataset de eventos (`make generate-sample`).
2. Guardar una copia en Parquet.
3. Medir tamaño en disco.
4. Leer solo columnas `region` y `amount` desde ambos formatos y comparar tiempos.

## Conceptos

- Parquet almacena por columnas → lee menos bytes si proyectas columnas.
- Compresión suele reducir I/O.
- CSV sigue siendo útil para intercambio humano/simple.

## Cómo ejecutar

```bash
make generate-sample
source .venv/bin/activate
PYTHONPATH=src python modulos/04_formatos_columnar/ejercicio.py
```
