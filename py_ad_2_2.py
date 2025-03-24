#%% [markdown]
# # Chapter 2
# ## Python Advanced(2) - Property(1) - Underscore
# ### Keyword: access modifier(접근지정자), underscore

#%%
# 다양한 언더스코어 활용
# 파이썬 접근지정자 설명

# Ex1
# Use underscore
# 1. 인터프리터 2. 값 무시 3. 변수 네이밍(국제화, 자릿수)

# Unpacking - 값을 무시할 때 사용
x, _, y = (1, 2, 3)
print(x, y) # 2번째 값을 무시한 채 1과 3만 출력됨

a, *_, b = (1, 2, 3, 4, 5)
print(a, b) # 2, 3, 4는 무시된 채 1과 5만 출력됨

a, *i, b = (1, 2, 3, 4, 5)
print(i)

print('Ex1 > ', x, y, a, b)

for _ in range(10):
    pass

for _, val in enumerate(range(10)):
    pass
print(val)


# Ex2
# 접근지정자 self.변수명
# name : public 변수
# _name : protected
# __name : private
# 파이썬 -> Public 강제 x, 약속된 규약에 따라 코딩 장려(자율적, 책임감 장려)
# 타 클래스(클래스 변수, 인스턴스 변수 값 쓰기 장려하지 않음) -> Naming Mangling
# 타 클래스 __ 접근하지 않는 것이 원칙

# No use Property
class SampleA:
    def __init__(self):
        self.x = 0    # public 변수
        self.__y = 0  # private 변수
        self._z = 0   # protected 변수

a = SampleA()

a.x = 1

print('Ex2 > x : {}'.format(a.x))
# print('Ex2 > y: {}'.format(a.__y)) # error! - 비공개 변수에 대해 Naming Mangling 사용하기 때문
print('Ex2 > z: {}'.format(a._z))

print('Ex2 > ', dir(a))

a._SampleA__y = 2
print('Ex2 > y : {}'.format(a._SampleA__y))


# Ex3
# method 활용: Getter, Setter
class SampleB:
    def __init__(self):
        self.x = 0
        self.__y = 0 # _SampleB__y로 치환
        self._z = 0


    # 값을 반환하는 Getter 메서드
    def get_y(self):
        return self.__y

    # 값을 설정하는 Setter 메서드
    def set_y(self, value):
        self.__y = value

# b._SampleB__y = SampleB() # 여전히 private 변수에 직접 접근이 가능

b = SampleB()

b.x = 1
b.set_y(2)

print('Ex3 > x : {}'.format(b.x))
print('Ex3 > y : {}'.format(b.get_y()))

# 변수 접근 후 수정 부분에서 일관성 및 가독성이 하락
b._SampleB__y = 343 # 가독성 하락

print('Ex3 > ', dir(b))
