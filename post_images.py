from PIL import Image
from instabot import Bot
from pathlib import Path
from dotenv import load_dotenv
import os


def convert_image(image_file):
    image = Image.open(image_file)
    image.thumbnail((1080, 1080))
    image_stem = Path(image_file).stem
    image.save(Path.cwd().joinpath('converted_images').joinpath(f"{image_stem}.jpg"), format='JPEG')
    Path(image_file).unlink()
        

def post_all_images(username, password):
    bot = Bot()
    bot.login(username=username, password=password)
    images = Path.cwd().joinpath('images')
    for image in images.iterdir():
        try:
            convert_image(image)
        except ValueError:
            Path(image).unlink()

    converted_images = Path.cwd().joinpath('converted_images')
    for image in converted_images.iterdir():
        bot.upload_photo(image, caption='caption')


if __name__ == '__main__':
    load_dotenv()
    username = os.getenv('INSTAGRAM_USERNAME')
    password = os.getenv('INSTAGRAM_PASSWORD')
    Path('converted_images').mkdir(parents=True, exist_ok=True)
    post_all_images(username, password)