from PIL import Image
from instabot import Bot
from dotenv import load_dotenv
import os


def prepare_image(image_file):
    try:
        image = Image.open(image_file)
        image.thumbnail((1080, 1080))
        image.save(f"{image_file.split('.')[0]}.jpg", format='JPEG')
        os.remove(image_file)
    except ValueError:
        os.remove(image_file)


def post_all_images():
    load_dotenv()
    username = os.getenv('INSTAGRAM_USERNAME')
    password = os.getenv('INSTAGRAM_PASSWORD')
    bot = Bot()
    bot.login(username=username, password=password)
    
    images = os.listdir('images/')
    for image in images:
        prepare_image(f'images/{image}')
        bot.upload_photo(image, caption='caption')
        if bot.api.last_response.status_code != 200:
            print(bot.api.last_response)

if __name__ == '__main__':
    post_all_images()