from bs4 import BeautifulSoup
import requests
import re
import csv

csv_filename = "billboard_top100.csv"
csv_open = open(csv_filename, "w+", encoding='utf-8')
csv_writer = csv.writer(csv_open)
csv_writer.writerow( ('HOT song', 'image.url', ) )

crawling_url ="https://www.billboard.com/charts/hot-100"

response = requests.get(crawling_url)

bs = BeautifulSoup(response.text, 'html.parser')

chart_list = bs.find_all('li', {'class':re.compile("chart-list__element display--flex")})

for chart in chart_list:
	rank = chart.find_all('span', {'class':re.compile('chart-element__rank__number')})
	real_rank = rank[0].text
	song = chart.find_all('span', {'class':re.compile('chart-element__information__artist text--truncate color--secondary')})
	real_song = song[0].text
	artist = chart.find_all('span', {'class':re.compile('chart-element__information__song text--truncate color--primary')})
	real_artist = artist[0].text
	print(f"""{real_rank}:{real_song}:{real_artist}""")	
	csv_writer.writerow( (real_rank, real_song, real_artist) )
csv_open.close()

