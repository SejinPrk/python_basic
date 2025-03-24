#%% [markdown]
# # Chapter 2
# ## Python Advanced(2) - Method Overloading
# ### Keyword: Overloading, OOP, multiple dispatch

#%%
# Method Overloading 사용의 장점
# 1. 동일 메서드 재정의
# 2. 네이밍 기능 예측 가능
# 3. 코드 절약, 가독성 향상
# 4. 메서드 파라미터 기반 호출 방식

# Ex1
# 동일 이름 메서드 사용 예제
# 동적 타입 검사 -> 런타임에 실행(타입 에러가 실행시에 발견)

class SampleA():
    def add(self, x, y):
        return x + y

    # 1. 이름은 동일하나 파라미터의 개수가 다른 메서드
    def add(self, x, y, z):
        return x + y + z

    # 2. 해결 방법: packing
    def add(self, *args):
        return sum(args)

a = SampleA()

# 동일한 이름의 메서드를 실행하면 가장 마지막 걸 실행함
# print('Ex1 >', a.add(2, 3)) # 1. 예외 발생! 파이썬에서는 클래스 내의 메서드 오버로딩을 지원하지 않음
# print('Ex1 >', a.add(2, 3, 4, 5, 6)) # 2. 패킹 후에는 에러가 나지 않음

# 모든 속성 개체 확인
print('Ex1 >', dir(a)) # 1. add가 한 개만 들어있는 것을 발견 가능


# Ex2
# 동일 이름 메서드 사용 예제
# 자료형에 따른 분기 처리
class SampleB():
    def add(self, datatype, *args):
        if datatype == 'int':
            return sum(args)

        if datatype == 'str':
            return ' '.join(x for x in args)

b = SampleB()

# 숫자 연산
print('Ex2 >', b.add('int', 5, 6))

# 문자 연산
print('Ex2 >', b.add('str', 'Hi', 'Python'))


# Ex3
# 패키지를 통한 메서드 오버로딩: 이름이 동일하더라도 아까와 달리 오류가 발생하지 않음
# 외부 패키지이기 때문에 가상환경에서 pip install 필요

from multipledispatch import dispatch

class SampleC():
    @dispatch(int, int)
    def product(x, y):
        return x * y

    @dispatch(int, int, int)
    def product(x, y, z):
        return x * y * z

    @dispatch(float, float, float)
    def product(x, y, z):
        return x * y * z

c = SampleC

# 정수 파라미터 2개
print('Ex3 >', c.product(5, 6))

# 정수 파라미터 3개
print('Ex3 >', c.product(5, 6, 7))

# 실수 파라미터 3개
print('Ex3 >', c.product(5.0, 6.0, 7.0))
