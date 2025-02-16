# YouTube MP3 Downloader

This project allows you to download all videos from a specified YouTube playlist and convert them into MP3 format.

## Features

- Retrieve video URLs from a YouTube playlist.
- Download videos as MP3 files.
- Simple command-line interface.

## Requirements

- Python 3.x
- `pytube` for downloading videos.
- `pydub` or `ffmpeg` for audio conversion.

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/youtube-mp3-downloader.git
   ```

2. Navigate to the project directory:

   ```sh
   cd youtube-mp3-downloader
   ```

3. Install the required dependencies:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Open `src/main.py` and specify the YouTube playlist URL.

2. Run the script:

   ```sh
   python src/download_playlist.py https://www.youtube.com/watch?list=PLpshJy6oyjM9fD2YtXafkvuSCkkprffuO
   ```

3. The MP3 files will be saved in the specified output directory.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
