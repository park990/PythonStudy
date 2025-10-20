"""_summary_

초기자: def __init__(self):
소멸자: def __del__(self):
생략되어 있어서 보이진 않지만 자동으로 정의된다.

위는 생략되어 있어 보이진 않지만 자동으로 정의된다.
"""

class MyClass: # 클래스 정의 시작
    def setName(self,n): # 멤버메서드(기능,동작) 정의
        self.name=n #현재 객체가 가지고 있는 name이라는 변수에 인자 n의 값을 대입
    
    def getName(self):
        return self.name