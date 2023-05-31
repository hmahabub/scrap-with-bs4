#TEST FILE FOR RESTING ALL
print("App Starting...")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu') 

browser = webdriver.Chrome('C:/Users/USER/projects/WORKSHOP/automation/chromedriver.exe' , options=options)
for a in range(1,11):
	browser.get("https://www.rokomari.com/book/author/1/%E0%A6%B9%E0%A7%81%E0%A6%AE%E0%A6%BE%E0%A7%9F%E0%A7%82%E0%A6%A8-%E0%A6%86%E0%A6%B9%E0%A6%AE%E0%A7%87%E0%A6%A6?ref=mm_p0&page={}".format(a))
	writer = "হুমায়ুন আহমেদ"
	# print("scrolling started")
	# for a in range(1,100):
	# 	b = a* 3000
	# 	browser.execute_script("window.scrollTo(0, {})".format(b))
	# 	time.sleep(3)
	# 	print("scrolled {}".format(b))

	web=browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/section/div[2]/div').get_attribute("innerHTML")

	bs = BeautifulSoup(web, 'html.parser')
	lista = bs.find_all(attrs={'class':'book-list-wrapper'})
	# lista = web.find_elements_by_class_name('book-list-wrapper')

	print("working...")
	data = {}
	data[str(a)]=[]
	count=0
	for x in lista:
		title=""
		author=""
		price=""
		for y in (x.find(attrs={"class":"book-title"}).contents):
			title= y
		for y in (x.find(attrs={"class":"book-author"}).contents):
			author= y
		for y in ((x.find(attrs={"class":"book-price"}).find('span')).contents):
			price= y

		entry = {"Title": title ,
				"author":author,
		"Price":price ,
		}
		print("entry no. {}".format(count))
		data[str(a)].append(entry)
		count+=1

	with open('file{}.json'.format(a), 'w',encoding='utf-8') as outfile:
		json.dump(data, outfile, ensure_ascii=False)


print("done")



#browser.execute_script('''window.open("https://google.com/","_blank");''')

