from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd
import string
import random

#生成随机用户名
def random_sentence(size):
    char_lists = string.ascii_lowercase + string.digits
    return ''.join(random.choice(char_lists) for _ in range(size))

url_login = 'https://pomotodo.com/account/signin'
url_sign_up = 'https://pomotodo.com/account/signup'
mail = pd.read_table('163mail.txt',sep = '----',names = ['user','password'], engine = 'python')  #引擎用python可以解析更丰富的数据，不会报warning


browser = webdriver.Chrome()
browser.maximize_window()
wait = WebDriverWait(browser, 30)


n = mail.shape[0] #返回行数
#下面是注册的代码
while(n > 0):
	try:
		browser.get(url_login)

		email_form = browser.find_element_by_id('js-email')
		#email_form.click()	#点击邮箱输入框
		email_form.clear()	#清空输入框
		email_form.send_keys(mail.user[n-1])

		passwd_form = browser.find_element_by_name('password')
		passwd_form.clear()
		passwd_form.send_keys(mail.password[n-1])

		browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/form/div[3]/button').click()

		sleep(5)

		browser.find_element_by_xpath('//*[@id="js-upgrade-pro-btn"]/a').click()
		sleep(5)
		handles = browser.window_handles
		browser.switch_to.window(handles[1])

		browser.find_element_by_xpath('/html/body/div[1]/div/ul/li/a').click()
		coupon = browser.find_element_by_xpath('//*[@id="coupon_code"]')
		coupon.send_keys('X47DFI7I')
		sleep(5)
		browser.find_element_by_xpath('//*[@id="use_coupon"]').click()
		sleep(5)
		n -= 1
		browser.quit()
		browser = webdriver.Chrome()
		browser.maximize_window()
	except:
		pass

#browser.find_element_by_id('js-username-angular').click()
#browser.find_element_by_xpath('/html/body/header/ul/li[3]/ul/li[1]/a').click()


sleep(20)
browser.quit()