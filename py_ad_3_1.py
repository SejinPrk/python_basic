#%% [markdown]
# # Chapter 3
# ## Python Advanced(3) - Meta Class(1)
# ### Keyword: Class of Class, Type, Meta Class, Custom Meta Class
#%%
"""
# MetaClass
# 1. 클래스를 만드는 역할 -> 의도하는 방향으로 클래스를 커스텀
# 2. 프레임워크 작성 시 필수
# 3. 동적 생성(type), 커스텀 생성(type) 함수
# 4. 커스텀 클래스 -> 검증 클래스 등
# 5. 엄격한 클래스 사용 요구, 메서드 오버라이드 요구
"""

# Ex1
# type 예제
class SampleA(): # Class == Object
    pass

obj1 = SampleA() # 변수에 할당, 복사 가능, 새로운 속성, 함수의 인자로 넘기기 가능

# obj1 -> SampleA instance
# SampleA -> type meta class : 모든 클래스의 메타는 타입 클래스
# type -> type meta class : 타입은 그 자체가 메타
print('Ex1 > ', obj1.__class__)
print('Ex1 > ', type(obj1)) # obj1의 타입: SampleA
print('Ex1 > ', obj1.__class__ is type(obj1)) # true: 부모와 동일

print('Ex1 > ', obj1.__class__.__class__) # 모든 클래스의 메타(원형): type
print('Ex1 > ', obj1.__class__.__class__ is type(obj1).__class__) # true: 둘다 타입 클래스로 동일

print(type.__class__) # type => 핵심 개념


# Ex2
# type meta(Ex1 증명)

#int, dict
n = 10
d = {'a':10, 'b': 20}

class SampleB():
    pass

obj2 = SampleB()

for o in (n, d, obj2):
    print('Ex2 > {} {} {}'.format(type(o), type(o) is o.__class__, o.__class__.__class__))

print()

for t in int, float, list, tuple:
    print('Ex2 > ', type(t)) # type

print('Ex2 > ', type(type))  # type