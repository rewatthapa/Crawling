
import requests
import re
from bs4 import BeautifulSoup


response = requests.get("https://www.drupal.org/project/issues")
responseContent = response.content.decode('utf-8')


filePath = "./issues.csv"
logFile = open(filePath, 'a')

logFile.write("Project, Title, Status, Replies, AssignedTo")

issuesHtml = BeautifulSoup(responseContent, 'html.parser')


projectTitles = issuesHtml.find_all("td", class_="views-field-field-project-title")
issueTitles = issuesHtml.find_all("td", class_="views-field-title")
issueStatus = issuesHtml.find_all("td", class_="views-field-field-issue-status")
issueReplies = issuesHtml.find_all("td", class_="views-field-comment-count")
issueAssignment = issuesHtml.find_all("td", class_="views-field-field-issue-assigned")

result = []

projectResult = []
titleResult = []
statusResult = []
repliesResult = []
assignmentResult = [] 


for listOfProjectTd in projectTitles:
    for linkWithTitle in listOfProjectTd:
        for projectTitle in linkWithTitle:
        	if "\n" not in projectTitle and " " != projectTitle:
        		projectResult.append(projectTitle)
        	

for listOfTitlesTd in issueTitles:
	for linkWithTitle in listOfTitlesTd:
		for Title in linkWithTitle:
			if "\n" not in Title and ' ' != Title:
				titleResult.append(Title)

for listOfIssueStatusTd in issueStatus:
	for linkWithIssueStatus in listOfIssueStatusTd:
		statusResult.append(re.sub('\s+',' ',linkWithIssueStatus))

for listOfrepliesTd in issueReplies:
	for linkWithIssueReplies in listOfrepliesTd:
		for replies in linkWithIssueReplies:
			if "\n" not in replies and ' ' != replies:
				repliesResult.append(replies)

for listOfassignmentTd in issueAssignment:
	for linkWithAssignment in listOfassignmentTd:
		for assignedTo in linkWithAssignment:
			if "\n" not in assignedTo:
				assignmentResult.append(assignedTo)



for i in range(1, len(projectResult)):
	lineToWrite = projectResult[i]

	if i <= len(titleResult):
		lineToWrite += "," + titleResult[i]
	else:
		lineToWrite += " "

	if i <= len(statusResult):
		lineToWrite += "," + statusResult[i]
	else:
		lineToWrite += " "

	if i <= len(repliesResult):
		lineToWrite += "," + repliesResult[i]
	else:
		lineToWrite +=  0

	if i < len(assignmentResult):
		if " " == assignmentResult[i]:
			lineToWrite += ",unassigned"
		else :
			lineToWrite += "," + assignmentResult[i]
	else:
		lineToWrite += ",unassigned"

	logFile.write(lineToWrite + "\n")
