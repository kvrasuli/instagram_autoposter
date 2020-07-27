import requests
from pathlib import Path
import pprint

def download_a_pic(url, filename):
    Path('images/').mkdir(parents=True, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()

    with open(f'images/{filename}', 'wb') as f:
        f.write(response.content)

def fetch_spacex_last_launch():
    response = requests.get('https://api.spacexdata.com/v4/launches/latest')
    urls = response.json()['links']['flickr']['original']

    for i, url in enumerate(urls):
        download_a_pic(url, f'spacex_{i}.jpg')

if __name__ == '__main__':
    # fetch_spacex_last_launch()

# 'https://media.stsci.edu/uploads/image_file/image_attachment/1/full_jpg.jpg'
    pp = pprint.PrettyPrinter()
    response = requests.get('http://hubblesite.org/api/v3/image/1')
    image_list = response.json()['image_files']
    for image in image_list:
        print(image['file_url'])