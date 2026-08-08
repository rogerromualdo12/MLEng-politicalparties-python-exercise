#!/usr/bin/env python3
"""CLI para generar datasets sintéticos del taller."""

from __future__ import annotations

import argparse
from pathlib import Path

from taller_bigdata.generators import generate_events


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Genera eventos sintéticos CSV")
    parser.add_argument("--rows", type=int, default=5000, help="Número de filas")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/generated/eventos_sample.csv"),
        help="Ruta de salida",
    )
    parser.add_argument("--seed", type=int, default=42, help="Semilla RNG")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    path = generate_events(rows=args.rows, output_path=args.output, seed=args.seed)
    print(f"Generado: {path} ({args.rows} filas)")


if __name__ == "__main__":
    main()