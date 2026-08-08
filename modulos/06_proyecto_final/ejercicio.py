"""Módulo 6: proyecto final — mini lakehouse de eventos."""

from __future__ import annotations

from pathlib import Path

from taller_bigdata.spark_session import build_spark, stop_spark

BRONZE = Path("data/generated/eventos_sample.csv")
SILVER_DIR = Path("data/processed/events_silver")
GOLD_DIR = Path("data/processed/events_gold")


def main() -> None:
    if not BRONZE.exists():
        raise SystemExit("Ejecuta primero: make generate-sample")

    spark = build_spark("modulo-06-proyecto")
    try:
        # TODO:
        # 1) Leer bronze CSV
        # 2) Tipar amount (double), event_ts (timestamp), derivar event_date
        # 3) Escribir silver parquet
        # 4) Calcular revenue_by_region y funnel_by_channel
        # 5) Escribir ambas tablas gold y mostrarlas
        raise NotImplementedError("Completa el proyecto final")
    finally:
        stop_spark(spark)


if __name__ == "__main__":
    main()