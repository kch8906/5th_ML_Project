

####################################### 성공 1 => 이미지가 너무 적게 불러와짐,,,,

from bs4 import BeautifulSoup
import requests
import urllib.request
from urllib.request import urlopen
from urllib.parse import quote_plus


baseURL = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusURL = input('입력')
#plusURL = '눈 감은 사람'
url = baseURL + quote_plus(plusURL)
#print(url)
html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
#img = soup.find_all('img')
img = soup.select("a img")
#print(img[0])

n = 1
for i in img:
    imgUrl = i['src']
    with urlopen(imgUrl) as f:
        with open('./img/' + plusURL + str(n) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    n +=1
    print(imgUrl)
print('끝')

#########################################################################


'''
driver = webdriver.Chrome(options=options)
driver.get("https://search.naver.com/search.naver?where=image&sm=tab_jum&query=")
elem = driver.find_element_by_id("nx_query")
elem.send_keys("눈 감은 사람")
elem.send_keys(Keys.RETURN)
'''