from datetime import datetime, timezone
import numpy as np

def create_features(channel_data):

    today = datetime.now(timezone.utc)

    # Parse published date (works with and without fractional seconds)
    published_at = channel_data["publishedAt"].replace("Z", "+00:00")
    created = datetime.fromisoformat(published_at)

    # Calculate channel age
    channel_age = (today - created).days / 365.25

    # Raw values
    subscribers = max(channel_data["subscriberCount"], 1)
    videos = max(channel_data["videoCount"], 1)
    views = channel_data["viewCount"]

    # ==========================
    # Display Metrics
    # ==========================
    display_metrics = {

        "channel_age": round(channel_age, 1),

        "views_per_subscriber": round(views / subscribers, 2),

        "views_per_video": round(views / videos, 2),

        "video_per_year": round(videos / max(channel_age, 1), 2)

    }

    # ==========================
    # AI Features
    # ==========================
    features = {

        "views_per_subscriber": np.log1p(views / subscribers),

        "views_per_video": np.log1p(views / videos),

        "view_count": np.log1p(views),

        "subscriber_count": np.log1p(subscribers),

        "video_per_year": np.log1p(videos / max(channel_age, 1)),

        "video_count": np.log1p(videos),

        "channel_age": channel_age

    }

    return features, display_metrics