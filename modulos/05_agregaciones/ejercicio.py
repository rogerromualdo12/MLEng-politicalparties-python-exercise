"""Módulo 5: agregaciones sobre tweets limpios."""

from __future__ import annotations

from pathlib import Path

from taller_bigdata.spark_session import build_spark, stop_spark

SILVER = Path("data/processed/tweets_silver")
RAW = Path("data/raw/Tweets.csv")


def main() -> None:
    spark = build_spark("modulo-05-agg")
    try:
        # TODO:
        # 1) Leer silver si existe; si no, ETL al vuelo desde RAW
        # 2) Usar analytics.tweets_by_party / avg_words_by_party / top_hashtags
        # 3) Mostrar resultados con .show()
        raise NotImplementedError("Completa las agregaciones del módulo 5")
    finally:
        stop_spark(spark)


if __name__ == "__main__":
    main()