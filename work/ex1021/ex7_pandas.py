import pandas as pd
from pandas import Series, DataFrame


ko = pd.Series([123,456,789,101112])
print(ko)
print("===============index값 변경================")
ko=Series(["123",456,789,101112],index=['10-02','10-03','10-04','10-05'])
print(ko)
print("===============index값만 출력===============")
for i in ko.index:
    print(i)   
print("===============value값만 출력===============")
for i in ko.values:
    print(i)