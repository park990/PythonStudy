fs = open("ex1_test2.txt","rb")
content = fs.read()
fs.close()
print(content)
print("-------decoding------")
print(content.decode("ansi")) # 파일의 원래 형식대로 decode 시켜서 출력함.