"""
LLM은 매우 똑똑하지만 모든 지식은 글로만 배움. 
지난 몇년동안 가장 많이 사용하고 학슥한 도구가 DB와 WebBrowser다
랭체인에서는 보다 편리하게 도구를 LLM과 연계할 수 있도록 기능을 제공
4단계로 구현하는데
1. 도구생성: LLM이 사용할 도구를 준비하는 단계
2. 도구연결: LLM에게 도구를 연결(Binding) 하는 단계
3. 도구호출: LLM이 사용할 도구를 선택하는 단계
4. 도구실행: 실제로 LLM이 도구를 실행하고 작업하는 단계

- @tool 어노테이션(데코레이터)를 사용한 도구생성
"""
import random
from langchain.tools import tool
from langchain_anthropic import ChatAnthropic
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

# 가위, 바위, 보 게임을 위한 tool 정의
@tool
def rock_paper_scissor()-> str:
    """
    사용자가 가위바위보 게임을 요청할 때, 컴퓨터의 선택(가위, 바위, 보 중 하나)을 결정하여 반환합니다.
    """
    return random.choice(["가위","바위","보"])

# Tool 이 바인딩된 LLM 지정
llm = ChatAnthropic(model="claude-3-5-haiku-latest").bind_tools([rock_paper_scissor])

llm_chat = ChatAnthropic(model="claude-3-5-haiku-latest") # 해설용 LLM
print(llm) #llm이 tool을 binding했는지 확인

#승부판정
def judge(user_choice, computer_choice):
    #가위,바위,보 승패를 판정합니다.
    user_choice=user_choice.strip()
    computer_choice = computer_choice.strip()
    if user_choice == computer_choice:
        return "무승부"
    elif (user_choice, computer_choice) in [
        ("가위","보"),
        ("바위","가위"),
        ("보","바위")
    ]:
        return "승리"
    else:
        return "패배"
# 게임 루프
print("가위,바위,보 (종료:q)")
while (user_input := input("\n 가위, 바위, 보 : ")) != "q":
    # LLM에게 tool 호출 
    ai_msg = llm.invoke(f"가위 바위 보 게임: 사용자가 {user_input}를 냈습니다. rock_paper_scissor tool을 사용하세요")
    
    #tool 호출 확인 및 실행
    if ai_msg.tool_calls:
        print(type(rock_paper_scissor))
        computer_choice=rock_paper_scissor.invoke("")    
        print(f"LLM이 선택한 도구: {computer_choice}")
        result = judge(user_input, computer_choice)
        
        print(f"승부: {result}")
        
        # 결과를 해설응답 생성
        final = llm_chat.invoke(
            f"가위,바위,보 게임 결과를 재미있게 해설해 주세요"
            f"사용자:{user_input}, AI:{computer_choice}, 결과:사용자의 {result}"
        )
        print(final)
        print(f" -LLM해설: {final.content}")    
        print(f"게임 요약: 유저({user_input} VS AI({computer_choice})=>{result})")
    
    else:
        print("tool호출 실패")