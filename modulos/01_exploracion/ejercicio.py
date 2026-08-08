"""Módulo 1: exploración del dataset de tweets con pandas."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

DATA_PATH = Path("data/raw/Tweets.csv")


def load_raw(path: Path = DATA_PATH) -> pd.DataFrame:
    """Carga el CSV crudo."""
    # TODO: leer el CSV con pandas (header en la primera fila)
    raise NotImplementedError("Completa load_raw")


def party_distribution(df: pd.DataFrame) -> pd.Series:
    """Devuelve conteo de tweets por partido."""
    # TODO: value_counts de la columna Party
    raise NotImplementedError("Completa party_distribution")


def null_report(df: pd.DataFrame) -> pd.Series:
    """Cuenta nulos por columna."""
    # TODO: isna().sum()
    raise NotImplementedError("Completa null_report")


def avg_tweet_length(df: pd.DataFrame) -> float:
    """Longitud media en caracteres de la columna Tweet."""
    # TODO: convertir a str y calcular mean de .str.len()
    raise NotImplementedError("Completa avg_tweet_length")


def main() -> None:
    df = load_raw()
    print("Filas:", len(df))
    print("Columnas:", list(df.columns))
    print("\nDistribución Party:\n", party_distribution(df))
    print("\nNulos:\n", null_report(df))
    print("\nLongitud media tweet:", round(avg_tweet_length(df), 2))


if __name__ == "__main__":
    main()