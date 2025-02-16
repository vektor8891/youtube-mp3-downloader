import os
from pytube import Playlist
from utils import download_video, convert_to_mp3

def main():
    playlist_url = input("Enter the YouTube playlist URL: ")
    playlist = Playlist(playlist_url)

    for video in playlist.videos:
        print(f"Downloading: {video.title}")
        video_url = video.watch_url
        download_video(video_url)
        convert_to_mp3(video.title)

if __name__ == "__main__":
    main()