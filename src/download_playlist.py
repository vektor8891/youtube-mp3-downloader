import os
import sys

def download_playlist_as_mp3(playlist_url):
    # Create a directory to store the downloaded MP3 files
    if not os.path.exists('mp3_downloads'):
        os.makedirs('mp3_downloads')

    # Command to download and convert videos to MP3
    command = f'yt-dlp -x --audio-format mp3 --output "mp3_downloads/%(title)s.%(ext)s" {playlist_url}'

    # Execute the command
    os.system(command)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python download_playlist.py <playlist_url>")
        sys.exit(1)

    playlist_url = sys.argv[1]
    download_playlist_as_mp3(playlist_url)