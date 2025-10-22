from pandas import Series, DataFrame

emp_dict = [
    {'empno':100, 'name':'마루치', 'job':'IT_PROG'},
    {'empno':120, 'name':'아라치', 'job':'Analysis'},
    {'empno':345, 'name':'을불', 'job':'IT_PROG'},
    {'empno':210, 'name':'창조리', 'job':'Sales'},
    {'empno':349, 'name':'홍길동', 'job':'IT_PROG'},
    {'empno':218, 'name':'아수라', 'job':'Sales'},
    {'empno':445, 'name':'마이클', 'job':'IT_PROG'},
    {'empno':410, 'name':'어두일미', 'job':'Analysis'}
]
df = DataFrame(emp_dict)
print(df)

print("================job으로 그룹 만들기==================")
group_job = df.groupby("job")
print(group_job.groups)

print("================job으로 그룹 만들기==================")
for name, group in group_job:
    print("{}: {}" .format(name,len(group)))
    print(group)
    print("=================================")
