from GetAllMainPageUrlDics import GetActressMainPageDics
import requests
from bs4 import BeautifulSoup


"""
创建本类的实例,调用方法，传入第一页（主页）地址，返回总页数,名字
"""


class GetTotalPageNumAndName:
    name_to_url_dic = GetActressMainPageDics.get_pages()
    all_base_pages = name_to_url_dic.values()
    not_exist_title = '404 Page Not Found!'

    def __init__(self, name):
        self.name = name;
        self.count = 0
        self.is_next_exist = True

    def get_total_pages_from_url(self, base_url):
        while self.is_next_exist:
            self.count += 1
            req_url = base_url + '/{}'.format(self.count)
            source_code = requests.get(req_url)
            soup = BeautifulSoup(source_code.text, 'html.parser')
            # print(soup.title.string)
            page_title = soup.title.string
            if page_title == self.not_exist_title:
                self.is_next_exist = False
        #     else:
        #         print('page {} exist'.format(self.count))
        # print('total pages {}'.format(self.count-1))
        return self.count


    # @classmethod
    # def get_total_page_from_name(cls, name):
    #     base_url = cls.name_to_base_url(name)
    #     cls.get_total_pages_from_url(base_url)
    #     return cls.count


    #
    # @classmethod
    # def get_actress_name(cls,base_url):
    #     source_code_name = requests.get(base_url)
    #     soup_name = BeautifulSoup(source_code_name.text,'html.parser')
    #     name = soup_name.find("div", class_="photo-frame").img.get('title')
    #     return name

    @classmethod
    def base_page_to_name(cls, base_page):
        return list(cls.name_to_url_dic.keys())[list(cls.name_to_url_dic.values()).index(base_page)]

    @classmethod
    def name_to_base_url(cls,name):
        return cls.name_to_url_dic[name]




# name_to_url_dic = GetActressMainPageDics.get_pages()
# all_main_pages = name_to_url_dic.values()
#
# for main_page in all_main_pages:
#     print(main_page)




