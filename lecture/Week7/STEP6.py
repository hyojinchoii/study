import pickle
file = open('daum_title.pickle','rb')
news_title = pickle.load(file)
print(news_title)

import re

def clean_text(text_string):
    # 문장부호 제거 : 따옴표 추가(\'\")
    text_string_re = re.sub('[,.?!:\'\";]', '', text_string)
    # 특수문자, 숫자 제거
    text_string_re = re.sub('[!@#$%^&*()]|[0-9]', '', text_string_re)
    # 영문 소문자 -> 영문 제거
    text_string_re = text_string_re.lower()
    text_string_re = re.sub('[a-z]', '', text_string_re)
    # 공백 제거
    text_string_re = ' '.join(text_string_re.split())

    return text_string_re

clean_texts = [clean_text((row)) for row in news_title]

# print(clean_texts)

# 중복을 허용하지 않는 set
word_list = {}

for text in clean_texts:
    for word in text.split():
        word_list[word] = word_list.get(word, 0) + 1

print(word_list)

# del word_list ['윌']

# 단어 빈도수가 3 이상인 데이터, 글자수가 2 이상

new_word_list = {}

for word, cnt in word_list.items():
    if cnt >=3 and len(word) >= 2 and len(word) <=3 :
        new_word_list[word] = new_word_list.get(word,cnt)

print(new_word_list)

from collections import Counter
counter = Counter(new_word_list)
top5 = counter.most_common(5)
print(top5)

word = []
counts = []

for w , c in top5 :
    word.append(w)
    counts.append(c)
import matplotlib.pyplot

words = ['탄소중립','윤석열','인플레이션','추석']
counts = [4,2,5,1]
import matplotlib.pyplot as plt

from matplotlib import font_manager,rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# 선 그래프
plt.plot(words,counts)

# 차트 구성요소 추가
plt.title("step and line graph")
plt.xlabel("단어")
plt.ylabel("빈도수")
plt.legend(loc='words')
plt.show()