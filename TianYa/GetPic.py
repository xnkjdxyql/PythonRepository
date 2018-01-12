import requests
import os
from bs4 import BeautifulSoup

url = 'http://bbs.tianya.cn/post-no04-2747897-1.shtml'
# url = 'http://bbs.tianya.cn/post-no04-2354217-1.shtml'
header = {
    # 'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    # 'Cookie':'id=24fe130a3fa76f24||t=1509606699|et=730|cs=002213fd48b0602004f3e11140',
    'Referer': 'http://bbs.tianya.cn/post-no04-2747897-1.shtml',
    # 'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA5'
    #               '8N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Mobile Safari/537.36'

}
folder_path = 'tianya'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print('creating folder: {}'.format(folder_path))
else:
    print('folder already exist!')
source_code = requests.get(url,headers = header)
plain_text = source_code.text
soup = BeautifulSoup(plain_text,"html.parser")

text = soup.select('img[original]')
for i in range(0,len(text)):
    pic_link = text[i].get('original')
    raw_pic = requests.get(pic_link,headers = header,timeout=10)
    pic_name = pic_link[-10:-5] + '.jpg'
    with open('tianya/{}'.format(pic_name),'wb') as pic_file:
            pic_file.write(raw_pic.content)
            print('writing pic_file {}/{}'.format(i,len(text)))


