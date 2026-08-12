import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

MODEL_PATH = "models/autoencoder.keras"
SCALER_PATH = "models/scaler.pkl"
THRESHOLD_PATH = "models/threshold.pkl"
FEATURE_PATH = "models/feature_columns.pkl"
CONFIG_PATH = "models/config.pkl"
