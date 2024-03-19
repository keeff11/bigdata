import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'xml')
    item = soup.find_all('item')
    for i in item:
        location = i.find_all('location')
        for j in location:
            city = j.find('city').text
            tmEf = j.find('data').find('tmEf').text
            wf = j.find('data').find('wf').text               
            print(f"[{tmEf}] {city}: {wf}")

if __name__ == "__main__":
    main()
