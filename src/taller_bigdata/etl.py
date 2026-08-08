"""Pipeline ETL con PySpark para el caso de tweets."""

from __future__ import annotations

from pathlib import Path

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import ArrayType, StringType

from taller_bigdata.cleaning import clean_tweet, extract_hashtags, normalize_party


def load_tweets(spark: SparkSession, path: str | Path) -> DataFrame:
    """Carga el CSV de tweets como DataFrame Spark."""
    return (
        spark.read.option("header", True)
        .option("multiLine", True)
        .option("escape", '"')
        .csv(str(path))
    )


def transform_tweets(df: DataFrame) -> DataFrame:
    """Aplica limpieza, normalización y features derivadas."""
    clean_udf = F.udf(clean_tweet, StringType())
    party_udf = F.udf(normalize_party, StringType())
    hashtags_udf = F.udf(extract_hashtags, ArrayType(StringType()))

    return (
        df.withColumn("party_norm", party_udf(F.col("Party")))
        .withColumn("tweet_clean", clean_udf(F.col("Tweet")))
        .withColumn("hashtags", hashtags_udf(F.col("Tweet")))
        .withColumn("word_count", F.size(F.split(F.col("tweet_clean"), " ")))
        .withColumn("hashtag_count", F.size(F.col("hashtags")))
        .filter(F.length(F.col("tweet_clean")) > 0)
        .select(
            "party_norm",
            "tweet_clean",
            "hashtags",
            "word_count",
            "hashtag_count",
        )
    )


def write_parquet(df: DataFrame, output_dir: str | Path, partition_by: str | None = "party_norm") -> Path:
    """Persiste un DataFrame en Parquet, opcionalmente particionado."""
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    writer = df.write.mode("overwrite")
    if partition_by:
        writer = writer.partitionBy(partition_by)
    writer.parquet(str(out))
    return out


def run_etl(spark: SparkSession, input_csv: str | Path, output_dir: str | Path) -> DataFrame:
    """Ejecuta extract -> transform -> load completo."""
    raw = load_tweets(spark, input_csv)
    clean = transform_tweets(raw)
    write_parquet(clean, output_dir)
    return clean