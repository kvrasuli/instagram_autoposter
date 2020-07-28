from aux_funcs import get_file_extension, download_a_pic
import requests
from pathlib import Path


def fetch_spacex_last_launch():
    response = requests.get('https://api.spacexdata.com/v4/launches/latest')
    response.raise_for_status()
    image_urls = response.json()['links']['flickr']['original']

    for i, url in enumerate(image_urls):
        file_extension = get_file_extension(url)
        download_a_pic(url, f'spacex_{i}{file_extension}')


if __name__ == '__main__':
    Path('images').mkdir(parents=True, exist_ok=True)
    fetch_spacex_last_launch()
