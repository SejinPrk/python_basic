#%% [markdown]
# # Chapter 1
# ## Advanced(1) - Context Manager(1)
# ### Keyword: Contextlib, __enter__, __exit__, exception
from typing import final

#%%
# 컨텍스트 매니저: 원하는 타이밍에 정확하게 리소스를 할당 및 제공, 반환하는 역할
# 가장 대표적인 with 구문 이해
# 정확한 이해 후 사용이 프로그래밍 개발에 중요 (문제 발생 요소)

#%%
# Ex1: try-finally로 파일을 열고 닫는 전통적인 방식
file = open('./testfile1.txt', 'w')
try:
    file.write('Context Manager Test1\nContextlib Test1.') # 메모장에 파일 하나 생성
finally:
    file.close() # 자원 낭비를 막기 위해 다시 돌려주기


# Ex2 - with 문: 자원 관리를 자동화하고 코드를 간결하게 만들기 위해서 사용
with open('./testfile2.txt', 'w') as f:
    f.write('Context Manager Test2\nContextlib Test2.')


# Ex3: 사용자 정의 클래스로 컨텍스트 매니저를 구현한 예시
# Use Class -> Context Manager with exception handling
class MyFileWriter():
    # 실행 순서
    def __init__(self, file_name, method): # 초기화
        print('MyFileWriter started : __init__')
        self.file_obj = open(file_name, method)

    def __enter__(self): # 진입
        print('MyFileWriter started : __enter__')
        return self.file_obj

    def __exit__(self, exc_type, value, trace_back): # 나가기
        print('MyFileWriter started : __exit__')
        if exc_type:
            print('Logging exception {}'.format((exc_type, value, trace_back)))
        self.file_obj.close()

# with문은 위와 동일한 작업을 진행하므로 try-finally 구문을 사용할 필요가 없어진다.
with MyFileWriter('./testfile3.txt', 'w') as f:
    f.write('Context Manager Test3\nContextlib Test3.')