
""" this is my first git.
"""
import html
from urllib.request import urlopen, Request

ACCU_URL = 'https://www.accuweather.com/uk/ua/lviv/324561/weather-forecast/324561'

#getting url from server

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'}
accu_request = Request (ACCU_URL, headers=headers)
accu_page = urlopen (accu_request).read()
accu_page = str (accu_page)

accu_temp_tag = '<span class="after-temp">'
accu_temp_tag_size = len (accu_temp_tag)
accu_temp_tag_index = accu_page.find (accu_temp_tag)
accu_temp_value_start = accu_temp_tag_index + accu_temp_tag_size
accu_temp = ''
for char in accu_page [accu_temp_value_start:]:
	if char != '<': 
		accu_temp += char
	else:
		break
	 

print ('ACCUWEATHER: \n')
print (f'TEMPERATURE: {html.unescape(accu_temp)} \n')




#user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36



