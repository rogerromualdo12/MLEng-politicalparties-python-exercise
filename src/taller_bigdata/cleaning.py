"""Funciones de limpieza reutilizables para el caso de tweets."""

from __future__ import annotations

import re
import string

URL_RE = re.compile(r"https?://\S+|www\.\S+", flags=re.IGNORECASE)
MENTION_RE = re.compile(r"@\w+")
HASHTAG_RE = re.compile(r"#(\w+)")
WHITESPACE_RE = re.compile(r"\s+")


def remove_urls(text: str) -> str:
    """Elimina URLs de un texto."""
    return URL_RE.sub(" ", text)


def remove_mentions(text: str) -> str:
    """Elimina menciones (@usuario)."""
    return MENTION_RE.sub(" ", text)


def extract_hashtags(text: str) -> list[str]:
    """Extrae hashtags sin el símbolo #."""
    return [tag.lower() for tag in HASHTAG_RE.findall(text or "")]


def normalize_whitespace(text: str) -> str:
    """Colapsa espacios y recorta extremos."""
    return WHITESPACE_RE.sub(" ", text).strip()


def remove_punctuation(text: str) -> str:
    """Quita puntuación básica."""
    translator = str.maketrans("", "", string.punctuation)
    return text.translate(translator)


def clean_tweet(text: str | None) -> str:
    """Pipeline de limpieza estándar para un tweet.

    Orden: URLs -> menciones -> puntuación -> whitespace -> minúsculas.
    """
    if text is None:
        return ""
    value = str(text)
    value = remove_urls(value)
    value = remove_mentions(value)
    value = remove_punctuation(value)
    value = normalize_whitespace(value)
    return value.lower()


def normalize_party(party: str | None) -> str:
    """Normaliza la etiqueta de partido político."""
    if party is None:
        return "unknown"
    value = normalize_whitespace(str(party)).lower()
    if value.startswith("rep"):
        return "republican"
    if value.startswith("dem"):
        return "democrat"
    return value or "unknown"