import os
from functools import lru_cache

from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
import mlflow.pyfunc

from text_loader.loader import DataLoader

mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI", "data"))
MODEL_URI = os.getenv("MODEL_URI", "data/models")

class InputText(BaseModel):
    input_texts: str


@lru_cache
def load_model():
    """Load and cache the MLflow model for the lifetime of the API process."""
    try:
        return mlflow.pyfunc.load_model(MODEL_URI)
    except Exception as error:
        raise RuntimeError(
            f"Unable to load MLflow model from {MODEL_URI!r}. "
            "Set MODEL_URI to a valid MLflow model URI."
        ) from error


app = FastAPI()

@app.get("/health")
def get_health():
    return {"status": "OK"}


@app.post("/get-prediction/")
def get_prediction(input_data: InputText):
    """Return the pre-trained model's prediction for one tweet."""
    text = input_data.input_texts.strip()
    if not text:
        raise HTTPException(status_code=422, detail="input_texts must not be empty")

    try:
        prediction = load_model().predict([DataLoader.clean_text(text)])
    except RuntimeError as error:
        raise HTTPException(status_code=503, detail=str(error)) from error
    except Exception as error:
        raise HTTPException(status_code=500, detail="Model prediction failed") from error

    if hasattr(prediction, "tolist"):
        prediction = prediction.tolist()
    return {"prediction": prediction}