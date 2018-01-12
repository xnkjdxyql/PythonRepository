import requests
from bs4 import BeautifulSoup
import os


"""
javabus.info/actress前186页女优
的名字和地址，保存地址为当前目录下
的www.javbus.info文件夹下
的actressInfo.txt文件中

"""

base_url = 'https://www.javbus.info/actresses'
count = 0


if not os.path.exists('www.javbus.info'):
    print('Creating Folder.....')
    os.makedirs('www.javbus.info')
else:
    print('Folder already exist...')

actress_file=open("www.javbus.info/actressInfo.txt","w",encoding='utf-8')




for i in range(1, 187):
    url = base_url + "/{}".format(i)
    source_code = requests.get(url)
    soup = BeautifulSoup(source_code.text, 'html.parser')
    photos=soup.find_all(attrs={"class": "photo-frame"})
    for n in range(0, len(photos)):
        pic_title = photos[n].contents[1].get('title')
        pic_link = photos[n].parent.get('href')
        count = count+1
        actress_item = '%d  %s   %s' %(count, pic_title, pic_link)
        actress_file.write(str(actress_item)+'\n')
        print('wrinting actress_item {}'.format(count))
actress_file.close()