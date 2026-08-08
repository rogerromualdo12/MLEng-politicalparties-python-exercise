# Módulo 6 — Proyecto final

## Objetivo

Construir un mini lakehouse batch sobre eventos de producto sintéticos.

## Historia

Una app genera eventos (`page_view`, `click`, `signup`, `purchase`, `refund`).
Tu equipo debe producir:

1. **Bronze**: CSV generado (`data/generated/eventos_sample.csv` o large)
2. **Silver**: Parquet limpio con tipos correctos y columna `event_date`
3. **Gold**:
   - ingresos netos por región
   - embudo por canal (views → signups → purchases)

## Criterios de aceptación

- El script corre de punta a punta sin errores
- Imprime las dos tablas gold
- Escribe silver en `data/processed/events_silver`
- Escribe gold en `data/processed/events_gold/`

## Cómo ejecutar

```bash
make generate-sample
source .venv/bin/activate
PYTHONPATH=src python modulos/06_proyecto_final/ejercicio.py
```
