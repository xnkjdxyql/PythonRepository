import requests
from bs4 import BeautifulSoup
import re

base_url = 'http://bbs.tianya.cn/post-no04-1858762-1.shtml'
n=1
for i in range(1,613):
    base_url = 'http://bbs.tianya.cn/post-no04-1858762-{}.shtml'.format(i)
    mysession = requests.session()
    headers = {
    'Referer':'http://bbs.tianya.cn/post-no04-1858762-612.shtml',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }
    raw_page = mysession.get(base_url,headers = headers)
    soup = BeautifulSoup(raw_page.text,'html.parser')
    imgs = soup.find_all('img')
    for img in imgs:
        img_url =(img.get('original'))
        if(img_url != None):
            # raw_img = mysession.get(img_url)
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # mysession = requests.session()
            # raw_img = mysession.get(img_url)
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            mysession = requests.session()
            raw_img = mysession.get(img_url,headers = headers)
            f = open('pictures/' + str(n) + '.jpg','wb')
            f.write(raw_img.content)
            print('downloading pictures {}'.format(n))
            n = n+1
            f.close()


