from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time


keyWord=input("검색할 뉴스 키워드를 주세요 :")
baseUrl=f"https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query={keyWord}"

driver=webdriver.Chrome()
# driver1=webdriver.Chrome()
# driver2=webdriver.Chrome()
# driver3=webdriver.Chrome()
# driver4=webdriver.Chrome()
driver.get(baseUrl)
# time.sleep(60)
html=driver.page_source
soup=BeautifulSoup(html,"html.parser")

a=soup.find_all(class_="news_tit")

urlList=[]

for li in a:
    urlList.append(li["href"])
    # print(li["href"])
    # print(li)
    # print()
    # print()
# print(urlList)
# for web in urlList:
#     driver.get(web)
#     time.sleep(5)

driver.execute_script(f"window.open('{urlList[0]}');")
driver.execute_script(f"window.open('{urlList[1]}');")
driver.execute_script(f"window.open('{urlList[2]}');")
driver.execute_script(f"window.open('{urlList[3]}');")
driver.execute_script(f"window.open('{urlList[4]}');")
driver.execute_script(f"window.open('{urlList[5]}');")
taps=driver.window_handles
for tap in taps:
    driver.switch_to.window(tap)
    time.sleep(2)
# driver1.get(urlList[1])

# driver2.get(urlList[3])
# driver3.get(urlList[4])
# driver4.get(urlList[5])                    
# driver1.get(urlList[0])
time.sleep(30)
print(urlList[3])