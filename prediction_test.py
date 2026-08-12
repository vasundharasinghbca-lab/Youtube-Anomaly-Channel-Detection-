from utils.youtube_api import get_channel_data
from utils.feature_engineering import create_features
from utils.predictor import predict_channel

url = input("Paste YouTube URL: ")

channel = get_channel_data(url)

features = create_features(channel)

result = predict_channel(features)

print(result)