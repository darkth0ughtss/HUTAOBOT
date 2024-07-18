# BOT/features/pin.py

import yt_dlp
import os

def download_pinterest_media(link, download_path):
    """
    Download Pinterest media (image or video) from the given link.

    Args:
        link (str): The link to the Pinterest media.
        download_path (str): The path to download the media to.

    Returns:
        str: Path to the downloaded media file, or None if failed.
    """
    ydl_opts = {
        'outtmpl': os.path.join(download_path, '%(id)s.%(ext)s'),
        'format': 'best',  # best quality
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=True)
            media_id = info_dict.get("id", None)
            media_ext = info_dict.get("ext", None)
            media_path = os.path.join(download_path, f"{media_id}.{media_ext}")

            if os.path.exists(media_path):
                return media_path

    except Exception as e:
        print(f"𝐹𝑎𝑖𝑙𝑒𝑑 𝑡𝑜 𝑑𝑜𝑤𝑛𝑙𝑜𝑎𝑑 𝑃𝑖𝑛𝑡𝑒𝑟𝑒𝑠𝑡 𝑚𝑒𝑑𝑖𝑎")
        return None
