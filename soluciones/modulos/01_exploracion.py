"""Solución módulo 1."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

DATA_PATH = Path("data/raw/Tweets.csv")


def load_raw(path: Path = DATA_PATH) -> pd.DataFrame:
    return pd.read_csv(path)


def party_distribution(df: pd.DataFrame) -> pd.Series:
    return df["Party"].value_counts(dropna=False)


def null_report(df: pd.DataFrame) -> pd.Series:
    return df.isna().sum()


def avg_tweet_length(df: pd.DataFrame) -> float:
    return df["Tweet"].astype(str).str.len().mean()


def main() -> None:
    df = load_raw()
    print("Filas:", len(df))
    print("Columnas:", list(df.columns))
    print("\nDistribución Party:\n", party_distribution(df))
    print("\nNulos:\n", null_report(df))
    print("\nLongitud media tweet:", round(avg_tweet_length(df), 2))


if __name__ == "__main__":
    main()