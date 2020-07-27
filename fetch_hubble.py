from aux_funcs import get_file_extension, download_a_pic
import requests
from pathlib import Path


def fetch_hubble_photo(id):
    response = requests.get(f'http://hubblesite.org/api/v3/image/{id}')
    response.raise_for_status()
    image_files = response.json()['image_files']
    image_url = image_files[-1]['file_url']
    file_extension = get_file_extension(image_url)
    download_a_pic('https:' + image_url, f'hubble_{id}.{file_extension}')


def fetch_hubble_collection(collection_name):
    response = requests.get(f'http://hubblesite.org/api/v3/images/{collection_name}')
    response.raise_for_status()
    pic_list = response.json()
    for pic in pic_list:
        fetch_hubble_photo(pic['id'])


if __name__ == '__main__':
    Path('images/').mkdir(parents=True, exist_ok=True)
    fetch_hubble_collection('starships')