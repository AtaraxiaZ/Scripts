from selenium import webdriver
from time import sleep

url_mail = 'https://hw.mail.163.com/'

browser = webdriver.Chrome()
browser.maximize_window()

browser.get(url_mail)

iframe = browser.find_elements_by_tag_name("iframe")[0]
browser.switch_to.frame(iframe)

mail_login = browser.find_element_by_name('email')
mail_login.send_keys('bhenpf61ni62')
mail_passwd = browser.find_element_by_name('password')
mail_passwd.send_keys('w3318bfprl')
browser.find_element_by_id('dologin').click()
repeat = True;
while repeat == True:
	try:
		browser.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div[3]/a[1]').click()
		repeat == False
	except:
		sleep(10)
		browser.find_element_by_id('dologin').click()
		repeat == True

browser.switch_to.default_content()  # 退出框架

#sleep(10)
#browser.quit()
