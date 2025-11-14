"""
MCP서버는 스프링에서 RestAPI 서버를 만드는 것과 같다.

pip install "mcp[cli]"

npx @modelcontextprotocol/inspector  -->> 실행(venv)에서
"""

from mcp.server.fastmcp import FastMCP

# FastMCP생성
mcp_server = FastMCP("My MCP Server")

@mcp_server.tool() # 도구 정의
def hello(name:str = "World") -> str:  
    # 인사말 메시지를 반환하는 도구
    return f"안녕하세요!{name}님!"

@mcp_server.tool()
def get_prompt(prompt_type:str="general")->str:
    # 프롬프트를 준비해서 반환하는 도구
    prompt = {
        "general":"당신은 도움이 되는 AI어시스턴트 입니다. 사용자의 질문에 정확하고 친절하게 답변해주세요",
        "code_review":"검토하고 개선점을 제안해주세요. 코드의 가독성,성능",
        "translate":"다음 텍스트를 자연스러운 한국어로 번역해 주세요.",
        "summarize":"다음 내용을 핵심을 중심으로 간결하게 요약해 주세요"
    }
    return prompt.get(prompt_type, prompt["general"])

# 요청경로(endpoint) 등록
@mcp_server.resource("simple://info")
def get_server_info() -> str:
    # 서버 정보 제공
    return """ 
    my MCP Server정보
    -----------------

    이 MCP서버는 다음과 같은 기능을 제공합니다.
    - 인사말 메시지 제공
    - 프롬프트 제공
    
    제공하는 리소스(endpoint):
    - simple://info : 서버 정보 제공          
    """
if __name__ =="__main__":
    mcp_server.run(transport="streamable-http")