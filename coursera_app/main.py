#Import Library
from functions import *

def main():
    htmls=[]
    data=[]
    max=getNumberOfPage()
    links=getListofCoursesLinks(2)
    for link in links:
        htmls.append({"link":link,"data":getCoursesHtmls(link)})
    for html in htmls:
        data.append(processHtmlData(html['link'],html['data']))
    writeData(data,'coursera.csv')

if __name__ == "__main__":
    main()