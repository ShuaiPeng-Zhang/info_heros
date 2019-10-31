import requests
from tkinter import *
from tkinter import messagebox
import re
import json

#获取英雄id
def getLOLImages():
    pic_list = []
    url_js = 'http://lol.qq.com/biz/hero/champion.js'
    html = requests.get(url_js).text
    req = r'"keys":(.*?),"data"'
    list_js = re.findall(req,html)
    # print(list_js[0])
    dict_js = json.loads(list_js[0])
    # print(dict_js)

    # 拼接url
    for hero_id in dict_js:
        # print(hero_id)
        #http://ossweb-img.qq.com/images/lol/web201310/skin/big222002.jpg
        for i in range(20):
            i = str(i)
            if len(i) == 1:
                hero_num = '00' + i
            elif len(i) == 2:
                hero_num = '0' + i
            numstr = hero_id + hero_num
            # print(numstr)
            url = 'http://ossweb-img.qq.com/images/lol/web201310/skin/big'+numstr+'.jpg'
            # print(url)
            pic_list.append(url)
    # print(pic_list)
    list_filepath = []
    path = r'C:\Users\17710\Desktop\info_heros\LOLPic\\'
    # 获取下载图片名称
    for name in dict_js.values():
        # print(name)
        for i in range(20):
            file_path = path + name + str(i) + '.jpg'
            list_filepath.append(file_path)
    # print(list_filepath)

    n=0
    for picurl in pic_list:
        res = requests.get(picurl)
        n+=1
        # print(res)
        # 下载图片
        if res.status_code == 200:
            print('正在下载%s'%list_filepath[n])
            f = open(list_filepath[n],'wb')
            f.write(res.content)
            f.close()


getLOLImages()

