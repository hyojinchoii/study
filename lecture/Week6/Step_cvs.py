import pandas as p
import os

score_csv = p.read_csv('meta-data/csv/score.csv')
print(score_csv.info())
