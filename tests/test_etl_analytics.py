from pathlib import Path

from taller_bigdata.analytics import funnel_by_channel, revenue_by_region, tweets_by_party
from taller_bigdata.etl import run_etl, transform_tweets
from taller_bigdata.spark_session import build_spark, stop_spark


def test_transform_and_analytics(tmp_path: Path):
    sample = tmp_path / "tweets.csv"
    sample.write_text(
        'Party,Tweet\n'
        'Republican,"Hello #Jobs https://x.com @bob"\n'
        'Democrat,"Vote now #Hope #Jobs"\n'
        'Republican,""\n',
        encoding="utf-8",
    )
    out = tmp_path / "silver"
    spark = build_spark("test-etl")
    try:
        df = run_etl(spark, sample, out)
        assert df.count() == 2
        assert out.exists()
        parties = {row["party_norm"]: row["count"] for row in tweets_by_party(df).collect()}
        assert parties["republican"] == 1
        assert parties["democrat"] == 1
    finally:
        stop_spark(spark)


def test_events_analytics():
    spark = build_spark("test-events")
    try:
        events = spark.createDataFrame(
            [
                ("web", "norte", "page_view", 0.0),
                ("web", "norte", "signup", 0.0),
                ("web", "norte", "purchase", 10.0),
                ("mobile", "sur", "purchase", 5.0),
                ("mobile", "sur", "refund", -2.0),
            ],
            ["channel", "region", "event_type", "amount"],
        )
        revenue = {r["region"]: r["net_revenue"] for r in revenue_by_region(events).collect()}
        assert revenue["norte"] == 10.0
        assert revenue["sur"] == 3.0
        funnel = {r["channel"]: r["purchases"] for r in funnel_by_channel(events).collect()}
        assert funnel["web"] == 1
        assert funnel["mobile"] == 1
    finally:
        stop_spark(spark)


def test_transform_filters_empty():
    spark = build_spark("test-transform")
    try:
        raw = spark.createDataFrame(
            [("Democrat", "!!!"), ("Republican", "Good day")],
            ["Party", "Tweet"],
        )
        clean = transform_tweets(raw)
        assert clean.count() == 1
        row = clean.collect()[0]
        assert row["party_norm"] == "republican"
        assert row["tweet_clean"] == "good day"
    finally:
        stop_spark(spark)