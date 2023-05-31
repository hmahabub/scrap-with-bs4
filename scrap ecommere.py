print("App Starting...")

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
import json
# from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests

browser =requests.get("https://www.leifshop.com/collections/home-goods")
web = browser.text
bs = BeautifulSoup(web, 'html.parser')
lista = bs.find_all('div', attrs={'class':'product-grid-item grid__item'})
count=0
data={}
data["products"]=[]
for x in lista:
	y=(x.find('a'))['href']
	browser = requests.get("https://www.leifshop.com{}".format(y))
	web = browser.text
	bs = BeautifulSoup(web, 'html.parser')
	p_name = bs.find('h1').contents[0]
	p_price = bs.find('span',attrs={"class":"price-span"}).contents[0]
	variant=[]
	
	for x in bs.find_all('div',attrs={"class":"selector-wrapper js"}):
		try:
			variant_name = x.find('label', attrs={"top-label show"}).contents[0]
		except:
			variant_name="other"
		variant_list=[]
		for y in x.find_all('option'):
			a = y.contents
			variant_list.append(a[0])
		v_entry={
		variant_name: variant_list
		}
		variant.append(v_entry)
	p_descrip = bs.find('div',attrs={"class":"rte description"}).contents[0]
	properties=[]
	for y in bs.find_all('tr'):
		a = (y.find_all("td")[0]).contents[0]
		b = (y.find_all("td")[1]).contents[0]
		c={
		a:b,
		}
		properties.append(c)
	

	entry={
	"p_name": p_name,
	"p_price": p_price,
	"p_descrip": p_descrip,
	"variant": variant,
	"properties": properties
	}
	data["products"].append(entry)
	print([count, p_name , p_price])
	count+=1

with open('file_buto.json', 'w',encoding='utf-8') as outfile:
	json.dump(data, outfile, ensure_ascii=False)
