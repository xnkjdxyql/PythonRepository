import requests
from bs4 import BeautifulSoup
import xlsxwriter

#四川招投标网
#货物类
cargo_base_url = "http://www.scbid.com/zh/news/web_zbxx_17.shtml?a=2&b=0&page="

#服务类
service_base_url = "http://www.scbid.com/zh/news/web_zbxx_18.shtml?a=2&b=0&page="

#工程类
project_base_url = "http://www.scbid.com/zh/news/web_zbxx_19.shtml?a=2&b=0&page="
scbid = xlsxwriter.Workbook('SCBidInfo.xlsx')
servicesheet = scbid.add_worksheet('ServiceInfo')
cargosheet = scbid.add_worksheet('CargoInfo')
projectsheet = scbid.add_worksheet('ProjectInfo')
servicesheet.write('A1', '名称')
servicesheet.write('B1', '城市')
servicesheet.write('C1', '开始')
servicesheet.write('D1', '结束')
servicesheet.write('E1', '地址')
cargosheet.write('A1', '名称')
cargosheet.write('B1', '城市')
cargosheet.write('C1', '开始')
cargosheet.write('D1', '结束')
cargosheet.write('E1', '地址')
projectsheet.write('A1', '名称')
projectsheet.write('B1', '城市')
projectsheet.write('C1', '开始')
projectsheet.write('D1', '结束')
projectsheet.write('E1', '地址')
count_s = 2
count_c = 2
count_p = 2

for i in range(50):
    service_url = service_base_url + str(i)
    cargo_url = cargo_base_url + str(i)
    project_url = project_base_url +str(i)
    service_source_code = requests.get(service_url)
    plain_text = service_source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for line in soup.select('#listzone span[class=line]'):
        TITLE = line.contents[0].get('title')
        servicesheet.write('A' + str(count_s), TITLE)
        href = line.contents[0].get('href')
        URL = 'http://www.scbid.com' + str(href)
        servicesheet.write('E' + str(count_s), URL)
        CITY = line.contents[1].string
        servicesheet.write('B' + str(count_s), CITY)
        S_TIME = line.contents[2].get('title')
        servicesheet.write('C' + str(count_s), S_TIME)
        E_TIME = line.contents[3].get('title')
        servicesheet.write('D' + str(count_s), E_TIME)
        print('wrinting {}'.format(count_s - 1))
        count_s += 1
    print('SERVICE PAGE {} DownLoad Finished'.format(i))
    cargo_source_code = requests.get(cargo_url)
    plain_text = cargo_source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for line in soup.select('#listzone span[class=line]'):
        TITLE = line.contents[0].get('title')
        cargosheet.write('A' + str(count_c), TITLE)
        href = line.contents[0].get('href')
        URL = 'http://www.scbid.com' + str(href)
        cargosheet.write('E' + str(count_c), URL)
        CITY = line.contents[1].string
        cargosheet.write('B' + str(count_c), CITY)
        S_TIME = line.contents[2].get('title')
        cargosheet.write('C' + str(count_c), S_TIME)
        E_TIME = line.contents[3].get('title')
        cargosheet.write('D' + str(count_c), E_TIME)
        print('wrinting {}'.format(count_c - 1))
        count_c += 1
    print('CARGO PAGE {} DownLoad Finished'.format(i))
    project_source_code = requests.get(project_url)
    plain_text = project_source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for line in soup.select('#listzone span[class=line]'):
        TITLE = line.contents[0].get('title')
        projectsheet.write('A' + str(count_p), TITLE)
        href = line.contents[0].get('href')
        URL = 'http://www.scbid.com' + str(href)
        projectsheet.write('E' + str(count_p), URL)
        CITY = line.contents[1].string
        projectsheet.write('B' + str(count_p), CITY)
        S_TIME = line.contents[2].get('title')
        projectsheet.write('C' + str(count_p), S_TIME)
        E_TIME = line.contents[3].get('title')
        projectsheet.write('D' + str(count_p), E_TIME)
        print('wrinting {}'.format(count_p - 1))
        count_p += 1
    print('PROJECT PAGE {} DownLoad Finished'.format(i))
scbid.close()
