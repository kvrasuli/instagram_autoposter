from pathlib import Path
from fetch_hubble import fetch_hubble_collection
from fetch_spacex import fetch_spacex_last_launch
from post_images import post_all_images
from dotenv import load_dotenv
import os


def main():
    load_dotenv()
    username = os.getenv('INSTAGRAM_USERNAME')
    password = os.getenv('INSTAGRAM_PASSWORD')
    Path('images').mkdir(parents=True, exist_ok=True)
    Path('converted_images').mkdir(parents=True, exist_ok=True)
    fetch_spacex_last_launch()
    fetch_hubble_collection('news')
    post_all_images(username, password)


if __name__ == '__main__':
    main()
