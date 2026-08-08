"""Solución módulo 3."""

from __future__ import annotations

from pathlib import Path

from taller_bigdata.etl import run_etl
from taller_bigdata.spark_session import build_spark, stop_spark

INPUT_CSV = Path("data/raw/Tweets.csv")
OUTPUT_DIR = Path("data/processed/tweets_silver")


def run() -> None:
    spark = build_spark("solucion-03-etl")
    try:
        df = run_etl(spark, INPUT_CSV, OUTPUT_DIR)
        print(f"Escrito en {OUTPUT_DIR}")
        print("Filas:", df.count())
        df.printSchema()
        df.show(5, truncate=40)
    finally:
        stop_spark(spark)


if __name__ == "__main__":
    run()