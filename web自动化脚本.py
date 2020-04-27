#!/user/bin/python
#!-*- coding:utf-8 -*-
# from selenium import webdriver
# from time import sleep
# dr = webdriver.Firefox()
# dr.get('https://qzone.qq.com/')
# dr.switch_to.frame('login_frame')
# sleep(2.0)
# dr.find_element_by_css_selector('#switcher_plogin').click()
# sleep(2.0)
# dr.find_element_by_id('u').send_keys('602022965')
# sleep(2.0)
# dr.find_element_by_id('p').send_keys('13137246872qwe')
# sleep(2.0)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
# QQ空间登陆
# from selenium import  webdriver
# from time import sleep
# class qz():
#     def __init__(self):
#         self.dr = webdriver.Firefox()
#         self.dr.get('https://qzone.qq.com/')
#         self.dr.switch_to.frame('login_frame')
#     def join(self):
#         self.dr.find_element_by_css_selector('#switcher_plogin').click()
#         self.dr.find_element_by_id('u').send_keys('602022965')
#         self.dr.find_element_by_id('p').send_keys('13137246872qwe')
#         sleep(5.0)
#         self.dr.find_element_by_xpath('//*[@id="login_button"]').click()
# if __name__ == '__main__':
#     run = qz()
#     run.join()
# from selenium import webdriver
# from time import sleep
# class qq():
#     def __init__(self):
#         self.dr = webdriver.Firefox()
#         self.dr.get('https://qzone.qq.com')
#         # # 切换到框架上id或name
#         # # 先定位到框架
# 退出框架(退出到最初的网页)
#         self.dr.switch_to.default_content()
#         # ww = self.dr.find_element_by_xpath('')
#         # self.dr.switch_to.frame(ww)
#         self.dr.switch_to.frame('login_frame')
#     def join(self):
#         self.dr.find_element_by_xpath('//*[@id="img_out_602022965"]').click()
#         # self.dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
#         # sleep(3.0)
#         # self.dr.find_element_by_xpath('//*[@id="u"]').send_keys('602022965')
#         # sleep(3.0)
#         # self.dr.find_element_by_id('p').send_keys('13137246872qwe')
#         # sleep(5.0)
#         # self.dr.find_element_by_xpath('//*[@id="login_button"]').click()
#         sleep(10.0)
#         self.dr.switch_to.default_content()
#         self.dr.find_element_by_xpath('//*[@id="tb_logout"]').click()
#         sleep(5)
#         we = self.dr.switch_to_alert()
#         print(we.text)
#         # 点击确定
#         we.accept()
# if __name__ == '__main__':
#     run = qq()
#     run.join()
# from selenium import webdriver
# from time import sleep
# dr = webdriver.Firefox()
# dr.get('file:///C:/Users/zls/Desktop/abc.html')
# sleep(5.0)
# dr.find_element_by_xpath('/html/body/input').click()
# 将你的鼠标切换到弹出框
# we = dr.switch_to_alert()
# sleep(5.0)
# 获取文本
# print(we.text)
# 弹出框输入
# we.send_keys('你好')
# 点击确定
# we.accept()
# 点击取消
# we.dismiss()
# from selenium import webdriver
# from time import sleep
# class qq():
#     def __init__(self):
#         self.dr = webdriver.Firefox()
#         self.dr.get('https://mail.qq.com/cgi-bin/loginpage')
#         self.dr.switch_to.frame('login_frame')
#     def join(self):
#         self.dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
#         sleep(3.0)
#         self.dr.find_element_by_xpath('//*[@id="u"]').send_keys('602022965')
#         sleep(3.0)
#         self.dr.find_element_by_id('p').send_keys('13137246872qwe')
#         sleep(2.0)
#         self.dr.find_element_by_id('login_button').click()
#     def mail(self):
#         self.join()
#         sleep(10.0)
#         self.dr.switch_to.default_content()
#         sleep(10)
#         self.dr.find_element_by_xpath('//*[@id="composebtn"]').click()
#         sleep(5.0)
#         self.dr.switch_to.frame('mainFrame')
#         sleep(5.0)
#         self.dr.find_element_by_xpath("/html/body/form[2]/div[2]/div[3]/div[2]/table[2]/tbody/tr/td[2]/div[1]/div[2]/input").send_keys("674794275@qq.com")
# if __name__ == '__main__':
#     run = qq()
#     run.mail()
# from selenium import webdriver
# from time import sleep
# dr =  webdriver.Firefox()
# dr.get('https://www.douban.com')#1号的窗口
# sleep(2.0)
# # 句柄：唯一标识一个窗口的
# # 获取第一个窗口的标识（句柄）
# # print(dr.current_window_handle)
# # dr.find_element_by_xpath('/html/body/div[1]/div[1]/ul/li[1]/a').click()
# # sleep(2.0)
# # 获取所有的句柄
# # ww = dr.window_handles
# # print(ww)
# # sleep(2.0)
# # print(dr.title)
# # 切换窗口
# # 浏览器本身是无法决定什么什么时候打开一个窗口
# # 按照窗口打开的顺序给窗口标号--唯一标识这个窗口的字符串
# # dr.switch_to.window(ww[1])
# # print(dr.title)
# from selenium import webdriver
# from time import sleep
# class taobao():
#     def __init__(self):
#         self.dr = webdriver.Firefox()
#         self.dr.get('https://www.taobao.com/')
#     def jump(self):
#         sleep(2.0)
#         self.dr.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/div[2]/div[2]/div[1]/a[1]').click()
#         sleep(5)
#         ww = self.dr.window_handles
#         self.dr.switch_to.window(ww[1])
#         sleep(3.0)
#         self.dr.find_element_by_css_selector('.J_Quick2Static').click()
#     def join(self):
#         self.jump()
#         sleep(2.0)
#         self.dr.find_element_by_xpath('//*[@id="TPL_username_1"]').send_keys('15103819460')
#         sleep(2.0)
#         self.dr.find_element_by_xpath('//*[@id="TPL_password_1"]').send_keys('13137246872zls')
# #         sleep(2.0)
# #         self.dr.find_element_by_xpath('//*[@id="J_SubmitStatic"]').click()
# #         sleep(3.0)
# #         self.dr.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div[3]/form/ul/li/a[2]').click()
# #         sleep(20.0)
# #         for i in range(2):
# #             self.dr.find_element_by_xpath('/html/body/div[1]/div[1]/div/ul[2]/li[3]/div[1]/a/span[2]').click()
# #             sleep(5.0)
# #         self.dr.find_element_by_css_selector('#J_SiteNavHome > div:nth-child(1) > a:nth-child(1) > span:nth-child(1)').click()
# #         sleep(5.0)
# #     def search(self):
# #         self.join()
# #         self.dr.find_element_by_xpath('//*[@id="q"]').send_keys('短裤男')
# #         sleep(2.0)
# #         self.dr.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div[1]/div[2]/form/div[1]/button').click()
# #         sleep(5.0)
# #         self.dr.find_element_by_xpath('//*[@id="J_Itemlist_Pic_45262197965"]').click()
# #         sleep(5.0)
# #     def shopping(self):
# #         self.search()
# #         ww = self.dr.window_handles
# #         self.dr.switch_to.window(ww[2])
# #         sleep(5.0)
# #         self.dr.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[1]/div[1]/div/div[4]/div/div/dl[1]/dd/ul/li[11]/a').click()
# #         self.dr.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[1]/div[1]/div/div[4]/div/div/dl[2]/dd/ul/li[5]/a/span').click()
# #         sleep(5.0)
# #         self.dr.find_element_by_xpath('//*[@id="J_LinkBasket"]').click()
# # if __name__ == '__main__':
# #     run = taobao()
# #     run.shopping()
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# dr = webdriver.Chrome()
# dr.get('https://www.jd.com')
# sleep(5.0)
# ww = dr.find_element_by_xpath('//*[@id="J_cate"]/ul').find_elements_by_class_name('cate_menu_item')
# sleep(5.0)
# for i in ww:
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(3.0)
# aa = dr.find_elements_by_class_name('cate_menu_lk')
# sleep(2.0)
# for x in aa:
#     ActionChains(dr).move_to_element(x).perform()
#     sleep(2.0)
# for i in range(200,2000,100):
#     js="var q=document.documentElement.scrollTop={}".format(i)
#     dr.execute_script(js)
#     sleep(5.0)
# from selenium import  webdriver
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
# class jd():
#     def __init__(self):
#         self.dr = webdriver.Firefox()
#     def jump(self):
#         self.dr.get('https://www.jd.com')
#         self.dr.find_element_by_xpath('//*[@id="ttbar-login"]/a[1]').click()
#         sleep(2.0)
#         self.dr.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]/a').click()
#         sleep(2.0)
#         self.dr.find_element_by_xpath('//*[@id="loginname"]').send_keys('234567')
#         sleep(2.0)
#         self.dr.find_element_by_xpath('//*[@id="nloginpwd"]').send_keys('q12345678')
#         sleep(2.0)
#         self.dr.find_element_by_xpath('//*[@id="loginsubmit"]').click()
#     def huadong(self):
#         self.jump()
#         ww = self.dr.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div[3]')
#         ActionChains(self.dr).drag_and_drop_by_offset(ww, 40, 0).perform()
# if __name__ == '__main__':
# #     jd().huadong()
# # from selenium import webdriver
# # import selenium.webdriver.support.ui as ui
# # dr = webdriver.Firefox()
# # dr.get('https://www.jd.com')
# # # 智能休息
# # unit = ui.WebDriverWait(dr,10)
# # unit.until(lambda dr:dr.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div[3]/div/div/div[1]/a/div/img').is_displayed())
# # dr.find_element_by_xpath('//*[@id="ttbar-login"]/a[1]').click()
# # unit.until(lambda dr:dr)



#例如  time 模块
# from time import sleep
# #调用要这样写
# sleep(1.0)
# #也可以这样写
# import time
# #调用这样写
# time.sleep(1.0)     
# from selenium import webdriver
# url = 'http://www.baidu.com'
# dr = webdriver.Chrome()
# dr.get(url)



#等同于
# from selenium import webdriver
# url1 = "http://www.baidu.com"
# dr1 = webdriver.Firefox()
# dr1.get(url1)
# print(dr1.headers)
import requests
url = "https://s.beta.myapp.com/myapp/rdmexp/exp/file2/2020/01/16/comqinheispeak_3.6.2.01161_ca7fdba0-2389-5799-9818-524c7489adb9.apk"
re = requests.get(url)
print(re.headers['content-length'])