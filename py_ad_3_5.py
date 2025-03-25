#%% [markdown]
# # Chapter 3
# ## Python Advanced(3) - Descriptor(2)
# ### Keyword: descriptor vs property, low level(descriptor) vs high level(property)

#%%
"""
# Descriptor
# 1. 상황에 맞는 메서드 구현을 통한 객체 지향 프로그래밍 구현
# 2. Property와 달리 reuse(재사용) 가능
# 3. ORM Framework 사용
"""

# Ex1
# Descript 예제(1): 디렉토리 내 파일 개수를 계산하는 디스크립터
import os # 파일 시스템 작업을 위한 os 모듈 임포트

class DirectoryFileCount:
    # obj: 디스크립터를 소유한 객체 인스턴스(DirectoryPath의 인스턴스)
    # objtype: 디스크립터를 소유한 클래스(DirectoryPath)
    def __get__(self, obj, objtype=None):
        # print(os.listdir(obj.dirname)) # 디렉토리 내용 출력
        return len(os.listdir(obj.dirname)) # 디렉토리 내 파일/폴더 개수 반환

# 디스크립터를 사용하는 클래스 정의
class DirectoryPath:
        # Descriptor instance 생성
        size = DirectoryFileCount()

        def __init__(self, dirname):
            self.dirname = dirname # 인스턴스 변수에 디렉토리 경로 저장

# 현재 경로('.')
s = DirectoryPath('./')

# 이전 경로('..')
g = DirectoryPath('../')

# 클래스와 인스턴스 구조 확인을 위한 출력
# dir(): 객체가 가진 모든 속성과 메서드 이름을 리스트로 반환
print('Ex1 > ', dir(DirectoryPath))        # DirectoryPath 클래스의 모든 속성과 메서드
print('Ex1 > ', DirectoryPath.__dict__)    # DirectoryPath 클래스의 네임스페이스(사전)
print('Ex1 > ', dir(s))                    # s 인스턴스의 모든 속성과 메서드
print('Ex1 > ', s.__dict__)                # s 인스턴스의 네임스페이스(dirname만 포함)
print('Ex1 > ', dir(g))                    # g 인스턴스의 모든 속성과 메서드
print('Ex1 > ', g.__dict__)                # g 인스턴스의 네임스페이스(dirname만 포함)

# 디스크립터 동작 확인
# s.size 접근 시 DirectoryFileCount.__get__ 메서드 호출됨
print(s.size)  # 현재 디렉토리의 파일/폴더 개수 출력
print(g.size)  # 상위 디렉토리의 파일/폴더 개수 출력


# Ex2
# Descript 예제(2): 점수 로깅 디스크립터
import logging

logging.basicConfig(
    format='%(asctime)s %(message)s', # 시간과 메시지 포맷
    level=logging.INFO,                # 로그 레벨 설정 (INFO 이상)
    datefmt='%Y-%m-%d %H:%M:%S',       # 날짜 시간 포맷
)

class LoggedScoreAccess:
    def __init__(self, value=50):
        self.value = value

    def __get__(self, obj, objtype=None):
        # 로그 기록 - 접근 시점과 현재 값 기록
        logging.info('Accessing %r giving %r', 'score', self.value)
        return self.value

    def __set__(self, obj, value):
        # 로그 기록 - 업데이트 시점과 이전 값 기록
        logging.info('Updating %r giving %r', 'score', self.value)
        self.value = value

class Student:
    # Descriptor instance 생성
    # 모든 Student 인스턴스가 이 디스크립터를 공유함
    score = LoggedScoreAccess()

    def __init__(self, name):
        # Regular instance attribute
        # 인스턴스 변수로 학생 이름 저장
        self.name = name

# Student 인스턴스 생성
s1 = Student('Kim')
s2 = Student('Lee')

# 점수 확인 (s1)
print('Ex2 > ', s1.score) # 에러 발생!
s1.score += 20
print('Ex2 > ', s1.score)

print('Ex2 > ', s2.score) # 에러 발생!
s2.score += 30
print('Ex2 > ', s2.score)

# __dict__ 확인 - 인스턴스 변수만 포함됨 (score는 클래스 변수이므로 __dict__에 없음)
print('Ex2 > ', vars(s1))  # vars()는 __dict__와 동일
print('Ex2 > ', vars(s2))
print('Ex2 > ', s1.__dict__)
print('Ex2 > ', s2.__dict__)

# 클래스 변수 vs 인스턴스 변수:
# size와 score는 클래스 변수로, 해당 클래스의 모든 인스턴스에서 공유된다.
# dirname과 name은 인스턴스 변수로, 각 인스턴스마다 독립적인 값을 가진다.
# 따라서, __dict__ 또는 vars()를 통해 확인할 수 있는 것은 인스턴스 변수뿐이다.