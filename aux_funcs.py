import requests
from pathlib import Path


def download_a_pic(url, filename):
    response = requests.get(url)
    response.raise_for_status()

    with open(f'images/{filename}', 'wb') as image:
        image.write(response.content)


def get_file_extension(url):
    return Path(url).suffix

