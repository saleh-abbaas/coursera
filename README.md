# Coursera Project

### Software Architecture and design:
- Python
- Argo workflow

### Description:

We need to retrieve courses data from the Coursera website using web scraping technology, by following these steps:
1)	Get the number of pages
2)	Get a list of course links
3)	Get the courses HTMLs
4)	Process the HTMLs to row data
5)	Check the data if it exists or not to store the new data or update the existing data
6)	Store all new changes


### To run this code using Python you need to follow these steps:
1) install all requirement from [coursera_app/requirement.txt] using "pip3 install -r requirements.txt"
2) run coursera_app/main.py using "python3 main.py"

### To run this code using Argo Workflow you need to follow these steps:
1) install argo workflow
2) open argo webpage
3) import argo_workflow/coursera-workflow.yaml file or using terminal "argo submit -n argo --watch https://github.com/Saleh-h-m-abbas/coursera/blob/main/argo%20workflow/coursera-workflow.yaml" 



## Coursera Project FlowChart:

![Alt text](documentation/FlowChart.jpg?raw=true "coursera project flowchart")
