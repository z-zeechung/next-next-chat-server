from search.Search import Search
from typing import List

from data_types import SearchResult


class Baidu(Search):

    def search(self, query: str, count: int, index: int) -> List[SearchResult]:

        import requests, math
        from bs4 import BeautifulSoup

        index = index
        pages = math.ceil(count / 5)
        ret = []
        for i in range(pages):
            url = f"http://www.baidu.com/s?wd={query}&cl=3&pn={index}&ie=utf-8&rn={5}&tn=baidurt"
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            soup = soup.find('div', class_='content')
            soup = soup.find_all('table', class_='result')
            for s in soup:
                s = s.find('td', class_='f')
                title_elem = s.find('h3', class_='t')
                title = title_elem.get_text()
                digest = s.find('font').get_text()
                bottom_url = s.find('font').find('font').get_text()
                digest = digest.replace(bottom_url, '').replace('百度快照', '')
                digest = title + '：' + digest
                digest = digest.replace('\n', '')
                digest = " ".join([x for x in digest.split() if x != ''])
                url = title_elem.find('a').get('href')
                ret.append(SearchResult(url, digest))
            index += 5
        ret = ret[:count]
        return ret