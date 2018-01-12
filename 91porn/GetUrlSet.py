from bs4 import BeautifulSoup
import requests
import re
import os


"""
取得一个帖子列表页中的所有帖子的地址
"""

# for i in range(1,1001):
#     url = "http://91.t9p.today/forumdisplay.php?fid=19&page={}".format(i)
#     print(url)


class GetPostUrlSet:
    def __init__(self, url):
        self.url = url

    def get_urls_set(self):
        req = requests.get(self.url)
        req.encoding = 'utf-8'
        soup = BeautifulSoup(req.text, 'html.parser')
        post_url_set = set()
        post_url_list = soup.find_all(href=re.compile("viewthread.php\?tid=(\d+?)&extra=page%([\d\w]{3})$"))
        for post_url in post_url_list:
            relative_url = post_url.get('href')
            real_post_url = 'http://91.t9p.today/' + relative_url
            post_url_set.add(real_post_url)
        return post_url_set




