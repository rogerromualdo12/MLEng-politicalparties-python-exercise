"""Solución módulo 2."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from taller_bigdata.spark_session import build_spark, stop_spark

DATA_PATH = Path("data/raw/Tweets.csv")


def count_by_party_pandas(path: Path = DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(path)
    out = df.groupby("Party", dropna=False).size().reset_index(name="count")
    return out.sort_values("Party").reset_index(drop=True)


def count_by_party_spark(path: Path = DATA_PATH) -> pd.DataFrame:
    spark = build_spark("solucion-02")
    try:
        sdf = (
            spark.read.option("header", True)
            .option("multiLine", True)
            .option("escape", '"')
            .csv(str(path))
        )
        return (
            sdf.groupBy("Party")
            .count()
            .orderBy("Party")
            .toPandas()
            .rename(columns={"count": "count"})
        )
    finally:
        stop_spark(spark)


def main() -> None:
    pdf = count_by_party_pandas()
    sdf = count_by_party_spark()
    print("Pandas:\n", pdf)
    print("\nSpark:\n", sdf)
    print("\n¿Coinciden?", pdf.equals(sdf))


if __name__ == "__main__":
    main()