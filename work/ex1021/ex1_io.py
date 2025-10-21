"""_summary_
파이썬에서 파일을 읽기/쓰기 하는 방법
-파일을 열기(open) 했으면 반드시 닫기(close) 해야함
(파일을 열기할 때는 반드시 읽기를 하기 위함인지?
쓰기를 하기 위함인지 명시해야한다.)

- mode는 다음과 같이 구분된다.
    ** w : 쓰기
    ** r : 읽기
    ** a : 추가
    ** rb: 바이너리로 읽기

"""
print("===================형식 UTF-8======================")
# fs = open("ex1_test.txt","r")
with open("ex1_test.txt","r",encoding="utf-8") as fs:
    content = fs.read()
fs.close()

print(content)


print("===================형식 ANSI======================")
fs = open("ex1_test2.txt","r")
content = fs.read()
fs.close()
print(content)