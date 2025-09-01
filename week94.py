# from urllib import response
from bs4 import BeautifulSoup
import requests

keyWord=input("검색어를 입력해주세요 :")

baseURL =f"https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query={keyWord}"


response= requests.get(baseURL)
resoure= response.text

soup=BeautifulSoup(resoure, "html.parser") 
items = soup.select("a.title_link")
# print(items)

result=[]
for item in items:
    blogTitle = item.text
    if "sk"in blogTitle:
        continue
    if "Sk"in blogTitle:
        continue   
    if "sK"in blogTitle:
        continue    
    if "SK"in blogTitle:
        continue 
    if "LG"in blogTitle:
        continue   
    result.append(blogTitle)

    
print(result)
    
    
    
    
    
    
    
    
    
    
