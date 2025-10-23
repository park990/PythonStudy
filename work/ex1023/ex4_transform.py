from pandas import Series, DataFrame

emp_dict = [
    {'empno':100, 'name':'마루치', 'job':'teacher', 'age': 32},
    {'empno':120, 'name':'아라치', 'job':'student', 'age': 18},
    {'empno':345, 'name':'을불', 'job':'student', 'age': 17},
    {'empno':210, 'name':'창조리', 'job':'teacher', 'age': 32},
    {'empno':349, 'name':'홍길동', 'job':'staff', 'age': 22},
    {'empno':218, 'name':'아수라', 'job':'student', 'age': 17},
    {'empno':545, 'name':'teacherAVG', 'job':'teacher', 'age': None},
    {'empno':445, 'name':'마이클', 'job':'teacher', 'age': 29},
    {'empno':410, 'name':'studentAVG', 'job':'student', 'age': None}
]
df = DataFrame(emp_dict)
print(df)
print("====================================================")
df["age"].fillna(df.groupby("job")["age"].transform("median"), inplace=True)
print(df)
