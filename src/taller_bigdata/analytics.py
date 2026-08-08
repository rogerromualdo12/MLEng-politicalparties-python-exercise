"""Agregaciones analíticas sobre datasets del taller."""

from __future__ import annotations

from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def tweets_by_party(df: DataFrame) -> DataFrame:
    """Cuenta tweets por partido normalizado."""
    party_col = "party_norm" if "party_norm" in df.columns else "Party"
    return df.groupBy(party_col).count().orderBy(F.desc("count"))


def avg_words_by_party(df: DataFrame) -> DataFrame:
    """Promedio de palabras por partido."""
    return (
        df.groupBy("party_norm")
        .agg(
            F.count("*").alias("tweets"),
            F.round(F.avg("word_count"), 2).alias("avg_words"),
            F.round(F.avg("hashtag_count"), 2).alias("avg_hashtags"),
        )
        .orderBy(F.desc("tweets"))
    )


def top_hashtags(df: DataFrame, limit: int = 20) -> DataFrame:
    """Hashtags más frecuentes en el corpus."""
    return (
        df.select(F.explode("hashtags").alias("hashtag"))
        .groupBy("hashtag")
        .count()
        .orderBy(F.desc("count"))
        .limit(limit)
    )


def revenue_by_region(events: DataFrame) -> DataFrame:
    """Ingresos netos por región a partir de eventos de producto."""
    return (
        events.filter(F.col("event_type").isin("purchase", "refund"))
        .groupBy("region")
        .agg(
            F.round(F.sum("amount"), 2).alias("net_revenue"),
            F.count("*").alias("transactions"),
        )
        .orderBy(F.desc("net_revenue"))
    )


def funnel_by_channel(events: DataFrame) -> DataFrame:
    """Embudo simple por canal: views, signups y purchases."""
    return (
        events.groupBy("channel")
        .agg(
            F.sum(F.when(F.col("event_type") == "page_view", 1).otherwise(0)).alias("views"),
            F.sum(F.when(F.col("event_type") == "signup", 1).otherwise(0)).alias("signups"),
            F.sum(F.when(F.col("event_type") == "purchase", 1).otherwise(0)).alias("purchases"),
        )
        .withColumn(
            "signup_rate",
            F.when(F.col("views") > 0, F.round(F.col("signups") / F.col("views"), 4)).otherwise(0.0),
        )
        .orderBy(F.desc("purchases"))
    )