"""Solución módulo 6."""

from __future__ import annotations

from pathlib import Path

from pyspark.sql import functions as F

from taller_bigdata.analytics import funnel_by_channel, revenue_by_region
from taller_bigdata.spark_session import build_spark, stop_spark

BRONZE = Path("data/generated/eventos_sample.csv")
SILVER_DIR = Path("data/processed/events_silver")
GOLD_DIR = Path("data/processed/events_gold")


def main() -> None:
    if not BRONZE.exists():
        raise SystemExit("Ejecuta primero: make generate-sample")

    spark = build_spark("solucion-06-proyecto")
    try:
        bronze = (
            spark.read.option("header", True)
            .option("inferSchema", True)
            .csv(str(BRONZE))
        )
        silver = (
            bronze.withColumn("amount", F.col("amount").cast("double"))
            .withColumn("event_ts", F.to_timestamp("event_ts"))
            .withColumn("event_date", F.to_date("event_ts"))
        )
        silver.write.mode("overwrite").partitionBy("event_date").parquet(str(SILVER_DIR))

        revenue = revenue_by_region(silver)
        funnel = funnel_by_channel(silver)

        revenue.write.mode("overwrite").parquet(str(GOLD_DIR / "revenue_by_region"))
        funnel.write.mode("overwrite").parquet(str(GOLD_DIR / "funnel_by_channel"))

        print("Silver:", SILVER_DIR)
        print("Gold:", GOLD_DIR)
        print("\nIngresos por región:")
        revenue.show(truncate=False)
        print("Embudo por canal:")
        funnel.show(truncate=False)
    finally:
        stop_spark(spark)


if __name__ == "__main__":
    main()