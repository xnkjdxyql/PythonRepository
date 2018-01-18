#-*- coding:utf-8 -*-
import re
import requests



def dowmloadPic(html,keyword):


    pic_url = re.findall('"objURL":"(.*?)",',html,re.S)
    i = 0
    print ('找到关键词:'+keyword+'的图片，现在开始下载图片...')
    for each in pic_url:
        print ('正在下载第'+str(i+1)+'张图片，图片地址:'+str(each))
        try:
            pic= requests.get(each, timeout=10)
        except requests.exceptions.ConnectionError:
            print ('【错误】当前图片无法下载')
            continue
            
        #需要手打在当前目录下创建文件夹pictures    
        string = 'pictures/'+keyword+'_'+str(i) + '.jpg'
        #strig is a jpg file,open it with the mode of write binary file
        fp = open(string,'wb')
        #write the picture into jpg file  http://www.jianshu.com/p/74b94eadae15
        fp.write(pic.content)
        fp.close()
        i += 1



if __name__ == '__main__':
    word = input("Input key word: ")
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+word+'&ct=201326592&v=flip'
    result = requests.get(url)
    dowmloadPic(result.text,word)

