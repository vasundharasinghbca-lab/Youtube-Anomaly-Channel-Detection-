import numpy as np
import joblib
import tensorflow as tf

from config import (
    MODEL_PATH,
    SCALER_PATH,
    THRESHOLD_PATH,
    FEATURE_PATH
)

# Load model only once
autoencoder = tf.keras.models.load_model(MODEL_PATH)

# Load scaler
scaler = joblib.load(SCALER_PATH)

# Load threshold
threshold = joblib.load(THRESHOLD_PATH)

# Load feature order
feature_columns = joblib.load(FEATURE_PATH)


def predict_channel(features_dict):

    # Arrange features in the same order used during training
    values = [features_dict[col] for col in feature_columns]

    X = np.array(values).reshape(1, -1)

    # Scale
    X_scaled = scaler.transform(X)

    # Reconstruct
    reconstructed = autoencoder.predict(X_scaled, verbose=0)

    # Reconstruction error
    error = np.mean(np.square(X_scaled - reconstructed))

    # Prediction
    prediction = "Likely Genuine"

    if error > threshold:
        prediction = "Suspicious"

    risk_score = min((error / threshold) * 100, 100)

    return {
        "prediction": prediction,
        "reconstruction_error": float(error),
        "risk_score": round(risk_score, 2)
    }