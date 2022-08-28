import urllib.request
from bs4 import BeautifulSoup

url= 'https://news.daum.net/foreign#1'

# 원격 서버 파일 요청
res = urllib.request.urlopen(url)
data = res.read()
print(type(data))

src = data.decode('utf-8')
print(type(src))

with open('sample.html','w',encoding = 'utf -8') as f :
    f. write(src)

# 3. html 파싱
html = BeautifulSoup(src, 'html.parser')
print(type(html))

a = html.find_all('a')
# print('a tag : ', a)
# print('a tag 내용: ', a.string)

lis = html.find_all ('li')

# for li in lis :
#     print(li.string)