print("App Starting...")

# from selenium import webdriver
import time
import json
# from selenium.webdriver.chrome.options import Options
import os
import csv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data={}
data["employee"]=[]
def csv_to_json():
	with open('E:/PROJECTS B2/automation/Payment Table Original.csv') as csvf: 
		csvReader = csv.DictReader(csvf)

		for rows in csvReader:
			data["employee"].append(rows)

	with open(os.path.join('E:/PROJECTS B2/automation//new.json'), 'w', encoding='utf-8') as jsonf:
		jsonf.write(json.dumps(data, indent=4))
# csv_to_json()

def add_employee_bot():
	list_mobile =[]
	count = 0
	with open(os.path.join('E:/PROJECTS B2/automation/new.json'), 'r', encoding='utf-8') as jsonf:
		json_file = json.load(jsonf)

		for a in json_file["employee"]:
			if a["Ins_ NID"] in list_mobile:
				print(str(a["ID"])+"--" +str(list_mobile.index(a["Ins_ NID"])) + "--"+  str(count) + "--" + str(a["Ins_ NID"]))
			else:
				list_mobile.append(a["Ins_ NID"])
			count +=1


add_employee_bot()
# def scrap():
# 	options = Options()
# 	options.add_argument('--headless')
# 	options.add_argument('--disable-gpu') 

# 	browser = webdriver.Chrome('C:/Users/USER/projects/WORKSHOP/automation/chromedriver.exe' , options=options)

# 	browser.get("https://dev.to/")
# 	print("scrolling started")
# 	for a in range(1,3):
# 		b = a* 3000
# 		browser.execute_script("window.scrollTo(0, {})".format(b))
# 		time.sleep(2)
# 		print("scrolled {}".format(b))
# 	web=browser.find_element_by_xpath('//*[@id="substories"]')


# 	lista = web.find_elements_by_class_name('crayons-story__body')

# 	print("working...")
# 	data = {}
# 	data['people']=[]
# 	for x in lista:

# 		name = ((((x.find_element_by_class_name('crayons-story__meta')).find_element_by_class_name('crayons-story__secondary')).get_attribute(r'text')).replace('\n            ', '')).replace('  ', '')
# 		print(name)
# 		title = ((((x.find_element_by_class_name('crayons-story__title')).find_element_by_tag_name('a')).get_attribute('text')).replace('\n          ', '')).replace('\n\n        ', '')
# 		link = ((x.find_element_by_class_name('crayons-story__title')).find_element_by_tag_name('a')).get_attribute('href')
# 		entry = {"Name":name ,
# 		"Title": title ,
# 		"Link":link ,
# 		}
# 		query = dev_scrap_db(name=name, title=title, link=link)
# 		query.save()

# 		data['people'].append(entry)

# 	with open(os.path.join(BASE_DIR,'file.json'), 'w',encoding='utf-8') as outfile:
# 		json.dump(data, outfile, ensure_ascii=False)


# 	print("done")
# 	return data['people']

# def json_to_csv():
# 	with open(os.path.join(BASE_DIR,'file.json'),'r', encoding="utf-8") as json_file: 
# 		data = json.load(json_file) 
	  
# 	employee_data = data['people'] 
	  
# 	# now we will open a file for writing 
# 	with open(os.path.join(BASE_DIR,'static','new.csv'), 'w', encoding="utf-8") as csvfile:
# 		    fieldnames = ['Name', 'Title', 'Link']
# 		    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

# 		    writer.writeheader()
# 		    count=0
# 		    for emp in employee_data:
# 		    	try:
# 		    		writer.writerow(emp)
# 		    		print("str in {}".format(count))
# 		    	except:
# 		    		dic = {
# 		    		"Name":(emp["Name"]).encode("utf-8"),
# 		    		"Title":(emp["Title"]).encode("utf-8"),
# 		    		"Link":emp["Link"]
# 		    		}
# 		    		print("Bytes in {}".format(count))
# 		    		writer.writerow(dic)
# 		    	count+=1

