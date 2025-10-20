for i in range(1,11):
    print(i)
    
print("=============================")
ar = ["python","java","c++","html","css"]
for v in ar:
    print(v)
print("=============================")
for v in enumerate(ar):
    print(v)
    
print("=============================")
for i, v in enumerate(ar):
    print("index={} , value={}" .format(i,v))