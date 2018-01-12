import requests
from bs4 import BeautifulSoup
import os


"""
传入某一个作品页的URL以及该女优的名字，下载图片到File/名字文件夹中。
"""

class GetBigImage:
    @classmethod
    def get_pic(cls, big_pic_page_url, name):
        raw_big_pic_page = requests.get(big_pic_page_url)
        soup = BeautifulSoup(raw_big_pic_page.text, 'html.parser')
        big_img_url = soup.find("a", class_="bigImage").img.get('src')
        id_block = soup.find("div", class_="col-md-3 info")
        identifier = id_block.p.span.find_next_sibling('span').string
        raw_pic = requests.get(big_img_url)
        if not os.path.exists('File/{}'.format(name)):
            os.makedirs('File/{}'.format(name))
        if not os.path.isfile('File/{}/{}.jpg'.format(name, identifier)):
            f = open('File/{}/{}.jpg'.format(name, identifier), 'wb')
            f.write(raw_pic.content)
            print('downloading {}   {}.jpg'.format(name, identifier))
            f.close()
