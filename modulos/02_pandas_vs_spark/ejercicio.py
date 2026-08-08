"""Módulo 2: misma agregación en pandas y Spark."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from taller_bigdata.spark_session import build_spark, stop_spark

DATA_PATH = Path("data/raw/Tweets.csv")


def count_by_party_pandas(path: Path = DATA_PATH) -> pd.DataFrame:
    """Agregación con pandas."""
    # TODO: read_csv + groupby('Party').size() como DataFrame con columnas Party, count
    raise NotImplementedError("Completa count_by_party_pandas")


def count_by_party_spark(path: Path = DATA_PATH) -> pd.DataFrame:
    """Agregación con Spark y retorno a pandas para comparar."""
    spark = build_spark("modulo-02")
    try:
        # TODO:
        # 1) leer CSV con header/multiLine/escape
        # 2) groupBy('Party').count()
        # 3) orderBy Party y toPandas()
        raise NotImplementedError("Completa count_by_party_spark")
    finally:
        stop_spark(spark)


def main() -> None:
    pdf = count_by_party_pandas().sort_values("Party").reset_index(drop=True)
    sdf = count_by_party_spark().sort_values("Party").reset_index(drop=True)
    print("Pandas:\n", pdf)
    print("\nSpark:\n", sdf)
    print("\n¿Coinciden?", pdf.equals(sdf))


if __name__ == "__main__":
    main()