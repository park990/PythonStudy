"""
웹 기반으로 서비스를 구현해 보자
pip install "fastapi[standard]"
pip install python-multipart unicorn
    -fastapi: 웹서버
    -python-multipart: 파일 업로드 처리에 필요한 패키지
    -unicorn: 웹 서버 실행 라이브러리    
"""
import anthropic
import os
from dotenv import load_dotenv
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import unicorn
import uvicorn

# .env파일 로드
load_dotenv()

# 환경변수 파일에서 API키 가져오기
api_key = os.getenv("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=api_key)

app = FastAPI() # 웹서버 어플리케이션 생성
list = [] # 대화내용들을 저장할 List

@app.get("/", response_class=HTMLResponse)
async def get_root(): # 웹에서 표현될 페이지 표현
    chat_history=""
    # 대화기록을 역할에 따라 구분해 HTML 문자열을 구성
    for msg in list:
        if msg["role"] == "user":
            chat_history += f"<p><Strong>사용자:</Strong> {msg["content"]}</p>"
        elif msg["role"] == "assistant":
            chat_history += f"<p><Strong>ChatJAEPT:</Strong> {msg["content"]}</p>"
    html_content = f'''  
                    <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Document</title>
                </head>
                <body>
                    <h1>챗봇과 대화하기</h1>
                    <div id = "chat-history">
                        {chat_history}
                    </div>
                    <form action="/chat" method="post">
                        <input type="text" name="user_message" placeholder="메시지를 입력하센요" required/>
                        <button type="submit">전송</button>
                    </form>
                        
                </body>
                </html>
    '''
    return html_content


    

# 어린왕자 페르소나 프롬프트(System prompt)
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
    "항상 간결하게 답변해줘 기어야 두 세 문장으로 답변해주고, 어린 왕자의 순수함과 지혜를 반영해줘. 복잡한 주제도 본질적으로 단순화하여 설명해줘"
)
def chatbot_response(msg):
    response = client.messages.create(
        model="claude-3-5-haiku-latest",
        max_tokens=1024,
        system=persona_prompt, # system파라미터로 프롬프트 유형전달
        messages=msg
    )
    return response.content[0].text

@app.post("/chat",response_class=HTMLResponse)
async def post_chat(user_message:str=Form(...)):
    #user_message:str=Form(...) : 사용자가 form-data로 전송한 text를 받는다.
    list.append({"role":"user","content":user_message})
    result = chatbot_response(list)
    list.append({"role":"assistant","content":result})
    return await get_root()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1",port=8000)
    
