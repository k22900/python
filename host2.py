
from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup



# # while True:     
# #     time.sleep(30)
# # "p.MyView-module__login_text___G0Dzv"


# # response=requests.get("https://section.cafe.naver.com/ca-fe/home")
# # html=response.text
# # print(html)
# # soup=BeautifulSoup(html, "html.parser")
# # result=soup.select_one("title").text
# # print(result)

# driver=webdriver.Chrome()   
# driver.get("https://section.cafe.naver.com/ca-fe/home")
# html=driver.page_source
# soup=BeautifulSoup(html,"html.parser")
# result=soup.select_one("title").text
# # result=driver.find_elements("title")
# print(html)
# print(result)



# # driver.quit()



# # from word import word


# w="Asde"
# word=w.lower()
# print(word)




baseURL="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query="

keyWord=input("검색 :")

search=baseURL+keyWord

driver=webdriver.Chrome()
driver.get(search)
html=driver.page_source
soup=BeautifulSoup(html,"html.parser")

# h1=soup.find('h1')
# print(h1)
# a= h1.find('a')

# print(a['href'])

h1=soup.select_one('h1')
# print(h1)
a=h1.select_one('a')
print(a['href'])

h1=soup.select_one('.logo')
# print(h1)
a=h1.select_one('.link')
print(a['href'])

h1=soup.find('h1')
# print(h1)
a=h1.find(class_="link")
print(a['href'])

i=a.find(class_="spnew2 ico_logo")
print(i)






















