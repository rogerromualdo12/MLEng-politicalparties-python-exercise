"""Módulo 3: pipeline ETL con PySpark."""

from __future__ import annotations

from pathlib import Path

from taller_bigdata.spark_session import build_spark, stop_spark

INPUT_CSV = Path("data/raw/Tweets.csv")
OUTPUT_DIR = Path("data/processed/tweets_silver")


def run() -> None:
    spark = build_spark("modulo-03-etl")
    try:
        # TODO:
        # 1) Cargar tweets (load_tweets o spark.read...)
        # 2) Transformar (transform_tweets)
        # 3) Escribir parquet particionado
        # 4) Imprimir conteo final y schema
        raise NotImplementedError("Completa el ETL del módulo 3")
    finally:
        stop_spark(spark)


if __name__ == "__main__":
    run()