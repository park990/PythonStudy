import pandas as pd
from pandas import Series
df = pd.read_csv("data/test_data.tsv",sep="\t")
print(df)       #sep 대신 delimiter라고 해도 된다.
print("=========위쪽 2개의 데이터만 가져오자=========")
print(df.head(2))
print("=========아래쪽 2개의 데이터만 가져오자=========")
print(df.tail(2))
print("=========년도 컬럼 데이터만 가져오자=========")
print(df['year'])
