from selenium import webdriver
browser = webdriver.Chrome()
url='https://cn.pornhub.com/'
browser.get(url)
input_first=browser.find_element_by_xpath('//*[@id="searchInput"]')
input_first.send_keys('国产')
botton=browser.find_element_by_xpath('//*[@id="btnSearch"]')
botton.click()


'''
#写账号和密码
input_first=browser.find_element_by_xpath('//*[@id="login-user"]/input')
input_first.send_keys('417109030109')
input_first2=browser.find_element_by_xpath('//*[@id="login-pass"]/input')
input_first2.send_keys('YANG3041')

#读取到验证码
input_first3=browser.find_element_by_xpath('//*[@id="vchart"]')
tupian=input_first3.get_attribute('src')
browser1=webdriver.Chrome()
browser1.get(tupian)
#写入验证码

yzm=input("在这输入验证码")
input_first3.send_keys('yzm')
'''

