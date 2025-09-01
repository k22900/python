# import keyword
from bs4 import BeautifulSoup 
import requests

keyword=input("검색어를 입력해주세요 :")



baseURL = f"https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query={keyword}"

response= requests.get(baseURL)
resoure= response.text

soup=BeautifulSoup(resoure, "html.parser") 
titles = soup.select("a.news_tit")
result=[]

for title in titles:
    tit=title.text
    result.append(tit)
print(result)