# BOT/features/yt.py

import yt_dlp
import os

def download_youtube_video(link, download_path):
    """
    Download YouTube video from the given link.

    Args:
        link (str): The link to the YouTube video.
        download_path (str): The path to download the video to.

    Returns:
        str: Path to the downloaded video file, or None if failed.
    """
    ydl_opts = {
        'outtmpl': os.path.join(download_path, '%(id)s.%(ext)s'),
        'format': 'best',  # best quality
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=True)
            video_id = info_dict.get("id", None)
            video_ext = info_dict.get("ext", None)
            video_path = os.path.join(download_path, f"{video_id}.{video_ext}")

            if os.path.exists(video_path):
                return video_path

    except Exception as e:
        print(f"Failed to download YouTube video: {e}")
        return None
