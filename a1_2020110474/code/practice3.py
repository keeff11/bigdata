from bs4 import BeautifulSoup
import urllib.request as req
import ssl
import datetime

url = 'https://finance.naver.com/marketindex/'
html = req.urlopen(url)

soup = BeautifulSoup(html, 'html.parser')
price = soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value")
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 

print("DATE: "+now+" 미국 USD : " + price.string)