import pandas as p
import os

score_csv = p.read_csv('meta-data/csv/score.csv')
print(score_csv.info())
print(score_csv.head())

# 엑셀 데이터를 끌고와서 리스트에 저장

kor  = score_csv.kor
eng = score_csv.eng
mat = score_csv.mat
dept = score_csv['dept']

print('kor max: ', max(kor))
print('eng max: ', max(eng))
print('mat max: ', max(mat))
print('dept max: ', max(dept))

print('kor min: ', min(kor))
print('eng min: ', min(eng))
print('mat min: ', min(mat))
print('dept min: ', min(dept))

from statistics import mean

print('kor mean: ', round(mean(kor),3))
print('eng mean: ', round(mean(eng),2))
print('mat mean: ', round(mean(mat),1))
print('dept mean: ', round(mean(dept),2))

# 중복을 허용하지 않는 컬렉션 set
# key:value

dept_cnt = {}

for key in dept:
    dept_cnt[key] = dept_cnt.get(key,0) + 1

print(dept_cnt)


# bmi 데이터 활용하기

import pandas as p
import os

bmi_csv = p.read_csv('lecture/Week6/meta-data/csv/bmi.csv')
print(bmi_csv.info())
print(bmi_csv.head())

w = bmi_csv['weight']
label = bmi_csv['label']

print('최대몸무게', max(w))

label_cnt = {}

for key in label:
    label_cnt[key] = label_cnt.get(key,0) + 1

print(label_cnt)