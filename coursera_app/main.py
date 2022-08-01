#Import Library
from functions import *

def main():
    htmls=[]
    data=[]
    max=getNumberOfPage()
    links=getListofCoursesLinks(2)
    print(links)
    for link in links:
        htmls.append(getCoursesHtmls(link))
    # print(htmls)
    for html in htmls:
        data.append(processHtmlData(html))
    print(data)
    # firstDataRequest=webRequest(1)
    # maxPageNumber=int(getNumberOfPage(firstDataRequest))
    # pageDataList=getAllPageData(maxPageNumber)
    # for pageData in pageDataList:
    #     getCourseLink(pageData)
    # for numberOfPage in range(0,10):
    #     getLinksData(links[numberOfPage])
    # writeData(dataDic,"gen.csv")

if __name__ == "__main__":
    main()