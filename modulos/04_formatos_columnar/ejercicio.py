"""Módulo 4: CSV vs Parquet."""

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

    spark = build_spark("modulo-04-formatos")
    try:
        # TODO:
        # 1) leer CSV
        # 2) escribir Parquet en PARQUET_PATH
        # 3) medir tamaños
        # 4) cronometrar lectura proyectando region, amount desde CSV y Parquet
        raise NotImplementedError("Completa la comparación CSV vs Parquet")
    finally:
        stop_spark(spark)


if __name__ == "__main__":
    main()