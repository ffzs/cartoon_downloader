import requests
from bs4 import BeautifulSoup
import os
import time
import execjs
import urllib
import random
import numpy as np

def mkdir(path):
    isExists = os.path.exists(path)
    if isExists:
        print("{}目录已存在".format(path))
    else:
        os.makedirs(path)
        print("{}目录创建".format(path))

def trans(name):
    node = execjs.get()
    file = 'trans.js'
    ctx = node.compile(open(file, encoding="utf-8").read())
    js = 'unsuan("{0}")'.format(name)
    return ctx.eval(js)

def img_download(url, path):
    urllib.request.urlretrieve(url, path)
    print(path + "已下载保存")

if __name__ == '__main__':
    cartoon_name = "一拳超人"
    interval = np.arange(1, 2, 0.1)
    base_url = 'http://www.hhcool.com'
    cartoon_id = '/manhua/15840.html'
    url = base_url + cartoon_id
    mkdir(cartoon_name)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    all_a = soup.find_all("a", class_='l_s')
    for i in range(135, 138):  #len(all_a)):138
        index = i
        href = all_a[index]['href']
        name = all_a[index].get_text()
        next_dir = cartoon_name + "/" + name
        mkdir(next_dir)
        next_url = "http://www.hhcool.com" + href + "&d=1"
        resp = requests.get(next_url)
        next_soup = BeautifulSoup(resp.text, 'lxml')
        all_page = next_soup.find('div', class_='cH1').find('b').get_text().split('/')[-1].strip()
        for j in range(0, int(all_page)):
            page_url = "/".join(next_url.split('/')[:-1]) + "/{}.".format(j+1) + next_url.split('.')[-1]
            print(page_url)
            page_resp = requests.get(page_url)
            page_soup = BeautifulSoup(page_resp.text, 'lxml')
            img_name = page_soup.find('div', class_='cBody').find('img')['name']
            img_url = 'http://124.94201314.net/dm06/'+trans(img_name)
            print(img_url)
            path = next_dir + '/{:0>3}.jpg'.format(j+1)
            img_download(img_url, path)
            time.sleep(random.choice(interval))


