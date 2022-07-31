#Import Library
import requests
from bs4 import BeautifulSoup
import pandas as pd

#Attribute
links=[]
dataDic=[]

# Functions
def webRequest(numberofPage):
    url='https://www.coursera.org/directory/courses?page='+str(numberofPage)
    response = requests.get(url)
    return BeautifulSoup(response.content, 'lxml')

def getNumberOfPage(soupData):
    pagination = soupData.find_all('div',{"class":"pagination-controls-container"})
    for pagination_dev in pagination:
        page_number = pagination_dev.text.split("…")
        return page_number[-1]

def getAllPageData(max):
    pagesList=[]
    for page_number in range(0,max):
        pagesList.append(webRequest(page_number))
    return pagesList

def getCourseLink(pageData):
    page_data = pageData.findAll('a',{"class":"MuiTypography-root MuiLink-root MuiLink-underlineHover css-h830z8 MuiTypography-colorPrimary"})
    for page in page_data:
        links.append("https://www.coursera.org"+page.attrs['href'])
    return links

def getLinksData(link):
    list_of_tag=[]
    course_desc=None
    course_rate=None
    newresponse = requests.get(link)
    newsoup=BeautifulSoup(newresponse.content, 'lxml')
    name=newsoup.find("h1")
    rate=newsoup.find("div",{"class":"rc-ReviewsOverview__totals__rating"})
    if rate is not None:
        course_rate =rate.text
    desc=newsoup.find("p",{"class":"cds-105 css-9it2qs cds-107"})
    if not desc:
        desc=newsoup.find("div",{"class":"m-t-1 description"})
        if desc is not None:
            course_desc=desc.find('p').text
    else:
        course_desc=desc.text

    tags=newsoup.find_all("div",{"class":"_1ruggxy"})
    for tag in tags:
        world=tag.text.replace("Chevron Right", '')
        if "Browse" not in world:
            list_of_tag.append(world)
    dataDic.append({"Name":name.text,"Url":link,"Rating":course_rate,"Tags":list_of_tag,"Description":course_desc})
    return dataDic

def writeData(courses_dict,filename):
    try:
        df = pd.DataFrame.from_dict(courses_dict) 
        df.to_csv (filename, index = False, header=True)
        return True
    except:
        print("An exception occurred")
        return False

