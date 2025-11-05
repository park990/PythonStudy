"""
벡터스토어를 활용하는 간단한 예제
pip install chromadb
pip install rich
pip install tenacity==8.2.3
pip install anthropic==0.49.0
pip install fastapi[standard]
pip install python-multipart unicorn
pip install langchain[anthropic]==0.3.27
pip install pydantic
pip install protobuf
"""
from dotenv import load_dotenv
import chromadb

# 클라이언트 생성
client = chromadb.Client()
collection = client.create_collection("my_db") # DB(스키마) 생성

# 문서 추가
collection.add(
    documents=["파이썬은 프로그래밍 언어", "머신러닝은 인공지능기술"],
    ids=["doc1","doc2"]
)

# 검색
results = collection.query(query_texts=["프로그래밍"], n_results=1)
print(results["documents"])