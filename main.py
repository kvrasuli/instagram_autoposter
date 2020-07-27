import requests
from pathlib import Path
import pprint

pp = pprint.PrettyPrinter()

def download_a_pic(url, filename):
    Path('images/').mkdir(parents=True, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()

    with open(f'images/{filename}', 'wb') as f:
        f.write(response.content)


def fetch_spacex_last_launch():
    response = requests.get('https://api.spacexdata.com/v4/launches/latest')
    image_urls = response.json()['links']['flickr']['original']

    for i, url in enumerate(image_urls):
        file_extension = get_file_extension(url)
        download_a_pic(url, f'spacex_{i}.{file_extension}')


def get_file_extension(url):
    file_extension = url.split('.')[-1]
    return file_extension


def fetch_hubble_photos(id):
    response = requests.get(f'http://hubblesite.org/api/v3/image/{id}')
    image_files = response.json()['image_files']

    for file in image_files:
        image_url = file['file_url']
        if image_url.split('/')[-2] == '1':
            file_extension = get_file_extension(image_url)
            download_a_pic('https:' + image_url, f'hubble_{id}.{file_extension}')

if __name__ == '__main__':
    fetch_spacex_last_launch()
    fetch_hubble_photos(1)
