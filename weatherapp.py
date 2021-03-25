
""" this is my first git.
"""
import html
from urllib.request import urlopen, Request

ACCU_URL = 'https://www.accuweather.com/uk/ua/lviv/324561/weather-forecast/324561'
ACCU_TAGS = ('<div class="temp">', '<span class="phrase">')

#accu_temp_tag = '<div class="temp">'
#accu_phrase_tag = '<span class="phrase">'	 

def get_request_headers():
	return {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'}


def get_page_source(url):
	"""
	дістаємо дані з сторінки і повертає як стрічку, а не як байти
	"""
	request = Request (url, headers = get_request_headers())
	page_source = urlopen(request).read()
	return page_source.decode('utf-8')

def get_tag_content(page_content, tag):
	"""
	"""
	tag_index = page_content.find(tag)
	tag_size = len (tag)
	value_start = tag_index + tag_size
	
	content = ''
	for c in page_content[value_start:]:
		if c != '<':
			content += c
		else:
			break
	return content
		
def get_weather_info (page_content, tags):
	return tuple ([get_tag_content (page_content, tag) for tag in tags])

def produce_output(provider_name, temp, condition):
	"""
	"""
	print (f'\n{provider_name}:')
	print (f'TEMPERATURE: {html.unescape(temp)} \n')
	print (f'CONDITION: {html.unescape(condition)} \n')
	

def main():          #!!!!!!!!!!!!!!!!!!!!!! 
	""" main entry point
	"""
	weather_sites = {"ACCUWEAHER": (ACCU_URL, ACCU_TAGS)} #"RP5": (PR5_URL, RP5_TAGS)
	# weather_sites - словник
	for name in weather_sites: 
		url, tags = weather_sites[name]  # кортеж 
		content = get_page_source(url)
		temp, condition = get_weather_info (content, tags)
		produce_output (name, temp, condition)
	                 

	
if __name__ == '__main__':
	main()



# python3 weatherapp.py














