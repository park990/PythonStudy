#부울형:bool (Boolean형)
b1 = True
b2 = False
print("b1:{}" .format(b1))
a = 100
b = 32
print("a+b=%d" %(a+b))

c = a*b
print("a*b=%d" %c)

c = a/b
print("a/b={}" .format(c))

c = a%b
print("a%b={}" .format(c))

## 비교 연산자
print(a==b)
print(a>=b)
print(a<=b)
print(a!=b)

## 논리연산자 (&, |, !)
print("a={}, b{}" .format(a,b))
print((a>b) & (a>=80))
print((a>b) | (a>=80))