
"""
데이터를 수정하고 목적에 맞도록 가공이 편리한
파이썬 라이브러리 내부적으로 Numpy를 사용해서 숫자 데이터들의 연산이 상당히 원할하다.

분석할 데이터의 양(volume)이 커지고
데이터의 입출력 속도(velocity)가 빨라지고
데이터의 종류가 다양(Variety)한 정보들을 분석

위의 빅데이터 개념에서 분석할 때 많이 쓰이는 것이 pandas다.
Pandas를 이해하는데 있어 DataFrame을 이해해야 한다.

DataFrame이란??
MySQL과 같은 데이터베이스에서 보자면 하나의 테이블과 같은 것.

이런 테이블의 열을 의미하는 것이 바로 Series라고 함.
Series란 1차원배열과 같다.
List와 dict 같은 것들이 포함된다.
"""
import pandas as pd

ko = pd.Series([123,456,789,101112])
print(ko)

"""
만약! Pandas버전에 관련된 오류가 발생할 때...
>>
pip uninstall pandas

pip install pandas==1.0.1
<<
"""


