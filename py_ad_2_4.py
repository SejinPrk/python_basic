#%% [markdown]
# # Chapter 2
# ## Python Advanced(2) - Method Overriding
# ### Keyword: Overriding, OOP, 다형성
from sqlite3.dbapi2 import Timestamp
from time import process_time_ns


#%%
# Method Overriding 사용의 장점
# 1. Sub class(자식)에서 Super class(부모)를 호출 후 사용
# 2. 메서드 재정의 후 사용 가능
# 3. 부모 클래스의 메서드를 추상화 후 사용가능 (구조적 접근)
# 4. 확장 가능, 다형성(다양한 방식으로 동작)
# 5. 가독성 증가, 오류 가능성 감소, 메서드 이름 절약

# Ex1
# 기본 Overriding 예제

class ParentEx1():
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value

class ChildEx1(ParentEx1):
    pass

c1 = ChildEx1()
p1 = ParentEx1()

# 부모 클래스 메서드 호출
print('Ex1 > ', c1.get_value())  # 상속받은 5 호출

# c1의 모든 속성 출력
print('Ex1 > ', dir(c1))

# 부모 & 자식 모든 속성 출력
print('Ex1 > ', dir(ParentEx1))
print('Ex1 > ', dir(ChildEx1)) # 부모, 자식 모두 동일

print('Ex1 > ', ParentEx1.__dict__)
print('Ex1 > ', ChildEx1.__dict__) # 자식에는 main함수, doc, 모듈만 담겨있음

# Ex2
# 기본 Overriding 메서드 재정의
class ParentEx2():
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value

class ChildEx2(ParentEx2):
    def get_value(self):
        return self.value * 10

p2 = ParentEx2()
c2 = ChildEx2()

# 자식 메서드 재정의 후 호출
print('Ex2 > ', c2.get_value()) # 5 * 10 = 50

# Ex3
# Overriding 다형성 예제
import datetime

class Logger(object):
    def log(self, msg):
        print(msg)

class TimestampLogger(Logger):
    def log(self, msg):
        message = "{ts} {msg}".format(ts=datetime.datetime.now(), msg=msg)
        # super().log(message) # shortcut 더 편한 로그
        super(TimestampLogger, self).log(message)

class DateLogger(Logger):
    def log(self, msg):
        message = "{ts} {msg}".format(ts=datetime.datetime.now().strftime('%Y-%m-%d'), msg=msg)
        super().log(message)
        # super(DateLogger, self).log(message)
#
l = Logger()
t = TimestampLogger()
d = DateLogger()

# 메서드 재정의 실행
# print('Ex3 > ', l.log('Called logger'))
# print('Ex3 > ', t.log('Called TimestampLogger'))
# print('Ex3 > ', d.log('Called DateLogger'))


l.log('Test1')
t.log('Test2')
d.log('Test3')
