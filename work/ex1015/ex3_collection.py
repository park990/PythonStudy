## 파이썬의 자료구조

"""
 - List : 배열과 같고 순서를 가짐 :[값1, 값2, 값3]
 - Tuple: List와 같지만 읽기 전용 추가하거나 수정하지 못한다:(값1, 값2, 값3)
 - Set: List와 유사하지만 교집합 구분 : {값1, 값2, 값3}
 - Dict: 키와 값이 쌍을 이루어 저장된다. :
            dict(키1=값1, 키2=값2...) //MAP 구조로 생각하자.
            {"키1":"값1","키2":"값2"}
"""
ar1 = [10, 3.14, "TEST"]

print("ar1:{}" .format(ar1))

ar2=[10,20,30,3.3,"Michael"]

var1 = ar2[3]
print("ar2[3]={}" .format(var1))

print("ar2의 길이={}" .format(len(ar2)))

# 리스트 구조가 있는데 길이가 얼마인지 모를 때
#  마지막 요소의 값을 출력하려고 한다.
print("ar2의마지막 요소는={}" .format(ar2[len(ar2)-1]))

#  기억: len(리스트) : 길이를 구해주며 전수로 반환됨
tuple1 =(100,"tuple",200,10.5)
ar2[4]="KOREA"
ar2.append(1000)
print("ar2[]={}" .format(ar2))

# 하지만 튜플은 수정하지 못한다.
# tuple1[2]="test" 오류남

# print("tuple1.count={}" .format(tuple1.count()))

ar3 = ar2[:]
print("ar2[]={}" .format(ar2))
print("ar3[]={}" .format(ar3))

chk = ar2 is ar3
print("ar2 is ar3={}" .format(chk))

tuple2 = tuple1[:]
print("tuple1[]={}" .format(tuple1))
print("tuple2[]={}" .format(tuple2))

chk2 = tuple1 is tuple2
print("tuple1 is tuple2={}" .format(chk2))

# Set구조
ice1={"체리","외계인","슈팅스타","외계인"}
print("ice1[]길이={},{}" .format(len(ice1),ice1))

res="체리" in ice1
print("체리가 있나요?={}" .format(res))
print("\"체리\"가 있나요?", res)

res="체리" not in ice1
print("체리가 없다요: {}" .format(res))
print("체리가 없다요:", res)

t1 = set('1234567')
t2 = set("9804567")
print("t1:",t1)
print("t2:",t2)

res1 = t1 & t2 # 두 set구조의 교집합
print("t1 & t2:{}".format(res1))

res2= t1|t2 # 두 Set 구조의 합집합
print("t1 | t2:{}".format(res2))

res3 = t1 - t2 # 두 Set 구조의 차집합
print("t1-t2:{}".format(res3))

### dict
d1 =  {"k1":100,"k2":200, 3:300}
print("d1안의 k1값", d1.get("k1"))

d1[3] =11000 # 3이라는 key의 value 값을 11000으로 변경
print("d1:", d1)

d1[4]=2200
print("d1", d1)

res4= d1.get(3)
print("d1 Key값 3의 Value값:{}" .format(res4))

keys=d1.keys()
print("d1.keys()",keys)
values=d1.values()
print("d1.values()",values)

key_list = list(keys) # List 값으로 바꾼 값.
print("list로 바꾼 dict(keys)값들:{}"  .format(key_list))

"""_summary_
변경가능(mutable):List Set dict
변경불가(immutable): int float bool String tuple
"""
var1 = 100
var2 = 200
print("ID(Var1):{}" .format(id(var1)))
print("ID(Var2):{}" .format(id(var2)))
print("===============================")
var2=var1
print("ID(Var1):{}" .format(id(var1)))
print("ID(Var2):{}" .format(id(var2)))

res = var1 is var2
print("var1 is var2={}" .format(res))
print("(Var1):{}" .format((var1)))
print("(Var2):{}" .format((var2)))

