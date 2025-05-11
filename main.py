import argparse
from pytube.exceptions import RegexMatchError
from pytube import YouTube
from pytube.cli import on_progress
from urllib.parse import urlparse

def some_callback_function(stream, chunk, bytes_remaining):
    pass  # No-op callback

def validate_url(url):
    parsed = urlparse(url)
    return 'youtube.com' in parsed.netloc or 'youtu.be' in parsed.netloc

def download_video(url, output_dir, resolution=None):
    try:
        yt = YouTube(url)
        print(f"Title: {yt.title}")
        print(f"Author: {yt.author}")
        print(f"Downloading to: {output_dir}")
        
        if resolution:
            streams = yt.streams.filter(res=resolution)
            if not streams:  # Check if the resolution is not found
                raise ValueError("Requested resolution not available.")
            stream = streams[0]  # Use the first stream in the list
            
        else:
            stream = yt.streams.first()
        
        # Try downloading the stream
        stream.download(output_dir)
        print("[SUCCESS] Download completed.")
        
    except ValueError as e:
        print(f"[ERROR] {e}")
        raise 
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")
        raise

def ensure_output_directory(path):
    try:
        os.makedirs(path, exist_ok=True)
    except Exception as e:
        print(f"[ERROR] Could not create/access output directory '{path}': {e}")
        sys.exit(1)

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="YouTube Video Downloader using pytube",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--url", required=True, help="YouTube video URL to download")
    parser.add_argument("--output", default="downloads", help="Directory to save the video")
    parser.add_argument("--resolution", default="720p", help="Desired resolution (e.g., 720p, 1080p)")

    return parser.parse_args()

def main():
    args = parse_arguments()

    if not validate_url(args.url):
        print(f"[ERROR] The provided URL doesn't seem to be a valid YouTube link.")
        sys.exit(1)

    ensure_output_directory(args.output)

    download_video(args.url, args.output, args.resolution)

if __name__ == "__main__":
    main()

