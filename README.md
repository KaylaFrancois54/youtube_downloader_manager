# youtube_downloader_manager

In this project I will be developing a command-line Youtube Download Manager using Python. By leveraging external libraries such as Pytube, and tqdm and my prior knowledge of Python fundamentals, I'll create a tool that:

1. Downloads youtube videos via url
2. Offers configurable options (ex: output folder, resolution)
3. Provides progress feedback during downloads
4. Gracefully handles errors(invalid urls, permissions problems, connection failures, etc...)

My goal is to build a tool tht can evolve overtime- once the basics are in place.

UPDATE:

I had a hard time with pytube, even installing the github version did not work for me. Alternatively, I've used yt-dlp which also handles downloading youtube videos while supporting multiple platforms. I have placed these files under a separate branch named "test-branch". Ultimately, yt_dlp was the better route for this assignment.
