"""
랭체인에서는 프롬프트를 객체로 관리하도록 PromptTemplate을 제공함.
PromptTemplate : 변수를 포함하는 템플릿을 정의하여 동적 프롬프트를 생성함.

PromptTemplate유형
1) PromptTemplate : 기본이며 단일 문자열 프롬프트 생성
2) ChatPromptTemplate : 채팅모델을 위한 템플릿
3) PipelinePromptTemplate : 여러 프롬프트들을 연결하여 하나의 프롬프트로 구성
4) FewShotPromptTemplate : 모델에게 작업 수행 예시를 프롬프트에게 동적으로 포함

PromptTemplate 생성법
1) from_template() : 문자열로 바로 생성
2) 생성자 호출 : 변수목록, 템플릿을 명시하여 세밀한 제어 가능
3) load_prompt() : 파일에서 템플릿을 불러올 수 있음
"""

from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template(
    "너는 대한민국의 로또 분석 전문가야\n질문:{question}\n답변:"
)
print(template.format(question="이번 주 당첨가능한 번호를 5개만 추천해줘"))