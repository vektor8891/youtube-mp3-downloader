def download_video(url, output_path):
    from pytube import YouTube
    yt = YouTube(url)
    video_stream = yt.streams.filter(only_audio=True).first()
    video_stream.download(output_path)
    return os.path.join(output_path, video_stream.default_filename)

def convert_to_mp3(video_file_path):
    from pydub import AudioSegment
    mp3_file_path = video_file_path.rsplit('.', 1)[0] + '.mp3'
    audio = AudioSegment.from_file(video_file_path)
    audio.export(mp3_file_path, format='mp3')
    os.remove(video_file_path)  # Remove the original file after conversion
    return mp3_file_path

def process_playlist(playlist_url, output_path):
    from pytube import Playlist
    playlist = Playlist(playlist_url)
    for video_url in playlist.video_urls:
        video_file_path = download_video(video_url, output_path)
        convert_to_mp3(video_file_path)