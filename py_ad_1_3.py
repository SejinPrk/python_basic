#%% [markdown]
# # Chapter 1
# ## Python Advanced(3) - Shallow Copy & Deep Copy
# ### Keyword: shallow & deep copy

#%%
# 객체의 복사 종류: Copy, Shallow Copy, Deep Copy
# 정확한 이해 후 사용 -> 프로그래밍 개발 중요 (문제 발생 요소)

# 가변(mutable): list, set, dict
# 불변(immutable): 그 외 나머지

# Ex1 - Copy
# Call by value, Call by reference, Call by share
# list: mutable
a_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
b_list = a_list # a_list 할당

print('Ex1 > ', id(a_list))
print('Ex1 > ', id(b_list)) # 서로 같은 id 값을 참조하고 있는 것을 확인 가능

b_list[2] = 100

print('Ex1 > ', a_list)
print('Ex1 > ', b_list) # b를 변경했어도 둘다 같은 곳을 바라보고 있기 때문에 a값까지 바뀜

b_list[3][2] = 100 # 6 -> 100

print('Ex1 > ', a_list)
print('Ex1 > ', b_list) # list 안의 list 변경 -> a 값까지 바뀜

# immutable: int, str, float, boolean, Unicode...

# Ex2 - Shallow Copy
import copy

c_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
d_list = copy.copy(c_list)

print('Ex2 > ', id(c_list))
print('Ex2 > ', id(d_list)) # 주소가 달라짐!

# 최상위 레벨의 요소 변경: 원본 리스트(c)에 영향을 주지 않음. 별도 객체.
d_list[1] = 100
print('Ex2 > ', c_list) # 바뀌지 않는다.
print('Ex2 > ', d_list) # d_list에서만 새로운 메모리 공간을 갖기 때문에 값이 바뀜 (복사본 같은 개념)

# 내부 리스트 [4, 5, 6], [7, 8, 9] 수정: 내부 리스트는 원본과 동일한 메모리 주소 참조. 동일 객체.
d_list[3].append(1000)
d_list[4][1] = 10000

print('Ex2 > ', c_list)
print('Ex2 > ', d_list) # 내부 리스트는 append(삽입)됨. 둘다 변경 -> Call by reference

# Ex3 - Deep Copy
e_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
f_list = copy.deepcopy(e_list) # 모든 중첩된 내부 객체들까지 완전히 새로운 메모리 공간에 복사

print('Ex3 > ', id(e_list))
print('Ex3 > ', id(f_list)) # 서로 다른 주소값 참조 -> Call by reference

f_list[3].append(1000)
f_list[4][1] = 10000

print('Ex3 > ', e_list) # e_list는 원본 그대로 유지
print('Ex3 > ', f_list) # f_list만 내부, 외부 둘다 변경됨

# 결과적으로 원본과 복사본은 완전히 독립적이며 서로 영향을 주지 않는다.
# Deep Copy가 성능상으로 메모리를 더 많이 잡아먹음