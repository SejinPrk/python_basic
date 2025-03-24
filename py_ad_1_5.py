#%% [markdown]
# # Chapter 1
# ## Advanced(1) - Context Manager(2)
# ### Keyword: Contextlib, __enter__, __exit__

#%%
# Contextlib - Measeure execution(타이머) 제작

# Ex1:  특정 코드 블록의 실행 시간을 측정하는 타이머 클래스 구현하기
# Use class
import time

class ExecuteTimer(object):
    def __init__(self, msg): # 결과 출력에 사용할 메시지를 저장
        self._msg = msg

    def __enter__(self):
        self._start = time.monotonic() # 시작 시간 기록 ->  with ... as v의 v에 할당
        return self._start

    def __exit__(self, exc_type, exc_value, exc_traceback): #  컨텍스트 매니저 종료 시 실행 -> 예외가 발생했는지 확인
        if exc_type:
            print("Logging exception {}".format((exc_type, exc_value, exc_traceback)))
        else:
            # 예외가 없을 경우 실행 시간 계산 및 출력
            # 현재 시간 - 시작 시간 = 실행에 걸린 시간
            print('{} : {} s'.format(self._msg, time.monotonic() - self._start))
        return True  # True 반환 시 예외를 정상 처리한 것으로 간주 (예외가 발생해도 프로그램이 계속 실행됨)

# ExecuteTimer 컨텍스트 매니저 사용
with ExecuteTimer('Start job!') as v:
    # v에는 __enter__()가 반환한 시작 시간 값이 할당됨
    print('Received start monotonic1 : {}'.format(v))
    # Execute job: 실행 시간을 측정할 작업 (300만 번 루프)
    for i in range(3000000):
        pass

    # 강제로 예외 발생시켜 __exit__의 예외 처리 기능 테스트
    raise Exception('Raise Exception!') # 이 예외는 __exit__에서 처리됨

