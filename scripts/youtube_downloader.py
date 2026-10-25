from pytube import YouTube

def download_video(video_url: str):
    yt = YouTube(video_url)
    stream = yt.streams.get_highest_resolution()
    stream.download()

def download_playlist(playlist_url: str):
    yt = YouTube(playlist_url)
    for video in yt.videos:
        download_video(video.watch_url)

if __name__ == "__main__":
    download_video("https://music.youtube.com/watch?v=LPMmfmsUhZ8")