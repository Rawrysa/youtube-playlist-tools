import requests
from dotenv import load_dotenv
import os

class YouTubeAPI:

    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("YOUTUBE_API_KEY")
        self.api_url = os.getenv("YOUTUBE_API_URL")

    def get_playlist_items(self, playlist_id):

        playlist_items_urls: list[str] = []

        params = {
            "key": self.api_key,
            "part": "contentDetails",
            "playlistId": playlist_id,
            "maxResults": 50
        }
        response = requests.get(self.api_url, params=params)

        if response.status_code == 200:

            playlist_items = response.json().get("items", [])

            if not playlist_items:
                return {"error": "No items found"}

            for item in playlist_items:
                video_id = item["contentDetails"]["videoId"]
                video_url = self.get_video_url(video_id)
                playlist_items_urls.append(video_url)

            next_page_token = response.json().get("nextPageToken")

            while next_page_token:
                # Fetch the next page of results
                params["pageToken"] = next_page_token
                response = requests.get(self.api_url, params=params)

                if response.status_code == 200:
                    next_playlist_items = response.json().get("items", [])
                    for item in next_playlist_items:
                        video_id = item["contentDetails"]["videoId"]
                        video_url = self.get_video_url(video_id)
                        playlist_items_urls.append(video_url)

                next_page_token = response.json().get("nextPageToken")

            return playlist_items_urls
        else:
            return {"error": response.text}

    def get_video_url(self, video_id):
        youtube_video_url = f"https://www.youtube.com/watch?v={video_id}"
        return youtube_video_url