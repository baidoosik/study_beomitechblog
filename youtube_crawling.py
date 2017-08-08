import requests as req
from bs4 import BeautifulSoup as bfs
import json
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "study.settings")

import django
django.setup()

from youtube.models import Youtube


#python 파일의 위치


def parse_youtube():
    url='https://www.youtube.com/results?search_query=개발자'

    html = req.get(url).text
    soup = bfs(html,'html.parser')

    data={}

    for tag in soup.select('li > div > div > div.yt-lockup-content > h3 > a'):
        data[tag.text]='https://www.youtube.com/'+tag['href']

    return data

if __name__=='__main__':
    youtube_data_dict = parse_youtube()
    for title, url in youtube_data_dict.items():
        Youtube(title=title,url=url).save()