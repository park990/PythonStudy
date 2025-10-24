"""_summary_
먼저 Anthropic패키지를 설치하자
pip install anthropic==0.49.0
pip install python-dotenv
"""
import anthropic
from dotenv import load_dotenv
import os

load_dotenv()
# 원하는 ANTHROPIC_API_KEY값 가져오기
api_key = os.getenv("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=api_key)

conversation=[] # 대화기록을 저장할 곳 

# 사용자의 입력값(프롬프트) 추가
conversation.append({"role":"user","content":"안녕?! 나는 박재윤이다 반말해라 앞으로"})

response= client.messages.create(
    model="claude-3-5-haiku-latest",
    max_tokens=1000,
    messages=conversation
)

assistant_message = response.content[0].text
print(assistant_message)