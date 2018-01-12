import re
import requests
from bs4 import BeautifulSoup
import os


"""
将actressInfo.txt文件中的所有地址以一个dic的形式返回
"""

class GetActressMainPageDics():
    actress_file = open('www.javbus.info/actressInfo.txt','r',encoding='utf-8')
    actress_item = []
    main_page_url_dics = {}
    @classmethod
    def get_pages(cls):
        for line in cls.actress_file:
            cls.actress_item = re.split(r'(\s)+', line)
            cls.main_page_url_dics[cls.actress_item[2]] = cls.actress_item[4]

        return cls.main_page_url_dics

# main_page_url_dics = {}
# actress_file = open('www.javbus.info/actressInfo.txt', 'r', encoding='utf-8')
# for line in actress_file:
#     actress_item = re.split(r'(\s)+', line)
#     # print(actress_item)
#     main_page_url_dics[actress_item[2]] = actress_item[4]
#     print('writing {} into dics'.format(actress_item[2]))
# print(main_page_url_dics)
