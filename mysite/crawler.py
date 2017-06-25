import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import requests
from bs4 import BeautifulSoup

urlCategoryList = []
urlCategoryBase = "http://www.armchairgeneral.com/category/tactics101"
#urlCategoryList.append(urlCategoryBase)
for i in range(1, 7):
    urlCategoryList.append(urlCategoryBase+'/page/'+str(i))
print urlCategoryList

articlesUrlsList = []

for urlCategory in urlCategoryList:
    req = requests.get(urlCategory).text
    soup = BeautifulSoup(req, 'html.parser')
    articleLinksOnPageList = soup.find_all('a', {'class':'more'})
    for articleLink in articleLinksOnPageList:
        articlesUrlsList.append(articleLink['href'])


for articleUrl in articlesUrlsList:
    req = requests.get(articleUrl).text
    soup = BeautifulSoup(req, 'html.parser')
    articleContent = soup.find('div', {'class':'post_content clearfix'})
    articleName = soup.find('h1', {'class':'title'}).text
    articleFileName = "C:/Tactics101/"+(articleName) + '.html'
    try:
        articleFile = open(articleFileName, 'w')
        dataToWrite = articleContent.prettify(formatter='html')
        articleFile.write(dataToWrite)
        articleFile.close()
        print 'SUCCESS with ' + articleFileName + ' SIZE: ' + str(len(dataToWrite))
    except Exception, err:
        print "FAIL with " + articleFileName + ' ' + str(err)
        break

