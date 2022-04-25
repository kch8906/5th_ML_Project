from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
import os

baseUrl = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query='
plusUrl = input('검색어를 입력하세요.')
url = baseUrl + quote_plus(plusUrl)
html = urlopen(url)
soup = bs(html, 'html.parser')
img = soup.find_all(class_ = '_image')

dir_path = './Data/IMG_Crwaling/'
dir_name = plusUrl
os.mkdir(dir_path + "/" + dir_name + "/")
path = dir_path + "/" + dir_name + "/"
n = 1

for i in img:
    imgUrl = i['data-source']
    with urlopen(imgUrl) as f:
        with open(path + plusUrl + str(n) + '.jpg','wb') as h:
            img = f.read()
            h.write(img)
    n += 1
print("끝")