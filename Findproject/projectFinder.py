import requests
from bs4 import BeautifulSoup
import xlsxwriter

base_url = "http://www.scbid.com/zh/news/web_zbxx_17.shtml?a=2&b=0&page=1"
project_book = xlsxwriter.Workbook('projectBook.xlsx')
worksheet = project_book.add_worksheet('ProInfo')
worksheet.write('A1', '名称')
worksheet.write('B1', '城市')
worksheet.write('C1', '开始')
worksheet.write('D1', '结束')
worksheet.write('E1', '地址')
count = 2


source_code = requests.get(base_url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text,"html.parser")
for line in soup.select('#listzone span[class=line]'):
    TITLE = line.contents[0].get('title')
    worksheet.write('A' + str(count), TITLE)
    href = line.contents[0].get('href')
    URL = 'http://www.scbid.com/'+str(href)
    worksheet.write('E' + str(count), URL)
    CITY = line.contents[1].string
    worksheet.write('B' + str(count), CITY)
    S_TIME = line.contents[2].get('title')
    worksheet.write('C' + str(count), S_TIME)
    E_TIME = line.contents[3].get('title')
    worksheet.write('D' + str(count), E_TIME)
    print('wrinting {}'.format(count - 1))
    count += 1

project_book.close()