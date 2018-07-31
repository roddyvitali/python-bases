import requests
from bs4 import BeautifulSoup as Parse_html
import urllib.request as request_image
from datetime import datetime, date, time, timedelta

def run():
	comics_amount = int(input('How many days have you been without reading comics?\nA// '))

	today = date.today()
	
	for i in range (0, comics_amount):
		comic_day = today - timedelta(days = i)
 
		inside_url = requests.get('http://www.gocomics.com/doonesbury/{}/{}/{}'.format(comic_day.year,comic_day.month,comic_day.day))
		url_html = Parse_html(inside_url.content, 'html.parser')
		image_container = url_html.find('picture',{'class':'item-comic-image'})
		
		image_url = image_container.find('img')['src']
		image_name = 'doonesbury{}.{}.{}.jpg'.format(comic_day.year,comic_day.month,comic_day.day)
		print('Downloading the image {}'.format(image_name))
		request_image.urlretrieve('{}'.format(image_url), image_name)

	print ('\nSuccesfull Download')

if __name__ == '__main__':
	run()