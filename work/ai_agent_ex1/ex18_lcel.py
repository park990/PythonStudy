"""
LCEL (LangChain Expression Language): 랭체인 표현언어
Runable들을 조합하여 복잡한 로직을 만들 수 있게 하는 선언적 언어다.

예) chain = component1 | component2 | component3

프롬프트 -> 모델 -> 파서로 이어지는 예제 확인
"""
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_anthropic import ChatAnthropic
import anthropic
import os

load_dotenv()

api_key= os.getenv("ANTHROPIC_API_KEY")
prompt = ChatPromptTemplate.from_messages([
    ("human","오늘 10월 31일 오후 4시 롤 월즈 경기 t1과 AL중 어느 팀이 이길지 이유까지 한국어로 3줄이상 작성해줘:{word}")])

# 모델준비
model = ChatAnthropic(model="claude-3-5-haiku-latest")
parser = StrOutputParser()

chain = prompt | model | parser

result=chain.invoke({"word":"T1 VS AL"})
print(result)
