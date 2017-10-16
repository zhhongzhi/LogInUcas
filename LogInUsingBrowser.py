# -*- encoding: utf-8 -*-
from selenium import webdriver
import time

user_name = u"20XXXX"  # 你的账号
password = u"*****"    # 你的密码
browser = webdriver.Firefox()
url = 'http://210.77.16.21/eportal/index.jsp?wlanuserip=0bc386d9e643d188b011a0d00c9b5c40&wlanacname=5fcbc245a7ffdfa4&ssid=&nasip=2c0716b583c8ac3cbd7567a84cfde5a8&mac=53ba540bde596b811a6d5617a86fa028&t=wireless-v2&url=2c0328164651e2b4f13b933ddf36628bea622dedcc302b30'
browser.get(url)
time.sleep(5)

browser.find_element_by_id("username").send_keys(user_name)
browser.find_element_by_id("pwd_tip").send_keys(pasaword)

browser.find_element_by_id("SLoginBtn_1").click()

time.sleep(5)
browser.close()
browser.quit()
