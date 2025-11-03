from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch
from langchain_anthropic import ChatAnthropic
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

def is_english(x:dict) -> bool:
    """ 입력 딕셔너리의 'word'키에 해당하는 값이 영어인지 확인"""
    return all(ord(char) < 128 for char in x["word"]) 
 # x["word"]: dict에서 "word"라는 키의 문자열 값을 가져옴
 # for char in x["word"] :문자열의 각 문자를 하나씩 가져와서 반복수행
 # ord(char) : 해당 문자의 유니코드 숫자 값을 가져온다.
 # ord(char) < 128 : 아스키 코드 범위(0~127) 안에 있으면 True
 
# 영어일 때 사용할 프롬프트
english_prompt = ChatPromptTemplate.from_template(
    "Give me 3 synonyms of {word}. Only list the words"
)
# 한국어일 때 사용할 프롬프트
korean_prompt = ChatPromptTemplate.from_template(
    "주어진 '{word}' 와 유사한 단어 3개만 나열해줘"
)

# 모델정의
model = ChatAnthropic(model="claude-3-5-haiku-latest")
parser = StrOutputParser()
 
# 조건부 분기 
# is_english 함수가 true 를 반환하면 english_prompt를 사용하고 그렇지 않으면 
# korean_prompt를 사용하는 체인을 구성하자

chain = RunnableBranch(
    (is_english, english_prompt| model| parser), #영어일 때 실행하는 체인
    korean_prompt | model | parser # is_english가 false일 때 실행되는 체인
)
# 영어로 테스트
english_word ={"word":"spring"}
english_result =chain.invoke(english_word)
print(f"Synonyms of '{english_word['word']}' : \n{english_result}\n")

#한글로 테스트
korean_word ={"word":"크리스마스"}
korean_result =chain.invoke(korean_word)
print(f"Synonyms of '{korean_word['word']}' : \n{korean_result}\n")


