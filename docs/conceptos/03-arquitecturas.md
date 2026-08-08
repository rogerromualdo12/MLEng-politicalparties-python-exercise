# Arquitecturas útiles para el taller

## Batch ETL clásico

```text
raw/ --> transform --> processed/ (Parquet particionado) --> agregaciones
```

Ventaja: simple, auditable, fácil de reejecutar.

## Lakehouse ligero (idea)

```text
bronze (raw) --> silver (limpio) --> gold (métricas de negocio)
```

En el proyecto final modelamos esta idea con carpetas:

- `data/raw` o `data/generated` = bronze
- `data/processed` = silver
- agregaciones en memoria o parquet gold

## Decisiones que pediremos justificar

1. ¿Particionar por qué columna?
2. ¿Qué columnas materializar en silver?
3. ¿Qué métricas merecen una tabla gold?
