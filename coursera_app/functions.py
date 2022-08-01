#Import Library
import requests
from bs4 import BeautifulSoup
import pandas as pd

#Attribute
links=[]
dataDic=[]
storeHtmlData=[]

# Functions
def getNumberOfPage():
    url='https://www.coursera.org/directory/courses?page=1'
    response = requests.get(url)
    soupData=BeautifulSoup(response.content, 'html.parser')
    pagination = soupData.find_all('div',class_="pagination-controls-container")
    for pagination_dev in pagination:
        page_number = pagination_dev.text.split("…")
        numberofpage = int(page_number[-1])
    print(numberofpage)
    return numberofpage


def getListofCoursesLinks(max):
    for page_num in range(0,max):
        url='https://www.coursera.org/directory/courses?page='+str(page_num)
        response = requests.get(url)
        soupData=BeautifulSoup(response.content, 'html.parser')
        page_data = soupData.find_all('a',class_="MuiTypography-root MuiLink-root MuiLink-underlineHover css-h830z8 MuiTypography-colorPrimary")
        for page in page_data:
            links.append("https://www.coursera.org"+page.attrs['href'])
    return links

def getCoursesHtmls(link):
    newresponse = requests.get(link)
    newsoup=BeautifulSoup(newresponse.content, 'html.parser')
    return newsoup

def processHtmlData(link,newsoup):
    list_of_tag=[]
    course_rate=None
    course_desc=None
    name=newsoup.find("h1")
    rate=newsoup.find("div",attrs={"class":"rc-ReviewsOverview__totals__rating"})
    if rate is not None:
        course_rate =rate.text
    desc=newsoup.find("p",attrs={"class":"cds-105 css-9it2qs cds-107"})
    if not desc:
        desc=newsoup.find("div",attrs={"class":"m-t-1 description"})
        if desc is not None:
            course_desc=desc.find('p').text
    else:
        course_desc=desc.text
    tags=newsoup.find_all("div",class_="_1ruggxy")
    for tag in tags:
        world=tag.text.replace("Chevron Right", '')
        if "Browse" not in world:
            list_of_tag.append(world)
    return{"Name":name.text,"Url":link,"Rating":course_rate,"Tags":list_of_tag,"Description":course_desc}

def writeData(courses_dict,filename):
    try:
        df = pd.DataFrame.from_dict(courses_dict) 
        df.to_csv (filename, index = False, header=True)
        return True
    except:
        print("An exception occجurred")
        return False

