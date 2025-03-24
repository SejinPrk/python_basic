#%% [markdown]
# # Chapter 1
# ## Python Advanced(1) - Python Variable Scope
# ### Keyword: scope, global, nonlocal, locals, globals...

#%%
# 전역변수는 주로 변하지 않는 고정값에 사용
# 지역변수 사용 이유: 지역변수는 함수 내에 로직 핵결에 국한, 소멸주기: 함수 실행 해제 시
# 전역변수를 지역 내에서 수정하는 것은 권장하지 않음

a = 10  # Global variable

def foo():
    # Read global variable
    print('Ex1 >', a)

foo()

# Read global variable
print('Ex1 >', a)


# Ex2
b = 20

def bar():
    b = 30 # Local variable
    print('Ex2 >', b) # Read Local Variable

bar() # scope 안에서 먼저 찾고 없으면 바깥으로 나가기 때문에 20이 출력될 것
print('Ex2 >', b) # Read global variable


# Ex3
c= 40

def foobar():
    # c = c + 10 # UnboundLocalError 발생!
    # c -= 10
    # c += 100
    print('Ex3 >', c)

foobar()


# Ex4
d = 50

def barfoo():
    global d # global이라는 예약어 사용
    d = 60
    d += 100
    print('Ex4 >', d)

barfoo()

print('Ex4 >', d)


# Ex5 (중요 - 기술 면접, 코테)
def outer():
    e = 70 # 상위 Local Variable
    def inner():
        nonlocal e
        e += 10 # 하위 Local Variable -> nonlocal e 예약어 없이 상위 지역 변수를 수정 불가
        print('Ex5 >', e)
    return inner

in_test = outer() # Closure

in_test() # UnboundLocalError 발생! -> nonlocal e 추가로 해결 完
in_test()
in_test() # 한 번 더 실행할 때마다 10씩 증가


# Ex6
def func(var):
    x = 10
    def printer():
        print('Ex6 >', "Printer Func Inner")
    print('Func Inner', locals()) # 지역 전체 출력

func('Hi') # Dictionary 형식으로 출력 가능


# Ex7
print('Ex7 >', globals()) # 지금까지 선언했던 모든 걸 출력: 전역 전체 출력
globals()['test_variable'] = 100
print('Ex7 >', globals())

# Ex8 (지역 -> 전역 변수 생성)
for i in range(1, 10):
    for k in range(1, 10):
        globals()['plus_{}_{}'.format(i, k)] = i + k

print(globals())
print('Ex8 >', plus_5_5) # 10
print('Ex8 >', plus_9_9) # 18