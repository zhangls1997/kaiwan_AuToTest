#!/user/bin/python
#!-*- coding:utf-8 -*-
# import requests
# import re
# a='https://www.qiushibaike.com/text/page/{}/'.format(1)
# oo={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
# }
# b=requests.get(a,headers=oo)
# c = b.content.decode('utf-8')
# d=re.compile('<div class="content">(.*?)</span>',re.S)
# dd = re.compile("<h2>(.*?)</h2>",re.S)
# f=d.findall(c)
# ffc = dd.findall(c)
# for i in ffc:
#      i=i.replace("\n","")
#      aa = i.strip()
# import requests
# import re
# import xlwt
# for k in range(2):
#  a = 'https://www.qiushibaike.com/text/page/{}/'.format(k)
#  oo={
#     'User - Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64;rv: 65.0) Gecko/20100101Firefox/65.0'
#  }    #发送请求
#  b=requests.get(a,headers=oo)
#  c=b.content.decode('utf-8')
#  zz=re.compile('<h2>(.*?)</h2>',re.S)
#  aa=zz.findall(c)
#  ff = []  # print(b.content.decode('utf-8'))#(网页源代码
#  qq = []
#  d=re.compile('<div class="content">(.*?)</span>',re.S)
#  f=d.findall(c)
#  for j in aa:
#      j=j.replace('\n','')
#      qq.append(j)
#  for i in  f:
#     i=i.replace('<span>','')
#     i=i.strip()
#     i=i.replace('<br/>','')
#     ff.append(i)
#  for x in range(len(ff)) :
#      ff.insert(x*2,qq[x])
#  with open('b.txt','a',encoding='utf-8') as g:
#     for i in ff:
#         g.write(i+'\n''\n')
# with open('b.txt','r',encoding='utf-8') as f:
#  c=f.readlines()
# ff=xlwt.Workbook(encoding='utf-8')
# sheet=ff.add_sheet('文件')
# for i in range(len(c)):
#     k=c[i].split('\n')
#     for j in range(len(k)):
#        sheet.write(i,j,k[j] )
# ff.save('b.xls')
# import requests
# import re
# for i in range(1,5):
#     a='0100/?query=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&page=1&ka=page-next'.format(i)
#     oo={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
# }
#     b=requests.get(a,headers=oo)
#     c = b.content.decode('utf-8')
#     d=re.compile('<div class="job-title">(.*?)</div>',re.S)
#     f=d.findall(c)
#     ff=[]
#     for i in f:
#         i=i.replace('<span>','')
#         i=i.strip()
#         i=i.replace('<br/>','')
#         i=i.replace("\n","")
#         ff.append(i)
#     with open('c.txt','a',encoding='utf-8') as g:
#         for i in ff:
# import re
# import requests
#
#
# class 图片(object):
#     def 发送请求(self, page):
#         url = "https://www.qiushibaike.com/imgrank/page/{}/".format(page)
#         head = {'User - Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64;rv: 65.0) Gecko/20100101Firefox/66.0'}
#         res = requests.get(url, headers=head)
#         html = res.content.decode("utf-8")
#         return html
#
#     def 过滤(self, abc):
#         lianjie = []
#         patt = re.compile(r'<div class="thumb">(.*?)</a>', re.S)
#         items = patt.findall(abc)
#         for i in items:
#             new_a = re.compile(r'<img src="(.*?)"')
#             aaa = new_a.findall(i)
#             lianjie.append(aaa[0])
#             for j in lianjie:
#                 qwe.append(j)
#         return lianjie
#
#     def 保存(self, shu):
#         global a
#         for i in shu:
#             res = requests.get("https:" + i)
#             qq = res.content
#             with open("{}.jpg".format(a), "wb") as f:
#                 f.write(qq)
#             a = a + 1
#
#
# tu = 图片()
# a = 0
# for i in range(1, 6):
#     abc = tu.发送请求(i)
#     sh = tu.过滤(abc)
#     tu.保存(sh)
#             g.write(i+'\n')
# import time
# a=input('请输入年份:')
# a = a.split(" ")
# b = []
# for i in a:
#     b.append(int(i))
# c = time.strptime("{} {} {}".format(b[0],b[1],b[2]),"%Y %m %d")
# d = time.mktime(c)-86400
# f = time.localtime(d)
# print(f[0],f[1],f[2])
# import time
# a=input('请输入年 月 日:')
# b=a.split(' ')
# c=[]
# for i in b:
#     c.append(int(i))
# if c[0]%4==0:
#     if c[0]%100==0:
#         if c[0]%400==0:
#             print('yes')
#         else:
#             print('no')
#     else:
#         print('yes')
# else:
#     print('no')
#
# k=time.strptime('{} {} {}'.format(c[0],c[1],c[2]),'%Y %m %d' )
# print('星期{}'.format(k[-3]+1))
# print('一年中的第{}'.format(k[-2]))
# import requests
# import re
# class 豆瓣(object):
#     def 发送请求(self,page):
#         url = "https://movie.douban.com/top250?start={}&filter=".format(page)
#         head = {'User - Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64;rv: 65.0) Gecko/20100101Firefox/66.0'}
#         res = requests.get(url, headers=head)
#         html = res.content.decode("utf-8")
#         return html
#     def 过滤(self,a):
#         patt = re.compile(r'<img width="100" alt="(.*?)"', re.S)
#         items = patt.findall(a)
#         aa = re.compile(r'src="(.*?)" class="">')
#         item = aa.findall(a)
#         cc =dict(zip(items,item))
#         return cc
#     def 保存(self,shu):
#         for i,j in shu.items():
#             res = requests.get(j)
#             qq = res.content
#             with open('{}.jpg'.format(i),'ab') as f:
#                 f.write(qq)
# qwe = 豆瓣()
# for i in range(0,125,25):
#     a = qwe.发送请求(i)
#     aa=qwe.过滤(a)
#     qwe.保存(aa)
# import requests
# import re
# import xlwt
# import xlrd
# from xlutils.copy import copy
# class douban(object):
#     def song(self,page):
#         url = "https://movie.douban.com/top250?start={}&filter=".format(page)
#         head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}
#         res = requests.get(url,headers=head)
#         html = res.content.decode("utf-8")
#         return html
#     def guo(self,aa):
#         patt = re.compile(r'<img width="100" alt="(.*?)"',re.S)
#         items = patt.findall(aa)
#         pat = re.compile(r'导演:(.*?)&nbsp;&nbsp;',re.S)
#         item = pat.findall(aa)
#         pa = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>', re.S)
#         ite = pa.findall(aa)
#         pp = re.compile(r'<span>(.*?)评价</span>')
#         it = pp.findall(aa)
#         return items,item,ite,it
#     def save(self,q,w,e,r):
#         try:
#             ff =  xlrd.open_workbook("a.xls")
#             sheet1 = ff.sheets()[0]
#             num = sheet1.nrows
#             new = copy(ff)
#             sheet = new.get_sheet(0)
#             for x,y in enumerate(q):
#                 sheet.write(num+x,0,y)
#                 sheet.write(num+x,1,w[x])
#                 sheet.write(num+x,2,e[x])
#                 sheet.write(num+x,3,r[x])
#             new.save("a.xls")
#         except:
#             ff=xlwt.Workbook()
#             sheet = ff.add_sheet("123")
#             sheet.write(0,0,"电影名")
#             sheet.write(0,1,"导演")
#             sheet.write(0,2,"评分")
#             sheet.write(0,3,"评价")
#             for i,j in enumerate(a):
#                 sheet.write(i+1,0,j)
#                 sheet.write(i+1,1,w[i])
#                 sheet.write(i+1,2,e[i])
#                 sheet.write(i+1,3,r[i])
#             ff.save("a.xls")
# for i in range(0,125,25):
#     qwe =douban()
#     qw=qwe.song(i)
#     a,b,c,d=qwe.guo(qw)
#     qwe.save(a,b,c,d)
# import mysql.connector
# mydb = mysql.connector.connect(
#     host="192.168.1.11",  # 数据库主机地址
#     user="root",  # 数据库用户名
#     passwd="123456"  # 数据库密码
# )
# print(mydb)
# import requests
# import json
# import xlwt
# url = 'https://www.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=12&city=410200&geoobj=114.204118|34.754749|114.588639|34.844963&keywords=洗浴中心'
# head=({'User - Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64;rv: 65.0) Gecko/20100101Firefox/66.0'})
# res = requests.get(url,headers=head)
# qwe = res.text
# abc = json.loads(qwe)
# print(abc)
# b = []
# c = []
# for i in range(0,20):
#     b.append(asd['data']['poi_list'][i]['address'])
#     c.append(asd['data']['poi_list'][i]['disp_name'])
# f = xlwt.Workbook(encoding='utf-8')
# sheet = f.add_sheet('123')
# sheet.write(0,0,'地点')
# sheet.write(0,1,'洗浴中心名字')
# for m,n in enumerate(b):
# 	sheet.write(m+1,0,n)
# 	sheet.write(m+1,1,c[m])
# f.save('a.xls')
# import pymysql
# mydb = pymysql.connect(
#     host="192.168.1.10",  # 数据库主机地址
#     user="root",  # 数据库用户名
#     passwd='123456'  # 数据库密码
# )
# while True:
#     a = input("请输入一条sql语句：")
#     import pymysql
#     mysql = pymysql.connect(host='192.168.1.10',port=3306,user='root',password='123456')
#     qwe = mysql.cursor()
#     if a == 'exit':
#         mysql.close()
#         break
#     else:
#         qwe.execute(a)
#         b = qwe.fetchall()
#         print(b)
# import requests
# import json
# class mysql(object):
#     def send(self):
#         url = 'https://www.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=12&city=410200&geoobj=114.204118%7C34.722445%7C114.58864%7C34.877219&keywords=%E6%B4%97%E6%B5%B4%E4%B8%AD%E5%BF%83'
#         head = {'User - Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64;rv: 65.0) Gecko/20100101Firefox/66.0'}
#         res = requests.get(url,headers=head)
#         qwe = res.text
#         abc = json.loads(qwe)
#         return abc
#     def guo(self,shuju):
#         print(shuju)
# qwe = mysql()
# abc = qwe.send()
# qwe.guo(abc)

