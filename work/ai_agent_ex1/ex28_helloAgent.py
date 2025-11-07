import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

class ClaudeAgent:
    def __init__(self,name,inst):
        self.name = name # 지역변수(name) 의 값을 멤버변수(self.name)에 저장
        self.inst = inst
        self.client = anthropic.Anthropic(api_key = os.getenv("ANTHROPIC_API_KEY"))
        
    def run(self, user_input):
        # 프롬프트 구성
        prompt = f"""
        {self.inst}
        사용자 요청: {user_input}
        위 지시사항에 따라 응답해 주세요
        """
        
        # Claude응답 생성
        response = self.client.messages.create(
            model = "claude-sonnet-4-20250514",
            max_tokens=500,
            messages=[{"role":"user","content":prompt}] 
        )
        
        return response.content[0].text
    
# 에이전트 생성
hello_agent = ClaudeAgent(
    name = "HelloAgent",
    inst="당신은 밝은 성격의 접견자 입니다. 당신의 임무는 친절하게 첫 인사를 전하는 겁니다."
    
)        

# 에이전트 실행
result = hello_agent.run("안녕? 스페인어로만 인사해 주세요")

# 결과 출력
print(result)