from selenium import webdriver
from bs4 import BeautifulSoup
import requests

baseURL="https://www.naver.com"
driver=webdriver.Chrome()
driver.get(baseURL)
soure=driver.page_source
soup=BeautifulSoup(soure,"html.parser")



ui=soup.findAll(class_="shortcut_item")
# print(ui)
barList=[]
names=soup.findAll(class_="service_name")
urlList=[]
for url in ui:
    
    link=url.find(class_="link_service")
    
    urlLink=link["href"]
    if "veta" in urlLink:
        continue
    urlList.append(urlLink)
    
print(urlList)

for name in names:
    # if name in "veta":
    #     continue
    print(name.text)
    