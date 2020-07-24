import time
import re
import os
import string
import shutil
from tkinter import filedialog

File = filedialog.askopenfilename(initialdir="D:/文档/Tex/论文笔记",title='Choose an txt.')
file = open(File,'r',encoding = 'utf-8')
number = input('please input number:')
#read the target *.ciw file
content = file.read()
file.close()
#os.remove(File)
#information dictionary
info = {}

#build the keywords list,updating...
keywords = ['0','0','AF','TI','PR','C1','SO','PY','KE','AB']
items = content.split('%')

for key,item in zip(keywords,items):
    print(key)
    print(item[2:])
    info[key] = item[2:]#前三个数据无效
#write

with open('n.template.tex','r',encoding = 'utf-8') as f:
    template = f.read()
try:
    template = template.replace('Title',info['TI'])
except Exception as e:
    print(e)
try:
    template = template.replace('Author',info['AF']+' '+info['PR'])
except Exception as e:
    print(e)
try:
    template = template.replace('institute',info['C1'].replace('&','\\&'))
except Exception as e:
    print(e)
try:
    template = template.replace('year',info['PY'])
except Exception as e:
    print(e)
try:
    template = template.replace('type',info['DT'])
except Exception as e:
    print(e)
try:
    template = template.replace('journal',info['SO'])
except Exception as e:
    print(e)
try:
    template = template.replace('abstract',info['AB'].replace('%','\\%'))
except Exception as e:
    print(e)
try:
    template = template.replace('tab:n.infomation',f'tab:{number}.infomation')
except Exception as e:
    print(e)
try:
    template = template.replace('tab:n.equipment',f'tab:{number}.equipment')
except Exception as e:
    print(e)
try:
    template = template.replace('tab:n.dataset',f'tab:{number}.dataset')
except Exception as e:
    print(e)
try:
    template = template.replace('tab:n.keywords',f'tab:{number}.keywords')
except Exception as e:
    print(e)

filename = str(number)+'.'+info['TI']

filename = filename.replace(':','')
filename = filename.strip()
os.mkdir(filename)
shutil.copy('readarticle.cls',filename)#将模板配置文件复制一份到新文件夹

os.chdir(filename)
with open(f'{number}.tex','w',encoding = 'utf-8') as f:
    f.write(template)
os.mkdir('images')



