from langchain_core.prompts import PromptTemplate

my_template =PromptTemplate(
    input_variables=["article","style"],
    template="다음기사를 {style} 스타일로 요약해줘 \n\n {article}"    
)
print(my_template.format(
    article="ISA계좌에 납입할 수 있는 금액은 연 2천만원까지이고, 이것을 3년마다 갱신하면 좋아",
    style="블로그"
))