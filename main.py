from doodstream import DoodStream
from dotenv import load_dotenv
from pathlib import Path

import os

#DoodStream library seems to be deprecated

load_dotenv(verbose=True)
API_KEY = os.getenv('DOOD_API_KEY')

dood_user = DoodStream(API_KEY)

print(dood_user.account_info())

def upload_video():
	video_path = 'videos/DB006.mp4'
	dood_user.local_upload(video_path)

upload_video()