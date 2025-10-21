fs = open("ex1_test2.txt","r") #파일 연결
while True:
    content= fs.readline()
    if content !="":
        print(content, end="") #마지막 엔터값을 공백으로 대체하여 출력한다.
    else:
        break;        
fs.close()
print("읽기 끝")