#!/usr/bin/env python3
"""Demo del pipeline ETL de tweets (referencia para instructores/alumnos)."""

from __future__ import annotations

from pathlib import Path

from taller_bigdata.analytics import avg_words_by_party, tweets_by_party
from taller_bigdata.etl import run_etl
from taller_bigdata.spark_session import build_spark, stop_spark

INPUT_CSV = Path("data/raw/Tweets.csv")
OUTPUT_DIR = Path("data/processed/tweets_silver")


def main() -> None:
    if not INPUT_CSV.exists():
        raise SystemExit(f"No existe {INPUT_CSV}")

    spark = build_spark("demo-etl-tweets")
    try:
        df = run_etl(spark, INPUT_CSV, OUTPUT_DIR)
        print(f"Silver escrito en: {OUTPUT_DIR}")
        print(f"Filas limpias: {df.count()}")
        print("\nTweets por partido:")
        tweets_by_party(df).show(truncate=False)
        print("Promedios:")
        avg_words_by_party(df).show(truncate=False)
    finally:
        stop_spark(spark)


if __name__ == "__main__":
    main()