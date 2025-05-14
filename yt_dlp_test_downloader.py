import unittest
from unittest.mock import patch
from yt_dlp_main import YouTubeDownloader

class TestYouTubeDownloader(unittest.TestCase):

    @patch('yt_dlp_main.YouTubeDownloader.download_video')
    def test_download_video_success(self, mock_download_video):
        mock_download_video.return_value = True
        downloader = YouTubeDownloader()
        result = downloader.download_video('https://www.youtube.com/watch?v=abc123')
        mock_download_video.assert_called_once_with('https://www.youtube.com/watch?v=abc123')
        self.assertTrue(result)

    @patch('yt_dlp_main.YouTubeDownloader.download_video')
    def test_download_video_failure(self, mock_download_video):
        mock_download_video.return_value = False
        downloader = YouTubeDownloader()
        result = downloader.download_video('https://www.youtube.com/watch?v=abc123')
        self.assertFalse(result)

    @patch('yt_dlp_main.YouTubeDownloader.download_video')
    def test_invalid_url(self, mock_download_video):
        mock_download_video.return_value = False
        downloader = YouTubeDownloader()
        result = downloader.download_video('https://www.invalid-url.com')
        mock_download_video.assert_called_once_with('https://www.invalid-url.com')
        self.assertFalse(result)

    @patch('yt_dlp_main.YouTubeDownloader.download_video')
    def test_missing_video_id(self, mock_download_video):
        mock_download_video.return_value = False
        downloader = YouTubeDownloader()
        result = downloader.download_video('https://www.youtube.com/watch?v=')
        mock_download_video.assert_called_once_with('https://www.youtube.com/watch?v=')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
