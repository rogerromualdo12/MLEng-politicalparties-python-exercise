"""Train and save the tweet-classification model consumed by the API."""

from pathlib import Path

import mlflow.sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from text_loader.loader import DataLoader


MODEL_PATH = Path("data/models")


def train_model() -> None:
    """Fit a text-classification pipeline and save it as an MLflow model."""
    loader = DataLoader()
    tweets = loader.data["Tweet"].map(loader.clean_text)
    parties = loader.data["Party"].map(loader.clean_text)

    model = Pipeline(
        [
            ("vectorizer", TfidfVectorizer(max_features=2500, min_df=1, max_df=0.8)),
            ("classifier", LogisticRegression(max_iter=1000)),
        ]
    )
    model.fit(tweets, parties)
    mlflow.sklearn.save_model(model, str(MODEL_PATH))


if __name__ == "__main__":
    train_model()
