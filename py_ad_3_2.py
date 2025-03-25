#%% [markdown]
# # Chapter 3
# ## Python Advanced(3) - Meta Class(2)
# ### Keyword: Type(name, base, dct), Dynamic metaclass

#%%
"""
# MetaClass
# 1. 메타클래스 동적 생성 중요
# 2. 동적 생성한 메타클래스 -> 커스텀 메타클래스 생성
# 3. 의도하는 방향으로 직접 클래스 생성에 관여할 수 있는 큰 장점
"""

# Ex1
# TYPE 동적 클래스 생성 예제

# 아래 둘은 동일
# class a():
# class a(object):

# Name(아름), Bases(상속), Dct(속성, 메서드)
s1 = type('sample1', (), {}) # 샘플1, 빈 튜플, 빈 딕셔너리

# 이 클래스와 동일한 클래스
# class sample1():
#     pass

print('Ex1 > ', s1)
print('Ex1 > ', type(s1))
print('Ex1 > ', s1.__base__) # Object
print('Ex1 > ', s1.__dict__)


# Ex2
# 동적 생성 + 상속
class Parent1:
    pass

s2 = type(
        'Sample2',
        (Parent1,),
        dict(attr1=100, attr2='hi')
    ) # {'attr1': 100, 'attr2': 'hi'}

# 이 클래스와 동일한 클래스
# class Sample2(Parent1):
#     attr1 = 100
#     attr2 = 'hi'

print('Ex2 > ', s2)                     # <class '__main__.Sample2'>
print('Ex2 > ', type(s2))               # <class 'type'>
print('Ex2 > ', s2.__base__)            # <class '__main__.Parent1'>
print('Ex2 > ', s2.__dict__)            # {'attr1': 100, 'attr2': 'hi', '__module__': '__main__', '__doc__': None}
print('Ex2 > ', s2.attr1, s2.attr2)     # 100 hi

print()


# Ex3
# type 동적 클래스 생성 + 메서드

class SampleEx:
    attr1 = 30
    attr2 = 100

    def add(self, m, n):
        return m + n

    def mul(self, m, n):
        return m * n

ex = SampleEx()

print('Ex3 > ', ex.attr1)
print('Ex3 > ', ex.attr2)
print('Ex3 > ', ex.add(100, 200))
print('Ex3 > ', ex.mul(100, 20))

print()

# 위 함수를 동적 클래스로 만들기
s3 = type(
        'Sample3',
        (object,),
        dict(attr1=30, attr2=100, add = lambda x, y: x + y, mul = lambda x, y: x * y)
        # {'attr1': 30, 'attr2': 100, 'add': lambda x, y: x + y, 'mul': lambda x, y: x * y}
    )

# 위와 동일한 결과 출력

print('Ex3 > ', s3.attr1)
print('Ex3 > ', s3.attr2)
print('Ex3 > ', s3.add(100, 200))
print('Ex3 > ', s3.mul(100, 20))
