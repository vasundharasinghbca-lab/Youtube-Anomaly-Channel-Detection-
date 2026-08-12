from utils.youtube_api import get_channel_data

url = "https://www.youtube.com/@HauntingTube"

channel = get_channel_data(url)

print(channel)