# Guía del instructor

## Perfil de audiencia

- Conocimientos previos: Python básico y SQL/pandas deseable
- No se asume experiencia previa en Spark
- Ideal: 8–20 personas

## Preparación previa (1 día antes)

1. Clonar el repo y correr `make install && make test`.
2. Verificar Java (`java -version`) y que PySpark arranca.
3. Revisar `soluciones/` sin proyectarlas al inicio.
4. Generar dataset grande si habrá demo de volumen: `make generate-large`.

## Ritmo sugerido

- Alterna 5–10 min de teoría con 15–25 min de práctica.
- Usa el caso de tweets para narrativa; usa eventos sintéticos para volumen.
- Si alguien se atrasa, ofrece pistas del README del módulo (no la solución completa).

## Puntos de discusión clave

1. **¿Cuándo Big Data?** Si cabe en memoria y el SLA lo permite, pandas/DuckDB pueden bastar.
2. **Costo de distributed systems**: serialización, shuffle, complejidad operativa.
3. **Schema y calidad**: tweets multilínea, nulos, etiquetas inconsistentes.
4. **Formato**: Parquet brilla en lecturas analíticas parciales; CSV sigue siendo buen interchange.

## Evaluación rápida (opcional)

Pedir al final:

- Diagrama del pipeline ETL (3 cajas)
- Una métrica calculada en Spark
- Una justificación de CSV vs Parquet para su caso

## Soluciones

Las referencias viven en `soluciones/modulos/`. Úsalas para destrabar o cerrar cada bloque.
