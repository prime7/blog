import requests
requests.packages.urllib3.disable_warnings()
from bs4 import BeautifulSoup
from .models import News

def scrape_theonion():
	session = requests.Session()
	session.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"}
	url = 'https://www.theonion.com/'

	content = session.get(url, verify=False).content

	soup = BeautifulSoup(content, "html.parser")
	posts = soup.find_all('div',{'class':'curation-module__item'})[:3]
	for i in posts:
		link = i.find_all('a',{'class':'js_curation-click'})[1]['href']
		title = i.find_all('a',{'class':'js_curation-click'})[1].text
		image_source = i.find('img',{'class':'featured-image'})['data-src']

		headline = News()
		headline.title = title
		headline.url = link
		headline.image = image_source
		headline.website = "theonion.com"
		headline.save()


def scrape_wired():
	session = requests.Session()
	session.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"}
	url = 'https://www.wired.com/most-popular/'

	content = session.get(url, verify=False).content

	soup = BeautifulSoup(content, "html.parser")

	posts = soup.find_all('li',{'class':'archive-item-component'})[:3]
	for post in posts:
		image_link = post.find('img')['src']
		url = 'https://www.wired.com'+post.find('a')['href']
		title = post.find('h2',{'class':'archive-item-component__title'}).get_text()

		headline = News()
		headline.title = title
		headline.url = url
		headline.website = "wired.com"
		headline.image = image_link
		headline.save()

def remove():
	News.objects.all().delete()

def scrape():
	scrape_theonion()
	scrape_wired()