import requests
from bs4 import BeautifulSoup
import urllib.request
for i in range(1,266):
    url = 'http://jandan.net/ooxx/page-264'
    next_url=url.replace('264',str(i))
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
    source_code = requests.get(next_url,headers = header)
    plain_text = source_code.text
    Soup = BeautifulSoup(plain_text,'html.parser')

    download_link=[]
    folder_path = 'D://PaCong/'

    for pic_tag in Soup.find_all('img'):
        pic_link = pic_tag.get('src')
        #print(pic_link)
        download_link.append('http:'+pic_link)

    for item in download_link:
        urllib.request.urlretrieve(item,folder_path+item[-10:])
        print('Done')

