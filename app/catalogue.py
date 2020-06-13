# #!/user/bin/python
# #!-*- coding:utf-8 -*-
# # import requests
# # import time
# # import os
# # def downloadFile(name,url):
# #     headers = {'Proxy-Connection': 'keep-alive'}
# #     r = requests.get(url, stream=True, headers=headers)
# #     length = float(r.headers['content-length'])
# #     ishow_package = os.getcwd()  # 获取当前的路径
# #     if ishow_package != "E:\is_appium\app":
# #         os.chdir(r"E:\is_appium\app")
# #         ishow_list = os.listdir('.')
# #     if "ishow.apk" in ishow_list:  # 判断apk包是否存在当前目录
# #         os.remove(ishow_list[0])
# #         new_ishow_list = os.listdir('.')
# #     if "ishow.apk" not in new_ishow_list:
# #         with open(r"E:\is_appium\app\ishow.apk", "wb") as ishow_package:
# #             count = 0
# #             count_tmp = 0
# #             time1 = time.time()
# #             for chunk in r.iter_content(chunk_size=512):
# #                 if chunk:
# #                     ishow_package.write(chunk)
# #                     count += len(chunk)
# #                     if time.time() - time1 > 2:
# #                         p = count / length * 100
# #                         speed = (count - count_tmp) / 1024 / 1024 / 2
# #                         count_tmp = count
# #                         print(name + ': ' + formatFloat(p) + '%' + ' Speed: ' + formatFloat(speed) + 'M/S')
# #                         time1 = time.time()
# #             ishow_package.close()
# # def formatFloat(num):
# #     return '{:.2f}'.format(num)
# # if __name__ == '__main__':
# #     get_url = "https://s.beta.myapp.com/myapp/rdmexp/exp/file2/2020/01/16/comqinheispeak_3.6.2.01161_ca7fdba0-2389-5799-9818-524c7489adb9.apk"
# #     downloadFile('ishow.apk', get_url)
# # print(40103+29999+9839+5005+4978+5054+4943+79)
# # def f(x,l=[]):
# #     for i in range(x):
# #         l.append(i*i)
# #     print(l)
# # f(2)
# # f(3,[3,2,1])
# # f(3)
# # def f2(arg1,arg2,*args,**kwargs):
# #     print(arg1,arg2,args,kwargs)
# # l = [1,2,3]
# # t = (4,5,6)
# # d = {'a':7,'b':8,'c':9}
# # f2(1,2,3)
# # f2(1,2,3,"groovy")
# # f2(arg1=1,arg2=2,c=3)
# # f2(arg1=1,arg2=2,c=3,zzz="hi")
# # f2(1,2,3,a=1,b=2,c=3)

# # f2(*l,**d)
# # f2(*t,**d)
# # f2(1,2,*t)
# # f2(1,1,q='winning',**d)
# # f2(1,2,*t,q='winning',**d)
# import pysnooper
# @pysnooper.snoop()
# def number_to_bits(number):
#     if number:
#         bits = []
#         while number:
#             number, remainder = divmod(number, 2)
#             bits.insert(0, remainder)
#         return bits
#     else:
#         return [0]
 
# # @pysnooper.snoop('F:/GitRepository/Python/PySnooper-Test/logs/file.log', prefix='ZZZ || ')
# # def number_to_bits2(number):
# #     if number:
# #         bits = []
# #         while number:
# #             number, remainder = divmod(number, 2)
# #             bits.insert(0, remainder)
# #         return bits
# #     else:
# #         return [0]
 
# number_to_bits(6)
# # number_to_bits2(8)
import sys  
from PyQt5.QtWidgets import QWidget, QApplication  
  
if __name__ == '__main__':  
    app = QApplication(sys.argv)  
    w = QWidget()  
    w.show()  
    w.setWindowTitle("Hello PyQt5")  
    sys.exit(app.exec_())  