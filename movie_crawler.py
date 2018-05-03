
import requests

from bs4 import BeautifulSoup


#response = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=8aba35e0")
response = requests.get("https://www.drupal.org/project/issues")
responseContent = response.content.decode('utf-8')


filePath = "./issues.csv"
logFile = open(filePath, 'a')

logFile.write("Project,Title,Status,Replies,AssignedTo")

issuesHtml = BeautifulSoup(responseContent, 'html.parser')


projectTitles = issuesHtml.find_all("td", class_="views-field-field-project-title")
issueTitles = issuesHtml.find_all("td", class_="views-field-title")
issueStatus = issuesHtml.find_all("td", class_="views-field-field-issue-status")
#issuePriority = issuesHtml.find_all("td", class_="views-field-field-issue-priority")
#issueCategory = issuesHtml.find_all("td", class_="views-field-field-issue-category")
#issueVersion = issuesHtml.find_all("td", class_="views-field-field-issue-version")
issueReplies = issuesHtml.find_all("td", class_="views-field-comment-count")
issueAssignment = issuesHtml.find_all("td", class_="views-field-field-issue-assigned")

result = []

projectResult = []
titleResult = []
statusResult = []
#priorityResult = []
#categoryResult = []
#versionResult = []
repliesResult = []
assignmentResult = [] 

#print(issueStatus)
#Create an array of all proejct and title
#the dictoinary should contain data in the following format
# project1 dict({"project":"Block field", "title":"Convert WTB tests to BTB (and fix failing tests)"})


#result = dict("project": "", "title": "", "status": "")

#results = {}


for listOfProjectTd in projectTitles:
    for linkWithTitle in listOfProjectTd:
        for projectTitle in linkWithTitle:
        	projectResult.append(projectTitle)
        	

for listOfTitlesTd in issueTitles:
	for linkWithTitle in listOfTitlesTd:
		for Title in linkWithTitle:
			titleResult.append(Title)

for listOfIssueStatusTd in issueStatus:
	for linkWithIssueStatus in listOfIssueStatusTd:
		for IssueStatus in linkWithIssueStatus:
			statusResult.append(IssueStatus)

for listOfrepliesTd in issueReplies:
	for linkWithIssueReplies in listOfrepliesTd:
		for replies in linkWithIssueReplies:
			repliesResult.append(replies)

for listOfassignmentTd in issueAssignment:
	for linkWithAssignment in listOfassignmentTd:
		for assignedTo in linkWithAssignment:
			assignmentResult.append(assignedTo)

#print (statusResult)
#print (repliesResult)
print (assignmentResult)

for i in range(1, len(projectResult)):
	logFile.write(projectResult[i] + ',' + titleResult[i] + ',' + statusResult[i] + ',' + repliesResult[i] + ',' + assignmentResult[i])
        	#results
            #logFile.write(l + "\n")


