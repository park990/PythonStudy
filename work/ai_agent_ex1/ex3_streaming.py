
"""
LLM은 기본적으로 요청에 대한 응답을 두 가지 형태로 제공한다.
1) 요청에 대한 응답을 한번에 반환 하는 방법(앞의 예제의 경우)
2) 요청에 대한 결과를 계속해서 흘려보내는 방법

**스트리밍**(Streaming)
 데이터를 실시간으로 전송하고 수신하는 방식
pip install rich
"""
import anthropic
import rich
from dotenv import load_dotenv
import os

load_dotenv()
api_key=os.getenv("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=api_key)

prompt="독도는 한국땅 인가요? 일본땅 인가요?"

# with로 인해서 __enter__()와__exit__() 자동으로 호출된다.
# __enter__(): 함수에서 스트리밍 세션이 시작된다.
# __exit__(): 함수에서 스트림을 안전하게 닫도록 보장함
with client.messages.stream( # 스트리밍 세션 생성
    messages=[{"role":"user","content":prompt}],
    model="claude-3-5-haiku-latest",
    max_tokens=1000,
) as stream:
    for event in stream:
        if event.type =="text": # 답변의 타입이 문자열일 때
            print(event.text, end="")
            
    print("===========================구분선==============================")
    
    #스트림의 최종 응답 내용이 궁금다하면
    rich.print(stream.get_final_message())
