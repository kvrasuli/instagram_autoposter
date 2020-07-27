from pathlib import Path
from fetch_hubble import fetch_hubble_collection
from fetch_spacex import fetch_spacex_last_launch
from post_images import post_all_images


if __name__ == '__main__':
    Path('images/').mkdir(parents=True, exist_ok=True)
    fetch_spacex_last_launch()
    fetch_hubble_collection('news')
    post_all_images()



