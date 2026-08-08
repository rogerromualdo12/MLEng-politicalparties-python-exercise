"""Solución módulo 4."""

from __future__ import annotations

import time
from pathlib import Path

from taller_bigdata.spark_session import build_spark, stop_spark

CSV_PATH = Path("data/generated/eventos_sample.csv")
PARQUET_PATH = Path("data/processed/eventos_sample.parquet")


def file_size_mb(path: Path) -> float:
    if path.is_file():
        return path.stat().st_size / (1024 * 1024)
    return sum(p.stat().st_size for p in path.rglob("*") if p.is_file()) / (1024 * 1024)


def main() -> None:
    if not CSV_PATH.exists():
        raise SystemExit("Ejecuta primero: make generate-sample")

    spark = build_spark("solucion-04-formatos")
    try:
        df = (
            spark.read.option("header", True)
            .option("inferSchema", True)
            .csv(str(CSV_PATH))
        )
        df.write.mode("overwrite").parquet(str(PARQUET_PATH))

        print(f"CSV MB: {file_size_mb(CSV_PATH):.3f}")
        print(f"Parquet MB: {file_size_mb(PARQUET_PATH):.3f}")

        t0 = time.perf_counter()
        (
            spark.read.option("header", True)
            .option("inferSchema", True)
            .csv(str(CSV_PATH))
            .select("region", "amount")
            .count()
        )
        csv_s = time.perf_counter() - t0

        t1 = time.perf_counter()
        spark.read.parquet(str(PARQUET_PATH)).select("region", "amount").count()
        parquet_s = time.perf_counter() - t1

        print(f"Lectura proyectada CSV: {csv_s:.3f}s")
        print(f"Lectura proyectada Parquet: {parquet_s:.3f}s")
    finally:
        stop_spark(spark)


if __name__ == "__main__":
    main()