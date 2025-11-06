"""
클로드나 GPT와 같은 LLM을 한 단계 더 똑똑하게 만드는 핵심적인 것이 리트리버(Retriever)와
RAG(Retrieval Augmented Generation) 검색 증강 생성 이다.
pip install langchain langchain-community
pip install duckduckgo-search==8.0.2
pip install -U ddgs
"""

from langchain_community.tools import DuckDuckGoSearchResults
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
import time 
import os
from dotenv import load_dotenv

load_dotenv()

class RealtimeWebRAG:
    """실시간 웹 검색을 활용하는 RAG"""
    def __init__(self):
        self.search = DuckDuckGoSearchResults()
        self.llm = ChatAnthropic(
            model="claude-sonnet-4-20250514",
            api_key=os.getenv("ANTHROPIC_API_KEY"),
            temperature=0 # 다양성과 창의성을 조절하는 값(0~1)
        )
        
        message = """
            웹에서 검색한 최신 정보를 바탕으로 답변하세요.
            검색결과: 
            {search_results}
            
            질문: {question}
            
            중요: 검색 결과에 있는 정보만 사용하여 답변하세요.
            답변:
        """
        self.qa_prompt = ChatPromptTemplate.from_messages([
            ("human",message)
        ])
        
    def answer(self,question):
        """ 실시간 검색 후 답변 생성"""
        # 1. 웹검색 
        print(f"검색중{question}")
        search_results = self.search.run(question)
        
        time.sleep(5) # 5초대기로 rate limit 방지
        
        # 2. Claude로 답변 생성 
        qa_chain = self.qa_prompt|self.llm
        answer = qa_chain.invoke({"search_results":search_results,
                                    "question":question})
        
        return answer
        
# 사용 예시
if __name__ == "__main__":
    web_rag = RealtimeWebRAG() # 생성자가 구동되어 search, llm, qa_prompt가 만들어짐
    
    # 최신 정보 질문 List로 준비하자
    questions = ["오늘 주요 뉴스는?","한국 야구 순위는","최신 AI기술 동향은?"]
    
    for q in questions:
        print(f"\n질문:{q}")
        try:
            answer =web_rag.answer(q)
            print(f"답변:{answer.content}\n")
        except Exception as e:
            print(f"오류발생:{e}\n")    