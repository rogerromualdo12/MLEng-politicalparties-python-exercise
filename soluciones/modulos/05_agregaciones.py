"""Solución módulo 5."""

from __future__ import annotations

from pathlib import Path

from taller_bigdata.analytics import avg_words_by_party, top_hashtags, tweets_by_party
from taller_bigdata.etl import run_etl
from taller_bigdata.spark_session import build_spark, stop_spark

SILVER = Path("data/processed/tweets_silver")
RAW = Path("data/raw/Tweets.csv")


def main() -> None:
    spark = build_spark("solucion-05-agg")
    try:
        if SILVER.exists():
            df = spark.read.parquet(str(SILVER))
        else:
            df = run_etl(spark, RAW, SILVER)

        print("Tweets por partido:")
        tweets_by_party(df).show(truncate=False)
        print("Promedios:")
        avg_words_by_party(df).show(truncate=False)
        print("Top hashtags:")
        top_hashtags(df, limit=15).show(truncate=False)
    finally:
        stop_spark(spark)


if __name__ == "__main__":
    main()