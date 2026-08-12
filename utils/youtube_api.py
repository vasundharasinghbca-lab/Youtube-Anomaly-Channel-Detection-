import re
from googleapiclient.discovery import build
from config import YOUTUBE_API_KEY

youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

def extract_handle(url):
    match = re.search(r"(?:https?://)?(?:www\.)?youtube\.com/(?:channel/|user/|c/)?([^/?]+)", url)
    if match:
        return match.group(1)
    return None

def get_channel_data(channel_url):
    handle = extract_handle(channel_url)
    if handle is None:
        return None

    request = youtube.channels().list(
        part="snippet,statistics",
        forHandle=handle
    )

    response = request.execute()

    if len(response['items']) == 0:
        return None

    channel = response['items'][0]

    snippet = channel['snippet']

    statistics = channel['statistics']

    data = {
        "title": snippet["title"],
        "description": snippet["description"],
        "publishedAt": snippet["publishedAt"],
        "viewCount": int(statistics.get("viewCount", 0)),
        "subscriberCount": int(statistics.get("subscriberCount", 0)),
        "videoCount": int(statistics.get("videoCount", 0)),
        "thumbnail": snippet["thumbnails"]["high"]["url"],
        "country": snippet.get("country", "N/A"),
        "channelUrl": f"https://www.youtube.com/channel/{channel['id']}"
       
    }

    return data
