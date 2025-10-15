str = 'go for it!'
print("str=%s" %str)

print("str>>{}" .format(str))

test = str*3

print("test:{}" .format(test))

test2 = test.replace("for","***")
print("test2:{}" .format(test2))

v1=str[3]
print("str[3]=%s" %v1)

v2= str[3:6]
print("v2[3:6]:%s" %v2)

#자바의 indexOf("") 위치 값 알아내는 방법
idx = str.find("fo")
print("str.find(\"fo\"):{}" .format(idx))