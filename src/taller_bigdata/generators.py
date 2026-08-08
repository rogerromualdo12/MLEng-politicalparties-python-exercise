"""Generadores de datos sintéticos para demos de volumen."""

from __future__ import annotations

import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

REGIONS = ["norte", "sur", "este", "oeste", "centro"]
EVENTS = ["page_view", "click", "signup", "purchase", "refund"]
CHANNELS = ["web", "mobile", "partner", "email"]


def generate_events(
    rows: int,
    output_path: str | Path,
    seed: int = 42,
    start: datetime | None = None,
) -> Path:
    """Genera un CSV de eventos de producto para ejercicios de volumen.

    Args:
        rows: Número de filas a generar.
        output_path: Ruta del archivo CSV de salida.
        seed: Semilla para reproducibilidad.
        start: Fecha base de los eventos.

    Returns:
        Path del archivo generado.
    """
    if rows < 1:
        raise ValueError("rows debe ser >= 1")

    rng = random.Random(seed)
    start = start or datetime(2024, 1, 1)
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "event_id",
                "user_id",
                "event_type",
                "channel",
                "region",
                "amount",
                "event_ts",
            ],
        )
        writer.writeheader()
        for i in range(rows):
            event_type = rng.choice(EVENTS)
            amount = round(rng.uniform(5, 250), 2) if event_type in {"purchase", "refund"} else 0.0
            if event_type == "refund":
                amount = -abs(amount)
            ts = start + timedelta(minutes=rng.randint(0, 60 * 24 * 180))
            writer.writerow(
                {
                    "event_id": f"evt-{i:08d}",
                    "user_id": f"user-{rng.randint(1, max(100, rows // 20)):06d}",
                    "event_type": event_type,
                    "channel": rng.choice(CHANNELS),
                    "region": rng.choice(REGIONS),
                    "amount": amount,
                    "event_ts": ts.isoformat(timespec="seconds"),
                }
            )
    return path