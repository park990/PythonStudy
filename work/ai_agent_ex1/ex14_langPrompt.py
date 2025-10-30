from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os

# env파일 읽기
load_dotenv()

# 채팅 모델 지정
chat_model = ChatAnthropic(model="claude-3-5-haiku-latest")

# 프롬프트 정의 - 시스템 메시지와 사용자메시지를 한번에 정의
chat_prompt_tmp = ChatPromptTemplate.from_messages(
    [
        ("system","당신은 1600년대 미국 흑인 노예제도의 흑인 노예 신분입니다. 식량을 얻어먹기 위한 간절한 마음으로 사용자의 질문에 최대 3줄로 답하세요"),
        ("human","{question}")
    ]
)

#출력 파서 정의
string_output_parser=StrOutputParser()
chain = chat_prompt_tmp|chat_model|string_output_parser

msg = input("질문:")
# 체인에 딕셔너리 입력
result = chain.invoke({"question":"{msg}"})
print(result)