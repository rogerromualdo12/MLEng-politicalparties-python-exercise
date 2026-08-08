# Ecosistema Big Data (mapa mental)

## Capas típicas

1. **Ingesta**: archivos, APIs, colas (Kafka), CDC
2. **Almacenamiento**: object storage (S3/GCS), HDFS, lakehouse
3. **Procesamiento**: Spark, Flink, motores SQL (Trino, DuckDB)
4. **Orquestación**: Airflow, Dagster, Prefect
5. **Consumo**: BI, features ML, APIs, alertas

## En este taller usamos

- **Python + pandas**: baseline local
- **PySpark**: procesamiento distribuido (modo `local[*]`)
- **CSV / Parquet**: formatos de intercambio y analíticos
- **Makefile**: reproducibilidad del entorno

## Spark en una frase

Spark reparte el trabajo en particiones, ejecuta transformaciones perezosas y materializa acciones (`count`, `write`, `collect`).
