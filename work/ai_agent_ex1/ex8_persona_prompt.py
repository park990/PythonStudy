import anthropic
import os
from dotenv import load_dotenv

# .env파일 로드
load_dotenv()

# 환경변수 파일에서 API키 가져오기
api_key = os.getenv("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=api_key)

# 어린왕자 페르소나 프롬프트
persona_prompt = (
    "너는 생테쥐베르 소설에 나오는 어린 왕자야. 너는 순수하고 호기심이 많으며, 세상을 탐험하는 것을 좋아해. "
    "너는 사람들과 쉽게 친구가 되고, 그들에게 따뜻한 조언을 해주는 것을 즐겨. "
    "너는 항상 긍정적이고 낙천적인 태도를 유지하며, 작은 것에서도 행복을 찾으려고 해. "
    "너는 별과 꽃, 그리고 사막에 대해 이야기하는 것을 좋아해. "
    "너는 사람들에게 진정한 우정과 사랑의 중요성을 가르쳐주려고 해."
    "너는 어린 왕자의 관점에서 세상을 바라보고, 그 특유의 순수함과 지혜로 대화를 이끌어가야 해."
    "다음의 특성을 따라 대답해줘:\n"
    "1. 순수하고 호기심 많은 태도 유지\n"
    "2. 긍정적이고 낙천적인 언어 사용\n"
    "3. 별, 꽃, 사막에 대한 비유와 이야기 활용\n"
    "4. '어째서?'라는 질문을 자주 사용하여 대화 유도\n"
    "5. '어른들은 참 이상해요'라는 표현 자주 사용\n"
)

def chatbot_response(msg):
    response = client.messages.create(
        model="claude-3-5-haiku-latest",
        max_tokens=1024,
        system=persona_prompt, # system파라미터로 프롬프트 유형전달
        messages=msg
    )
    return response.content[0].text

if __name__ == "__main__":
    list = []
    while True:
        user_message = input("메세지:") # 키보드로 입력
        if user_message.lower() == "exit":
            print("대화가 종료되었습니다.")
            break

        list.append({"role":"user", "content":user_message})
        result = chatbot_response(list)
        print("챗봇:"+result)
        list.append({"role":"assistant", "content":result})