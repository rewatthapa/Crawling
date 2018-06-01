from bs4 import BeautifulSoup
import requests
import re


source = requests.get("https://www.drupal.org/user/909522/track")
responseContent = source.content.decode('utf-8')

filePath = "./dinarcon.csv"
logFile = open(filePath, 'a')

logFile.write("Type, Title, Author, Replies")

soup = BeautifulSoup(responseContent, 'html.parser')

#print (soup.prettify())

table = soup.find("tbody")

#print (table)

row = table.find_all("tr")
 
#print (row)

result = []


for item in row:
	#print (item)
	for td in item:
		for x in td:
			print(x)
#results = str(result)

#print (results).text

#for i in range(0, len(result)):
	#lineToWrite = result[i]
	#print (lineToWrite)
#print (result) 
#logFile.write(lineToWrite + "\n")	
			