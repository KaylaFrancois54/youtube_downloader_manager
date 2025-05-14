import unittest
from unittest import mock
from main import download_video
from pytube.exceptions import RegexMatchError
from urllib.error import URLError


class TestYouTubeDownloader(unittest.TestCase):

    @mock.patch("main.YouTube")
    def test_download_video_success(self, MockYouTube):
        mock_stream = mock.Mock()
        mock_stream.download.return_value = None

        mock_yt = mock.Mock()
        mock_yt.title = "Test Video"
        mock_yt.author = "Test Author"
        mock_yt.streams.filter.return_value = [mock_stream]

        MockYouTube.return_value = mock_yt

        download_video("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "downloads", resolution="720p")

    @mock.patch("main.YouTube")
    def test_download_video_invalid_resolution(self, MockYouTube):
        mock_yt = MockYouTube.return_value
        mock_yt.streams.filter.return_value = []  # Simulate no stream found

        with self.assertRaises(ValueError) as context:
            download_video("https://www.youtube.com/watch?v=invalid", "downloads", resolution="4k")

        self.assertEqual(str(context.exception), "Requested resolution not available.")

    @mock.patch("main.YouTube", side_effect=RegexMatchError("Invalid URL", "some-pattern"))
    def test_download_video_invalid_url(self, MockYouTube):
        with self.assertRaises(RegexMatchError):
            download_video("invalid_url", "downloads")

    @mock.patch("main.YouTube", side_effect=URLError("Network unreachable"))
    def test_download_video_network_failure(self, MockYouTube):
        with self.assertRaises(URLError):
            download_video("https://www.youtube.com/watch?v=fail", "downloads")

    @mock.patch("main.YouTube")
    def test_download_video_permission_error(self, MockYouTube):
        mock_stream = mock.Mock()
        mock_stream.download.side_effect = PermissionError("Access denied")

        mock_streams = mock.Mock()
        mock_streams.filter.return_value = [mock_stream]  # Matches .filter()[0]

        mock_yt = mock.Mock()
        mock_yt.title = "Test Video"
        mock_yt.author = "Test Author"
        mock_yt.streams = mock_streams

        MockYouTube.return_value = mock_yt

        with self.assertRaises(PermissionError):
            download_video("https://www.youtube.com/watch?v=test", "restricted_folder", resolution="720p")


if __name__ == "__main__":
    unittest.main()


