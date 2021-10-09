from doodstream import DoodStream
from dotenv import load_dotenv
from pathlib import Path

from videos.util import INFO_VIDEOS_DIR 

import os

load_dotenv(verbose=True)
API_KEY = os.getenv('DOOD_API_KEY')

dood_user = DoodStream(API_KEY)

def look_for_user_data():
	print(dood_user.account_info())

def upload_video():
	VIDEO_FILES = []
	VIDEO_FILES = INFO_VIDEOS_DIR()

	video = 'DB006'

	if not VIDEO_FILES.count(video):
		exception = 'File does not exists'
		return exception

	video_path = 'videos/{}.mp4'.format(video)
	dood_user.local_upload(video_path)

if __name__ == '__main__':
	look_for_user_data()
	upload_video()