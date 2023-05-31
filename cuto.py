import json 
import csv 

  
# Opening JSON file and loading the data 
# into the variable data
file = open('new.csv','w', encoding="utf-8")
file.write("Title, author,Price\n\n")
file.close()
for a in range(1,11):
	with open('file{}.json'.format(a),'r', encoding="utf-8") as json_file: 
	    data = json.load(json_file)
	    employee_data = data[str(a)]
	    with open('new.csv', 'a', encoding="utf-8") as csvfile:
	    	fieldnames = ['Title','author', 'Price']
	    	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	    	
	    	count=0
	    	for emp in employee_data:
	    		writer.writerow(emp)
	    		print("str in {}".format(count))
	    		count+=1