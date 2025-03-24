#%% [markdown]
# # Chapter 1
# ## Python Advanced(2) - Lambda, Reduce, Map, Filter
# ### Keyword: Lambda, Reduce, Map, Filter

# lambda 장점: 익명, 힙 영역 사용 즉시 소멸, pythonic?, 파이썬 가비지 컬렉션(Count=0)
# 일반함수: 재사용성을 위해 메모리 저장
# 시퀀스형 전처리에 Reduce, Map, Filter를 주로 사용

#%%

# Ex1 - lambda
cul = lambda a, b, c: a * b + c
print('Ex1 >', cul(10, 15, 20))


# Ex2 - map
digits1 = [x * 10 for x in range(1, 11)]
print('Ex2 >', digits1)

# lambda를 사용하지 않을 경우 함수 선언 필요
# def ex2_func(x):
#     return x ** 2

result = list(map(lambda i: i ** 2, digits1)) # list로 cast(형변환)해야 결과 출력
print('Ex2 >', result)

# 모듈화
def also_square(nums):
    def double(x):
        return x ** 2
    return map(double, nums)

print('Ex2 >', list(also_square(digits1)))


# Ex3: filter - 원하는 값만 뽑아내기
digits2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(filter(lambda x: x % 2 == 0, digits2))
print('Ex3 >', result)

# 모듈화
def also_evens(nums):
    def is_even(x):
        return x % 2 == 0
    return filter(is_even, nums)

print('Ex3 >', list(also_evens(digits2)))


# Ex4: Reduce - 누적 합계 구하기 (python3부터 내장함수가 아니라 별도로 분리됨: import 필요)
from functools import reduce

digits3 = [x for x in range(1, 101)]

result = reduce(lambda x, y: x + y, digits3) # 최종 결과값 반환

print('Ex4 >', result)

# 모듈화
def also_add(nums):
    def add_plus(x, y):
        return x + y
    return reduce(add_plus, nums)

print('Ex4 >', also_add(digits3))