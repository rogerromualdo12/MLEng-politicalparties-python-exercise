from taller_bigdata.cleaning import (
    clean_tweet,
    extract_hashtags,
    normalize_party,
    remove_urls,
)


def test_remove_urls():
    text = "Mira esto https://example.com ahora"
    assert "https" not in remove_urls(text)


def test_extract_hashtags():
    assert extract_hashtags("Hola #Data #BigData") == ["data", "bigdata"]


def test_clean_tweet_basic():
    raw = "Hello @user!!! Visit https://x.com #AI"
    cleaned = clean_tweet(raw)
    assert "@" not in cleaned
    assert "https" not in cleaned
    assert cleaned == "hello visit ai"


def test_normalize_party():
    assert normalize_party("Republican") == "republican"
    assert normalize_party("Democrat") == "democrat"
    assert normalize_party(None) == "unknown"