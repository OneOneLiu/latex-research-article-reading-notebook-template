import time
import re
import os
import string
import shutil

number = input('please input number:')
#read the target *.ciw file
file = open('savedrecs.ciw','r')
content = file.read()
file.close()
os.remove('savedrecs.ciw')
#information dictionary
info = {}

#build the keywords list,updating...
keywords = ['FN','VR','PT','AU','AF','TI','SO','LA','DT','DE','ID','AB','C1','RP','EM','OI','FU','FX','NR','TC','Z9','U1','U2','PU','PI','PA','SN','J9','JI','PY','VL','BP','EP','DI','PG','WC','SC','GA','UT','OA','DA','ER','EF']

#start searching
scope = []
for each in keywords:
    scope.append(re.search(each+'\s',content))#add a \s to match the whitespace after each keyword
print(len(scope))
print(len(keywords))

#delete the Nones in scope
indexes = []
#firstly,find the index of these Nones
for i in range(len(scope)):
    if scope[i]  == None:
        print(i)
        print(scope[i])
        indexes.append(i)
#then,pick the No-None elements out and update the keywords and scope list
new_keywords = [keywords[i] for i in range(len(keywords)) if i not in indexes]
new_scope = [scope[i] for i in range(len(scope)) if i not in indexes]

keywords = new_keywords
scope = new_scope
print(len(scope))
print(len(keywords))

#then the next stratigy is to split content by every keywords
for num in range(len(scope)-1):#here you must minus one to keep the last one+1 not bigger than len(scope)
    info[keywords[num]] = content[scope[num].span()[1]:scope[num+1].span()[0]-1].replace('\n','').replace('   ',' ').replace(' ',' ')#delete '\n'

#对一些难搞的信息加工一下
#institute
try:
    temp = info['C1']
    result = re.findall('](.+?)\.',temp)
    info['C1'] = result[0]
except Exception as e:
    print(e)

#write

with open('n.template.tex','r',encoding = 'utf-8') as f:
    template = f.read()
try:
    template = template.replace('Title',info['TI'])
except Exception as e:
    print(e)
try:
    template = template.replace('Author',info['AF'])
except Exception as e:
    print(e)
try:
    template = template.replace('institute',info['C1'].replace('&','\\&'))
except Exception as e:
    print(e)
try:
    template = template.replace('email',info['EM'])
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
    template = template.replace('DI',info['DI'])
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
os.mkdir(filename)
shutil.copy('readarticle.cls',filename)#将模板配置文件复制一份到新文件夹

os.chdir(filename)
with open(f'{number}.tex','w',encoding = 'utf-8') as f:
    f.write(template)
os.mkdir('images')


