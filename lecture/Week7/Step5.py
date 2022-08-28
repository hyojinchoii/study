from bs4 import BeautifulSoup

with open('daum_sample.html','r', encoding = 'utf-8') as f :

    source = f.read()

html = BeautifulSoup(source,'html.parser')

# table = html.select_one('#tit_g')
# print(table)

atags = html.select('a[class=link_txt]')
print(atags)
print(len(atags))

# a_list = html.find_all('a')
# for i in a_list:
#     print(i)

crawling_data = []

for tag in atags :
    tagstr = str(tag.string)
    crawling_data.append(tagstr.strip())
print(crawling_data)


import pickle
file = open('daum_title.pickle','wb')
pickle.dump(crawling_data,file)
print('리스트 저장 성공')


