#%% [markdown]
# # Chapter 2
# ## Python Advanced(2) - Context Manager Annotation
# ### Keyword: @contextlib.contextmanager, __enter__, __exit__

#%%
# 가장 대표적인 with 구문 이해
# Contextlib Decorator 사용
# 코드 직관적, 예외 처리 용이성

# 외부 패키지 임포트
import contextlib
import time

# Ex1
# Use Decorator
@contextlib.contextmanager
def my_file_writer(file_name, method):
    f = open(file_name, method)
    # yield: 제너레이터(generator) 함수를 만들 때 사용
    yield f     # __enter__ 구문
    f.close()   # __exit__ 구문

with my_file_writer('testfile4.txt', 'w') as f:
    f.write('Context Manager Test4.\nContextlib Test4.')

# Ex2: timer - 코드 블록의 실행 시간을 측정
# Use Decorator

@contextlib.contextmanager
def ExecuteTimerDc(msg):
    start = time.monotonic()
    try:  # __enter__
        yield start
    except BaseException as e:
        print('Logging exception: {}: {}'.format(msg, e))
        raise # 예외를 다시 발생시켜 상위 코드로 전파
    else: # __exit__
        print('{}: {}s'.format(msg, time.monotonic() - start))

with ExecuteTimerDc("Start Job!") as v:
    print('Received start monotonic2: {}'.format(v))
    # Execute job.
    # 빈 반복문 4천만 번 실행
    for i in range(40000000):
        pass
    # 의도적으로 예외 발생
    # raise ValueError('occured')
