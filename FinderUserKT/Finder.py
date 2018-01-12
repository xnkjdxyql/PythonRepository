import requests
from bs4 import BeautifulSoup
import re

# 找到特定用户的帖子

base_url = 'http://93.t9p.today/forumdisplay.php?fid=19&page=1'
author = '缚青主'

for i in range(1, 1001):
    url = 'http://93.t9p.today/forumdisplay.php?fid=19&page={}'.format(i)
    raw_page = requests.get(url)
    raw_page.encoding = 'utf-8'
    plain_page = BeautifulSoup(raw_page.text, 'html.parser')
    # author_tags = plain_page.find_all("td", class_="author")
    try:
        author_tag = plain_page.find(text=author)
        post_tag = author_tag.find_parent("tbody")
        url_tag = post_tag.find("th", class_="subject")
        print('http://92.t9p.today/'+url_tag.span.a.get('href'))
    except:
        print('page {} not find'.format(i))
