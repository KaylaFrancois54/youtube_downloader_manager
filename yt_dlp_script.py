import yt_dlp
import argparse

class YouTubeDownloader:
    def __init__(self, output_path='downloads/%(title)s.%(ext)s'):
        # Default settings for video download
        self.ydl_opts = {
            'format': 'best',  # Default format: best quality
            'outtmpl': output_path,  # Default output path
            'quiet': False,  # Show progress
            'noplaylist': True,  # Don't download entire playlists
        }

    def download_video(self, url):
        """
        Downloads a YouTube video using yt_dlp.
        Returns True if successful, False otherwise.
        """
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                ydl.download([url])  # Download the video
            return True
        except Exception as e:
            print(f"Download failed: {e}")
            return False


def main():
    # Setting up argparse for command-line arguments
    parser = argparse.ArgumentParser(description="Download YouTube videos using yt-dlp.")
    parser.add_argument('url', type=str, help='URL of the YouTube video to download')
    parser.add_argument('--output', type=str, default='downloads/%(title)s.%(ext)s',
                        help='Path to save the downloaded video (default: downloads/%(title)s.%(ext)s)')
    
    args = parser.parse_args()

    # Initialize the downloader
    downloader = YouTubeDownloader(output_path=args.output)
    
    # Start downloading the video
    success = downloader.download_video(args.url)
    
    if success:
        print(f"Video downloaded successfully to {args.output}")
    else:
        print("Download failed.")

if __name__ == '__main__':
    main()

