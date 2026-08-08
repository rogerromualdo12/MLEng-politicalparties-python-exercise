"""Utilidades para crear sesiones Spark locales del taller."""

from __future__ import annotations

from pyspark.sql import SparkSession


def build_spark(app_name: str = "taller-big-data", shuffle_partitions: int = 8) -> SparkSession:
    """Crea una SparkSession en modo local apta para el taller.

    Args:
        app_name: Nombre de la aplicación Spark.
        shuffle_partitions: Particiones de shuffle (bajo para demos locales).

    Returns:
        SparkSession configurada.
    """
    return (
        SparkSession.builder.appName(app_name)
        .master("local[*]")
        .config("spark.sql.shuffle.partitions", str(shuffle_partitions))
        .config("spark.driver.memory", "2g")
        .config("spark.ui.showConsoleProgress", "false")
        .getOrCreate()
    )


def stop_spark(spark: SparkSession | None) -> None:
    """Detiene la sesión Spark de forma segura."""
    if spark is not None:
        spark.stop()