from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

baseURL="https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/"

driver=webdriver.Chrome()
driver.get(baseURL)
# time.sleep(100)

idInputPlace = driver.find_element(By.ID, "id")

idInputPlace.send_keys("kjmwpoxy")

pwInputPlace = driver.find_element(By.ID, "pw")

pwInputPlace.send_keys("s")

pwInputPlace.send_keys(Keys.ENTER)
time.sleep(300)
print(idInputPlace)
# <selenium.webdriver.remote.webelement.WebElement (session="d77d356c78ec4ad4d113778446a0d8b1", element="f.27A3138C5E305256CB202C47FF7804AE.d.CDE1DFAEC56B0B3EBED33E0C3871D310.e.4")>