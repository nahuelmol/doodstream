import requests
import json
import os

from dotenv import load_dotenv
load_dotenv(verbose=True)

API_KEY = os.getenv('DOOD_API_KEY')

def search_file():
	file 	= 'DB'
	url 	= 'https://doodapi.com/api/search/videos?key=' + API_KEY

	url_file = url + '&search_term='+ file 
	response = requests.get(url_file)

	res_str = response.content.decode('utf-8')
	res 	= json.loads(res_str)

	for each in res['result']:
		print(each['title'])

def send_subtitle():
	remote_sub 	= 'https://example.com/sub.vtt'
	local_sub  	= 'subs/"[Utsukushii-Raws] Dragon Ball - 003 (DVD 720x480 H264 AC3 2.0 Chap Sub).srt"'
	url 		= 'https://dood.so/e/xxx?c1_file='+ local_sub +'&c1_label=Japanese'

	res = requests.get(url)
	print(res)

def get_file_list():

	url = 'https://doodapi.com/api/file/list?key='+API_KEY
	res = requests.get(url)

	res_string 	= res.content.decode('utf-8')
	content 	= json.loads(res_string)
	msg 	= content['msg']
	files 	= content['result']['files']

	for each in files:
		print(each['title'])

	print('Files info:\n')
	print(files)

def get_link_to_upload():
	url = 'https://doodapi.com/api/upload/server?key='+API_KEY
	r = requests.get(url)
	print(r.content)


if __name__ == '__main__':
	search_file()