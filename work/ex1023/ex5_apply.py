from pandas import Series, DataFrame

df= DataFrame([
    {"b_day":"1997-10-23"},
    {"b_day":"2000-08-15"},
    {"b_day":"2003-09-13"},
    {"b_day":"1999-07-25"},
])
print(df)
print("============================================")

def clip_year(col):
    return col.split("-")[0]

df["year"] = df["b_day"].apply(clip_year) # clip_year(df["b_day"])
# 즉 apply 함수를 붙이면 앞의 컬럼 값이 우선 인자로 전달된다.
print(df)

def get_age(year, c_year):
    return c_year -int(year)

df["age"]=df["year"].apply(get_age,c_year=2025)
print(df)

print("=======================함수호출 시 행전체를 인자로 전달=======================")
def get_age2(row):
    return str(row.year)+"년생은 "+str(row.age)+"세"

df["etc"] = df.apply(get_age2, axis=1) # 하나의 행 의미 axis=1
print(df)
