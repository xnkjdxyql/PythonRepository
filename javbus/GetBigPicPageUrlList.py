from bs4 import BeautifulSoup
import requests


'''
创建本类的实例，调用实例方法，参数为一个女优作品列表页的地址，返回一个各作品url地址的集合列表
'''

class GetBigPigPages:

        def __init__(self):
            self.BigPicUrlsInOnePage = []

        def get_big_pic_urls_within_page(self, url):
            soup = BeautifulSoup(requests.get(url).text, 'html.parser')
            img_list = soup.find_all("a", class_="movie-box")
            for img_tag in img_list:
                self.BigPicUrlsInOnePage.append(img_tag.get('href'))
            return self.BigPicUrlsInOnePage




