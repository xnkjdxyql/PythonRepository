"""
(1). %字符：标记转换说明符的开始
(2). 转换标志：-表示左对齐；+表示在转换值之前要加上正负号；“”（空白字符）表示正数之前保留空格；0表示转换值若位数不够则用0填充
(3). 最小字段宽度：转换后的字符串至少应该具有该值指定的宽度。如果是*，则宽度会从值元组中读出。
(4). 点(.)后跟精度值：如果转换的是实数，精度值就表示出现在小数点后的位数。如果转换的是字符串，那么该数字就表示最大字段宽度。如果是*，那么精度将从元组中读出
(5).字符串格式化转换类型
    转换类型          含义

    d,i               带符号的十进制整数
    o                 不带符号的八进制
    u                 不带符号的十进制
    x                 不带符号的十六进制（小写）
    X                 不带符号的十六进制（大写）
    e                 科学计数法表示的浮点数（小写）
    E                 科学计数法表示的浮点数（大写）
    f,F               十进制浮点数
    g                 如果指数大于-4或者小于精度值则和e相同，其他情况和f相同
    G                 如果指数大于-4或者小于精度值则和E相同，其他情况和F相同
    C                 单字符（接受整数或者单字符字符串）
    r                 字符串（使用repr转换任意python对象)
    s                 字符串（使用str转换任意python对象）

"""
# x=3.141592653
# print('%10.3f' % x)         #字段宽10，精度3,
# print('%010.3f' % x)        #字段宽10，精度3,使用0填充空白
# print('x=%.*f' % (3,x))     #用*从后面的元组中读取字段宽度或精度
# print("%-10.3f" % x)        #左对齐
# print('%+f' % x)            #显示正负号
#
#
# for i in range(1,10):
#     # print(i)             #默认输出一个值换一行
#     # print(i,end=' ')     #空格分给不换行
#     print(i,end='|')       #|分割不换行




# for i in range(1,1000):
#     print('%-5d' % i,end=' ')
#     if i%5==0:
#         print('')





# name1 = 'abcdefghe'
# name2 = 'abc'
# name3 = 'abcdef'
# print('%10s' % name1)
# print('%10s' % name2)
# print('%10s' % name3)
# print('%-10s' % name1)
# print('%-10s' % name2)
# print('%-10s' % name3)




"""
自python2.6开始，新增了一种格式化字符串的函数str.format()，可谓威力十足。那么，他跟之前的%型格式化字符串相比，有什么优越的存在呢？
"""


# print('{:>8}'.format('189'))      #对齐
# print('{:<8}'.format('189'))
# print('{:0>8}'.format('189'))
# print('{:a<8}'.format('189'))
# print('{:*>8}'.format('189'))



# print("{:.2f}".format(3.1415926))  #精度

# import sys
#
# std_output = sys.__stdout__
# f_result=open('result.txt', 'w')
# sys.stdout=f_result
# print('print to file')
# print('show in file')
# sys.__stdout__=std_output
# print('show on console')





# import re
# from bs4 import BeautifulSoup
# import requests
# import urllib.request
# url = 'http://bbs.tianya.cn/post-no04-2513621-1.shtml'
# headers= {
# 'Accept':':text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
# 'Referer':'http://bbs.tianya.cn/post-no04-2513621-1.shtml',
# 'Cookie':'__cfduid=d8e76eea38149cc8fcc7f0f8b9d78eda81509847308; ADVC=35a81d341ae5b0; ASL=17480,0000q,8bcd9e9b; tianya1=123868,1510301714,1,86400; AJSTAT_ok_pages=4; AJSTAT_ok_times=3; time=ct=1510709219.945',
# 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
#
# }
# raw_page = requests.post(url,headers=headers)
# soup = BeautifulSoup(raw_page.text, 'html.parser')
# #
# # img3.laibafile.cn/p/m/175358482.jpg
# # img3.laibafile.cn/p/m/175358691.jpg
#
#
# img_list = soup.find_all('img')
# for img in img_list:
#     img_url = img.get('original')
#     if(img_url != None):
#         img_name = img_url[-10:]
#         img_path = 'pictures/' + img_name
#         # 下载下来的全都是：该图片仅供天涯用户分享
#         urllib.request.urlretrieve(img_url, img_path)
#         print('downloading img {}'.format(img_name))




from bs4 import BeautifulSoup
import requests,re
a = requests.session()
url = 'http://bbs.tianya.cn/post-no04-2513621-1.shtml'
b = a.get(url)
c = BeautifulSoup(b.content,'html.parser')
header = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;0.8',
          'Referer':'%s' % url,
          'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)rome/41.0.2272.101 Safari/537.36',
         }
n = 1
for i in c.find_all(original = re.compile("^.*?\.jpg")):
    tmp = i['original']
    d = requests.session()
    e = d.get(tmp,headers=header)
    f = open('pictures/'+str(n)+'.jpg','wb')
    f.write(e.content)
    print('downloading picture {}'.format(n))
    f.close()
    n+=1