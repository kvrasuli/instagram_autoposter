# Space Instagram

This is the app automatically posting photos from the last SpaceX launch and also from Hubble website by specified category.

### How to install

You'll need to create two environment variables with your instagram username and password:
```
INSTAGRAM_USERNAME='your_username'
INSTAGRAM_PASSWORD='your_password'
```
You can put them into .env file next to main.py.

Just run the python script main.py with the following concole command:
```
python main.py
```

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).