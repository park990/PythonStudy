"""
Pydantic은 LLM에게 모델을 지정하여 해당스키마를 기반으로 응답형식을 지정할 수 있다.
pip install pydantic
"""

from pydantic import BaseModel, Field
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

llm = init_chat_model("claude-3-5-haiku-latest", model_provider="anthropic")
class StockReview(BaseModel):
    """ 주식 평가 스키마 정의 """
    name:str=Field(description="종목 이름")
    market_capitalization:int=Field(description="한국시장 몇등(예:3등)")
    estimation:str=Field(description="평가내용(3~4문장)")
    futurePrice:int=Field(description="예상 목표가(예:18만원)")
    
    
# 모델에 스키마 바인딩
structured_llm=llm.with_structured_output(StockReview)

# llm의 실행 결과가 StockReview 타입으로 넘어옴
result : StockReview = structured_llm.invoke(
    "주식 종목 '삼성전자'에 대한 평가를 작성해 주세요"
)

print("종목이름:", result.name)
print("시총 순위:", result.market_capitalization)
print("평가 내용:", result.estimation)
print("예상 목표가:", result.futurePrice)
