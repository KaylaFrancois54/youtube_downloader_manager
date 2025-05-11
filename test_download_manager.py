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
        mock_yt.streams.filter.return_value.first.return_value = mock_stream

        MockYouTube.return_value = mock_yt

        download_video("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "downloads")

    @mock.patch("main.YouTube")
    def test_download_video_invalid_resolution(self, MockYouTube):
        # Mock the YouTube object
        mock_yt = MockYouTube.return_value
        mock_yt.streams.filter.return_value = [] 

        with self.assertRaises(ValueError) as context:
            download_video("https://www.youtube.com/watch?v=invalid", "downloads", resolution="4k")

        self.assertEqual(str(context.exception), "Requested resolution not available.")

@mock.patch("main.YouTube", side_effect=RegexMatchError("Invalid URL", "some-pattern"))
def test_download_video_invalid_url(self, mock_yt):
    with self.assertRaises(RegexMatchError):
        download_video("invalid_url", "downloads")

    @mock.patch("main.YouTube", side_effect=URLError("Network unreachable"))
    def test_download_video_network_failure(self, MockYouTube):
        with self.assertRaises(ConnectionError):
            download_video("https://www.youtube.com/watch?v=fail", "downloads")

    @mock.patch("main.YouTube")
    def test_download_video_permission_error(self, MockYouTube):
        mock_stream = mock.Mock()
        mock_stream.download.side_effect = PermissionError("Access denied")

        mock_yt = mock.Mock()
        mock_yt.title = "Test Video"
        mock_yt.author = "Test Author"
        mock_yt.streams.filter.return_value.first.return_value = mock_stream

        MockYouTube.return_value = mock_yt

        with self.assertRaises(PermissionError):
            download_video("https://www.youtube.com/watch?v=test", "restricted_folder")


if __name__ == "__main__":
    unittest.main()


