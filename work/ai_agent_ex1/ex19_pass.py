"""
Runnable의 기능중 RunnablePassthrough는 입력되는 데이터를
그대로 통과 시키는 것이며 이는 나중에 데이터 흐름제어에 유용하다.
"""
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_anthropic import ChatAnthropic
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

prompt =ChatPromptTemplate.from_messages([
    ("human","주어지는 '{word}'와 유사한 단어 3개를 나열해줘, 단어만 부탁해")
])

model = ChatAnthropic(model="claude-3-5-haiku-latest")
parser = StrOutputParser()

# 병렬처리 체인 구성
chain =RunnableParallel({
    "original":RunnablePassthrough(), # 원본 데이터 보존
    "processed": prompt | model | parser # 처리 
})

# 실행부분
result = chain.invoke({"word":"인공지능"})
print(result) 