import pandas as pd
import numpy as np
from bs4 import BeautifulSoup   
import requests
result=pd.Series(data=[20,30,40], index=['Bread','Butter','Jaam'], name='Price of the category item')
# print(result)

dictionary={'apple':45,"grapes":35,'guava':34}
# print(pd.Series(dictionary))

datas=pd.read_csv('youtube_channel_info_v1.csv')
print(datas)

print("*********************************************************")

dict_avg=dict(datas)
print(dict_avg)
print(type(dict_avg))


print("*********************************************************")


response=requests.get("http://quotes.toscrape.com")

soup = BeautifulSoup(response.text,"html.parser")

quotes=soup.find_all("span", class_="text")
quote1=soup.find_all("small", class_="author")

for qote in quotes:
    print(qote.text)

for qote in quote1:
    print(qote.text)




