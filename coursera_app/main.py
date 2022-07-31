#Install Library
# !pip3 install requests=2.27.1
# !pip3 install beautifulsoup4=4.11.1
# !pip3 install lxml
# !pip3 install pandas

#Import Library
from functions import *

def main():
    firstDataRequest=webRequest(1)
    maxPageNumber=int(getNumberOfPage(firstDataRequest))
    pageDataList=getAllPageData(maxPageNumber)
    for pageData in pageDataList:
        getCourseLink(pageData)
    for numberOfPage in range(0,10):
        getLinksData(links[numberOfPage])
    writeData(dataDic,"gen.csv")

if __name__ == "__main__":
    main()