import anthropic
import os
from dotenv import load_dotenv
import asyncio

class ClaudeAgent:
    def __init__(self,name,inst,handoffs=None):
        self.name=name
        self.inst=inst
        self.handoffs=handoffs or []
        
        

class Runner:
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    @classmethod
    async def run(cls,agent,message,previous_response_id=None):
        #핸드오프 판단을 위한 프롬프트
        if agent.handoffs:
            handoff_info="\n".join([f"-{h.name} : {h.inst}" for h in agent.handoffs])
            prompt = f"""
            {agent.inst}
            
            사용 가능한 전문의:
            {handoff_info}
            
            환자메시지 : {message}
            
            이 환자를 다른 전문의에게 보내야 하는지 판단하고 필요하면
            "핸드오프:[전문의 이름] 으로 시작하여 답변하세요"
            그렇지 않으면 직접 답변하세요.
            """
        else:
            prompt = f"""
            {agent.inst}
            환자 메시지:{message}
            
            위 지시사항에 따라 응답해 주세요
            """
        response = cls.client.messages.create(
            model = "claude-3-5-haiku-latest",
            max_tokens=500,
            messages=[{"role":"user","content":prompt}]
        )    
        output = response.content[0].text
        
        #핸드오프 체크
        last_agent = agent
        if output.startswith("핸드오프:"):
            handoff_target =output.split("핸드오프")[1].split("\n")[0].strip()
            for handoff_agent in agent.handoffs:
                if handoff_agent.name in handoff_target:
                    last_agent=handoff_agent
                    # 핸드오프된 에이전트로 다시 실행
                    new_response = cls.client.messages.create(
                        model = "claude-3-5-haiku-latest",
                        max_tokens=500,
                        messages=[{"role":"user",
                                   "content":f"{handoff_agent.inst}\n\n환자메시지:{message}"}]                        
                    )
                    output = new_response.content[0].text
                    break
        class Result:
            def __init__(self,final_output,last_agent,last_response_id):
                self.final_output=final_output
                self.last_agent=last_agent
                self.last_response_id=last_response_id
                
        return Result(output, last_agent, "response_"+str(hash(output)))
async def simple_handoff_example():
    print("Agent 병원 안내 시스템\n")
    print("--------------------------------*2")
    
    
    # 정형외과 전문의 에이전트
    doctor1 = ClaudeAgent(
        name="정형외과 전문의",
        inst="근골격계 문제(허리 통증, 관절염, 골절 등)을 진료 합니다. 코 귀 진료는 이비인후과로... 감기등은 내과로..."
    )
    
    # 이비인후과 전문의
    doctor2 = ClaudeAgent(
        name="이비인후과 전문의",
        inst="코,귀의 질환을 진료합니다. 근골격계 문제는 정형외과로... 감기등 은 내과로..."
    )
    
    # 내과 전문의
    doctor3 = ClaudeAgent(
        name ="내과 전문의",
        inst="내과 질환 (감기,소화불량,두통등) 진료합니다. 근골격계 문제는 정형외가로.. 코 귀의 질환은 이비인후과로..."
    )
    
    # 병원 안내 에이전트
    desk = ClaudeAgent(
        name = "병원 안내",
        inst=""" 
        환자의 증상을 듣고 적절한 전문의 에게 연결합니다.
        - 감기 증상, 소화 불량, 두통 등 -> 내과
        - 허리통증, 관절, 골격, 근육 등-> 정형외과
        - 코, 귀 등-> 이비인후과
        """,
        handoffs = [doctor1, doctor2, doctor3]
    )    
    
    # 핸드오프 테스트
    response_id =None
    current_agent =desk
    conversations = [
        "안녕하세요! 며칠 전 부터 두통이 있습니다.",
        "커피를 마시면 아파요, 허리도 아프고",
        "운동을 하면 좋아질까요"
    ]
    
    for msg in conversations:
        print(f"\n 환자:{msg}")
        
        # 이전 대화가 있으면 response_id 를 전달
        if response_id:
            result = await Runner.run(
                current_agent,msg,previous_response_id=response_id
            )
        else:
            result = await Runner.run(current_agent,msg)
            
        response_id = result.last_response_id
        # 핸드오프가 발생한 경우 에이전트를 변경
        if current_agent != result.last_agent:
            print(f"<핸드오프 발생> {current_agent.name}에서 {result.last_agent.name}로 핸드오프")
            current_agent = result.last_agent
        print(f"<Agent병원> {current_agent.name} : {result.final_output}")
        
if __name__ == "__main__":
    asyncio.run(simple_handoff_example())
                