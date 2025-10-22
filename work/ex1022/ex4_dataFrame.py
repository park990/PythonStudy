from pandas import Series, DataFrame

ar=[{"id":1010,"name":"이무배","Java":99,"python":97,"Fast":98},
    {"id":1120,"name":"개똥이","Java":39,"python":72,"Fast":20},
    {"id":1015,"name":"죽띵이","Java":84,"python":52,"Fast":40},
    {"id":2310,"name":"도날드","Java":35,"python":22,"Fast":50}]

df = DataFrame(ar)
print(df)

print("================총점[Total] 컬럼 추가===========================")
df["Total"] = df["Java"] + df["python"] + df["Fast"]
print(df)

print("================총점[Total] 컬럼 추가===========================")
df["Avg"] = (df["Total"]/3).round(1)
print(df)

print("===================등급[Grade]를 지정하자========================")

grades=[] # 등급들이 들어갈 저장소
for i in df["Avg"]:
    if(i>95):
        grades.append("A+")
    elif(i>89):
        grades.append("A")
    elif(i>85):
        grades.append("B+")
    elif(i>79):
        grades.append("B")
    elif(i>75):
        grades.append("C+")
    elif(i>69):
        grades.append("C")
    elif(i>65):
        grades.append("D+")
    elif(i>59):
        grades.append("D")
    else:
        grades.append("F")
        
df["Grade"]=grades
print(df)