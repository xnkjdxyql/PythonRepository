import requests
from bs4 import BeautifulSoup
import os


"""
javabus.info/actress前186页女优
的图片,保存地址为当前目录下的
www.javbus.info/img文件夹下

"""

base_url = 'https://www.javbus.info/actresses'
count = 0


if not os.path.exists('www.javbus.info/img'):
    print('Creating img Folder.....')
    os.makedirs('www.javbus.info/img')
else:
    print('Folder already exist...')


for i in range(1, 187):
    url = base_url + "/{}".format(i)
    source_code = requests.get(url)
    soup = BeautifulSoup(source_code.text, 'html.parser')
    photos=soup.find_all(attrs={"class": "photo-frame"})
    for n in range(0, len(photos)):
        pic_link = photos[n].contents[1].get('src')
        pic_title = photos[n].contents[1].get('title')
        count = count+1
        raw_pic=requests.get(pic_link,timeout=5)
        with open('www.javbus.info/img/{}.jpg'.format(pic_title),'wb') as pic_file:
            pic_file.write(raw_pic.content)
        print("wrinting {}/{}/{}".format(n,i,187), pic_title)
