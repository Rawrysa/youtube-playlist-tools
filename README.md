# YouTube Playlist Tools

Small Python utilities for working with YouTube playlists:

- **`scripts/youtube_api.py`**: `YouTubeAPI.get_playlist_items(playlist_id)` calls the YouTube Data API v3 `playlistItems` endpoint. It follows `nextPageToken` until it has every page, then returns the watch URL of each video in the playlist.
- **`scripts/youtube_downloader.py`**: downloads a single video, or every video in a playlist, at the highest available resolution using `pytube`.
- **`notebooks/youtube_api.ipynb`**: the same API client, for interactive experimentation.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate          # macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env            # then add your API key
```

Get an API key from the [Google Cloud console](https://console.cloud.google.com/apis/library/youtube.googleapis.com) with the YouTube Data API v3 enabled.

## Usage

From the `scripts/` folder:

```python
from youtube_api import YouTubeAPI

urls = YouTubeAPI().get_playlist_items("PLxxxxxxxxxxxxxxxx")
print(len(urls), "videos")
```

> `pytube` breaks whenever YouTube changes its player, so if downloads fail, use a maintained fork such as `pytubefix` instead.
