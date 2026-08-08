from pathlib import Path

import pandas as pd

from taller_bigdata.generators import generate_events


def test_generate_events(tmp_path: Path):
    out = tmp_path / "events.csv"
    path = generate_events(rows=100, output_path=out, seed=1)
    df = pd.read_csv(path)
    assert len(df) == 100
    assert set(["event_id", "user_id", "event_type", "amount", "event_ts"]).issubset(df.columns)
    assert df["event_type"].isin(["page_view", "click", "signup", "purchase", "refund"]).all()


def test_generate_events_rejects_zero(tmp_path: Path):
    try:
        generate_events(rows=0, output_path=tmp_path / "x.csv")
        assert False, "debía fallar"
    except ValueError:
        pass