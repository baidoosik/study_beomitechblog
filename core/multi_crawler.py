import requests as req
from bs4 import BeautifulSoup as bfs
import time

from multiprocessing import Pool

def get_links():
    request_headers = {
        'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 '
                       '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'),
        'Referer': 'http://myjorney.tistory.com',  # 뉴스홈
    }
    html = req.get('http://myjorney.tistory.com/category/%EC%BD%94%EB%94%A9/PYTHON%20%EA%B8%B0%EB%B3%B8%EB%AC%B8%EB%B2%95',headers=request_headers).text
    soup = bfs(html,'html.parser')

    data=[]
    for url in soup.select('#body > ul > li > a'):
        data.append(url['href'])
        print(url['href'])

    return data

def get_content(link):
    request_headers = {
        'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 '
                       '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'),
        'Referer': 'http://myjorney.tistory.com',  # 뉴스홈
    }
    abs_link ='http://myjorney.tistory.com'+link
    html = req.get(abs_link,headers=request_headers).text
    soup = bfs(html, 'html.parser')
    # 가져온 데이터로 뭔가 할 수 있겠죠?
    # 하지만 일단 여기서는 시간만 확인해봅시다.
    print(soup.select('#head > h2 > a')[0].text) # 첫 h1 태그를 봅시다.

if __name__=='__main__':
    start_time = time.time()
    pool =Pool(processes=4)
    pool.map(get_content,get_links())
    print("--- %s seconds ---" % (time.time() - start_time))