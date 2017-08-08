import requests as req
from bs4 import BeautifulSoup as bfs
import time

def get_links():
    html = requests.get('http://myjorney.tistory.com/category/%EC%BD%94%EB%94%A9/PYTHON%20%EA%B8%B0%EB%B3%B8%EB%AC%B8%EB%B2%95').text
    soup =bfs(html,'html.parser')

    data=[]
    for url in soup.select('#body > ul > li:nth-child(1) > a'):
        data.append(url['href'])

    return data

def get_content(link):
    abs_link ='http://myjorney.tistory.com'+link
    html = requests.get(abs_link).text
    soup = bs(html, 'html.parser')
    # 가져온 데이터로 뭔가 할 수 있겠죠?
    # 하지만 일단 여기서는 시간만 확인해봅시다.
    print(soup.select('h1')[0].text) # 첫 h1 태그를 봅시다.

if __name__=='__main__':
    start_time = time.time()
    for link in get_links():
        get_content(link)
    print("--- %s seconds ---" % (time.time() - start_time))