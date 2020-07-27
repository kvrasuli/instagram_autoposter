import requests

def download_a_pic(url, filename):
    response = requests.get(url)
    response.raise_for_status()

    with open(f'images/{filename}', 'wb') as f:
        f.write(response.content)

def get_file_extension(url):
    file_extension = url.split('.')[-1]
    return file_extension