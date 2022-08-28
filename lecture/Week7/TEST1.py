import urllib.request
from bs4 import BeautifulSoup

with open('daum_sample2.html','r', encoding = 'utf-8') as f :

    source = f.read()

html = BeautifulSoup(source,'html.parser')

# 원격 서버 파일 요청
res = urllib.request.urlopen(url)
data = res.read()
# print(type(data))

src = data.decode('utf-8')
print(type(src))

with open('sample.html','w',encoding = 'utf -8') as f :
    f. write(src)

html = BeautifulSoup(src, 'html.parser')
print(type(html))

# SELECT 함수 사용
a = html.find_all('a')
atags = html.select('a[class=link_txt]')
print(atags)
print(len(atags))

crawling_data = []

for tag in atags :
    tagstr = str(tag.string)
    crawling_data.append(tagstr.strip())
print(crawling_data)

import pickle
file = open('daum_title.pickle','wb')
pickle.dump(crawling_data,file)
print('리스트 저장 성공')