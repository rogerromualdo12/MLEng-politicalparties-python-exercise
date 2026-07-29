import os

import requests
import streamlit as st

PREDICTION_URL = os.getenv(
    "PREDICTION_URL", "http://model_inference_endpoint:8000/get-prediction/"
)


def get_prediction(input_text: str):
    """Request a prediction from the model-inference service."""
    response = requests.post(
        PREDICTION_URL,
        json={"input_texts": input_text},
        timeout=10,
    )
    response.raise_for_status()
    return response.json()["prediction"]

# Streamlit page configuration
st.set_page_config(page_title="Tweet Classifier", layout="wide")

# Streamlit UI components
st.title("Classify your tweet")

# User inputs the tweet
tweet_input = st.text_input("Enter your tweet", "")

# Button to trigger prediction
if st.button("Classify Tweet"):
    try:
        prediction = get_prediction(tweet_input)
        st.write("Prediction:", prediction)
    except requests.RequestException:
        st.error("The prediction service is unavailable. Please try again later.")
    except (KeyError, ValueError):
        st.error("The prediction service returned an invalid response.")

