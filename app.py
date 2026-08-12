

from flask import Flask, render_template, request, session
from config import SECRET_KEY

from utils.youtube_api import get_channel_data
from utils.feature_engineering import create_features
from utils.predictor import predict_channel

app = Flask(__name__)
app.secret_key = SECRET_KEY


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    channel_url = request.form["channel_url"]

    # Get YouTube channel information
    channel = get_channel_data(channel_url)

    if channel is None:
        return "Invalid YouTube channel URL or channel not found."

    # Create AI features
    features, display_metrics = create_features(channel)

    # Predict
    result = predict_channel(features)

    session["channel"] = channel
    session["result"] = result
    session["display_metrics"] = display_metrics

    # Send everything to result page
    return render_template(
        "result.html",
        channel=channel,
        result=result,
        features=features,
        display_metrics=display_metrics
    )

@app.route("/dashboard")
def dashboard():

    channel = session.get("channel")
    result = session.get("result")
    display_metrics = session.get("display_metrics")

    if not channel or not result:
        return "Please analyze a channel first."

    return render_template(
        "dashboard.html",
        channel=channel,
        result=result,
        display_metrics=display_metrics
    )

    


if __name__ == "__main__":
    app.run(debug=True)