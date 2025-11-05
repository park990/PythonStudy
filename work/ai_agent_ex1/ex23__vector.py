"""
랭체인의 핵심: 임베딩과 벡터스토어
- 임베딩: 인간의 언어를 컴퓨터(LLM)가 이해할 수 있는 숫자의 배열로 바꾸는 것
그냥 단순히 배열로 변환만 하는 것은 크게 의미가 없다. 즉, 임베딩은 벡터스토어와 
함께 사용해야 의미가 생긴다.

현재 클로드를 사용하기 때문에 임베딩은 하지 못한다.
클로드가 임베딩을 지원하지 않기 때문
단순히 벡터스토어를 활용해보자.
- pip install scikit-learn
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 자료들(문서들)
docs = ["벡터 검색", "딥러닝 신경망", "머신러닝 인공지능", "파이썬 프로그래밍", "자연어 처리"]

# 벡터화 - 클로드는 임베딩을 지원하지 않는다.
vectorizer = TfidfVectorizer()
doc_vectors = vectorizer.fit_transform(docs)

# 검색 함수
def search(query):
    query_vector = vectorizer.transform([query])
    scores = cosine_similarity(query_vector, doc_vectors)[0]
    # 두 벡터 사이의 코사인 유사도를 계산하는 함수
    # 뒤에 [0]: query_vector가 1개뿐이라 결과가 2차원 배열이기 때문

    # 결과 출력
    print(f"검색어: '{query}'")
    for i, score in enumerate(scores):
        print(f"{docs[i]} -> {score:.3f}")

# 테스트
v1 = input("입력:")
search(v1)
print()
search("이미지")