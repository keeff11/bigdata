#!/usr/bin/env python3
import sys
import urllib.request as req
import urllib.parse as parse

if len(sys.argv)<=1:
    print("USAGE: download-forecast-argv <Region Number>")
    sys.exit()
regionNumber = sys.argv[1]

url = req.urlopen(f'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId={regionNumber}')

text = url.read().decode('utf-8')

print(text)