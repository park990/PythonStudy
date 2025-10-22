from pandas import Series, DataFrame

emp = [[100,"마루치","dev"],
        [220,"아루마","dev"],
        [250,"가루두","dev"],
        [290,"므루게","ceo"]]

#컬럼명만 따로 저장하자
c_name =["empno","ename","job"]

#위의 내용들을 가지고 DataFrame 생성
df = DataFrame.from_records(emp, columns=c_name)
print(df)
print("========0행과 2행 지우자=================")
print(df.drop([0,2]))

print("============ceo 인행=============")
print(df[df.job == "ceo"])



