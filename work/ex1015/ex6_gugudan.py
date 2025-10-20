
dan=input("몇 단?:")
dan=int(dan)
print(type(dan))
for i in range(1,10):
    print("{}*{}={}" .format(dan,i,dan*i))
print("=============================")
for i in range(1,10):
    str =""
    for j in range(2,10):
        str += "{}*{}={}\t" .format(j,i,(j*i))
    print(str)