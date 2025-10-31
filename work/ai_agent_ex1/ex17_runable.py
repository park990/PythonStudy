"""
Runable은 LangChain에서 입력값을 받아 원하는 처리를 수행하고, 동기식, 비동기식, 스트리밍, 배치 처리를
쉽게 실행할 수 있는 표준화된 실행객체다.

-invoke(): 동기적 실행
-ainvoke(): 비동기적 실행
-stream(): 스트리밍 방식 실행
-astream(): 비동기적 스트리밍 실행
-batch(리스트구조): 배치 처리

대표적인 클래스: RunnableLamda
    함수형 스타일로 사용자 정의 함수
    워크플로우에 쉽게 끼워 넣고 실행할 수 있게 하는 래퍼클래스다.
    개인적으로 경험한 경험한 경우는 데이터 전처리, 계산, 외부API 호출시 
    RunableLamda로 감싸면 해당 함수가 자동으로 Runable객체처럼 체인 내에서
    invoke(실행)될 수 있다.
"""

from langchain_core.runnables import RunnableLambda

def add_exec(msg:str)->str:
    # 문자열 뒤에 "!" 를 붙이는 함수 만드거임.
    return f"{msg}!"
    

run = RunnableLambda(add_exec)
result = run.invoke("와아 금요일이다.")
print(result)
print("======================================")
ar=["양식","한식","중식","일식"]

result2 = run.batch(ar)
print(result2)

for i in result2:
    print(i, end=", ")
    