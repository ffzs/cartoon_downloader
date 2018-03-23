#coding=utf-8
from urllib import request
import urllib
import execjs

# print(execjs.get().name)

node = execjs.get()
name = 'yexoooxopexytxqqxoooxopqxoptxqqxywxyqxyexyqxyextoxtoxtpxyqxtoxyexqexqqxoorxqtxywxywxtoxyexoiixqtxywxywxywxtexqtxtrxyqxyqxtrxtoxyrxeyxwpxeopoiuytrewqxxwixwpuiqxopyxoyrwqwqwxw'
file = 'trans.js'
ctx = node.compile(open(file, encoding="utf-8").read())
js = 'unsuan("{0}")'.format(name)
params = ctx.eval(js)
url = 'http://165.94201314.net/dm01/'+params
urllib.request.urlretrieve(url, '1.jpg')
print(url)