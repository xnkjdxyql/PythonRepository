from bs4 import BeautifulSoup
import requests
import re
import os



class GetPics:
    def __init__(self, url, post_number):
        self.url = url
        self.post_number = post_number
        self.img_number = 1

    def getpic(self):
        raw_page = requests.get(self.url)
        raw_page.encoding = 'utf-8'
        soup = BeautifulSoup(raw_page.text, 'html.parser')
        img_tags = soup.find_all('img', file=re.compile("attachments/.*?\.jpg"))
        describe_tag = soup.find('td',class_='t_msgfont')
        post_title = soup.find('title')
        if not os.path.exists('posts/{}'.format(self.post_number)):
            os.makedirs('posts/{}'.format(self.post_number))
        f = open('posts/{}/{}.txt'.format(self.post_number, self.post_number), 'w', encoding='utf-8')
        f.write(self.url+'\n')
        f.write(post_title.text+'\n\n\n\n\t\t\t')
        for string in describe_tag.stripped_strings:
            f.write(string+'\n')
        f.close()
        for img_tag in img_tags:
            img_url = img_tag.get('file')
            real_url = 'http://91.t9p.today/'+img_url
            raw_img = requests.get(real_url)
            img_file = open('posts/{}/{}.jpg'.format(self.post_number, self.img_number), 'wb')
            img_file.write(raw_img.content)
            print('downing {}'.format(self.img_number))
            img_file.close()
            self.img_number +=1





