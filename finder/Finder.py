import requests
from bs4 import BeautifulSoup

url = 'http://www.okcis.cn/r/s/bn_mf/keystr-/citystr-/timezb-3/searchList-list/' \
      'search_column-bn_mf/appear-content/searchTrue-auto/page-1/pagecount-29893/pagecount-29893/page-1'
# url = 'http://www.scbid.com/zh/news/web_zbxx_17.shtml'

source_code = requests.get(url)
print(url)