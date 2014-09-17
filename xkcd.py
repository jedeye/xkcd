#!/usr/bin/python

## Import libraries

import requests
import re
from PIL import Image
from StringIO import StringIO
import io


## Set initial variables

xkcd_url = "http://www.xkcd.com/"

## GET the number of the latest xkcd comic

initial_comic = requests.get(xkcd_url)
initial_comic_html = initial_comic.text
get_prev_url = re.compile('prev" href="/(\d*)')
locate_prev = re.search(get_prev_url, initial_comic_html)
initial_comic_number = locate_prev.group()
initial_comic_number = initial_comic_number[-4:]
initial_comic_number = int(initial_comic_number)
initial_comic_number += 1
print initial_comic_number

## Generate new URL, regex it for image, GET image and save.

while initial_comic_number >= 1:
	try:
		comic_page_url = xkcd_url + str(initial_comic_number)
		comic_page_url_header = requests.get(comic_page_url)
		comic_page_html = comic_page_url_header.text
		regex_for_comic_source = re.compile('http://imgs.xkcd.com/comics(.*)png')
		result_of_comic_source = re.search(regex_for_comic_source, comic_page_html)
		comic_url = result_of_comic_source.group()
		comic_image = requests.get(comic_url)
		temp_img_filename = str(initial_comic_number) + ".png"
		with open(temp_img_filename, 'wb') as file:
			file.write(comic_image.content)
		initial_comic_number -= 1
	except:
		initial_comic_number -= 1
		pass