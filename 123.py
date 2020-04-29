def appium_desired() -> object:   #注释作用
	print(123)
appium_desired
#-*- coding: UTF-8 -*-
from selenium import webdriver
import time
def login(driver,username,password):
    '''登录github'''
    #打开github首页
    driver.get("https://github.com/login")
    driver.implicitly_wait(10)
    #输入账号
    driver.find_element_by_id("login_field").send_keys(username)
    #输入密码
    driver.find_element_by_id("password").send_keys(password)
    #点击登录
    driver.find_element_by_name("commit").click()
def logout(driver):
    '''退出github'''
    #退出登录页面
    driver.find_element_by_css_selector('html body.logged-in.env-production.page-responsive.full-width div.position-relative.js-header-wrapper header.Header.py-lg-0.js-details-container.Details.flex-wrap.flex-lg-nowrap.p-responsive div.Header-item.position-relative.mr-0.d-none.d-lg-flex details.details-overlay.details-reset.js-feature-preview-indicator-container summary.Header-link').click()
    time.sleep(3)
    #点击sing out
    driver.find_element_by_xpath('/回头ml/body/div[1]/header/div[7]/details/details-menu/a[7]').click()
    driver.quit()
if __name__ == "__main__":
    driver=webdriver.Firefox()
    #调用登录
    login(driver,"youruser","yourpsw")
    print("Hello zhujiang00!")
    #调用退出
    logout(driver)