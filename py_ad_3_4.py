#%% [markdown]
# # Chapter 3
# ## Python Advanced(3) - Descriptor(1)
# ### Keyword: Descriptor, Get, Set, Del, Property

#%%
"""
# Descriptor
# 1. 객체에서 서로 다른 객체를 속성값으로 가지는 것
# 2. Read, Write, Delete 등을 미리 정의 가능
# 3. data descriptor(set, del), non-data descriptor(get)
# 4. 읽기 전용 객체 생성 장점, 클래스를 의도하는 방향으로 생성 가능
"""

# Ex1
# 기본적인 Descrpitor 예제
# 디스크립터 프로토콜: __get__, __set__, __delete__ 메서드 중 하나 이상을 구현

class DescriptorEx1(object):
    def __init__(self, name='Default'):
        # 디스크립터 객체의 초기 상태를 설정
        self.name = name

    # __get__ 메서드: 속성값을 읽을 때 호출됨
    # obj: 디스크립터를 소유한 객체(여기서는 Sample1의 인스턴스)
    # objtype: 디스크립터를 소유한 클래스(여기서는 Sample1)
    def __get__(self, obj, objtype):
        return 'Get method called. -> self : {}, obj : {}, pbjtype : {}, name : {}'.format(self, obj, objtype, self.name)

    # __set__ 메서드: 속성값을 변경할 때 호출됨
    # obj: 디스크립터를 소유한 객체
    # name: 설정하려는 새 값
    def __set__(self, obj, name):
        print('Set method called.')
        # 타입 체크를 통한 데이터 검증 - 디스크립터의 주요 용도 중 하나
        if isinstance(name, str):
            self.name = name
        else :
            # 문자열이 아닌 값으로 설정하려고 하면 예외 발생
            raise TypeError('Name should be string.')


    # __delete__ 메서드: 속성을 삭제할 때 호출됨
    # obj: 디스크립터를 소유한 객체
    def __delete__(self, obj):
        print('Delete method called.')
        # 속성 삭제 시 name을 None으로 설정
        self.name = None

# Sample1 클래스 - 디스크립터 사용 예시
class Sample1(object):
    # 클래스 변수로 디스크립터 인스턴스를 할당
    # 이 디스크립터는 Sample1의 모든 인스턴스에서 name 속성 접근을 관리함
    name = DescriptorEx1()

# Sample1 인스턴스 생성
s1 = Sample1()

# __set__ 호출
s1.name = 'Descriptor Test1'

# 예외 발생! Name should be string
# s1.name = 10

# attr 확인
# __get__ 호출
print('Ex1 > ', s1.name)

# __delete__ 호출
del s1.name

# 재확인
# __get__ 호출
print('Ex1 > ', s1.name) # name: None으로 바뀜

print()
print()


# Ex2
# Property 클래스 사용 Descriptor 직접 구현
# class property(fget=None, fset=None, fdel=None, dec=None)
# property는 디스크립터를 더 쉽게 구현할 수 있게 해주는 내장 클래스

class DescriptorEx2(object):
    def __init__(self, value):
        # 언더스코어를 붙여 내부 변수임을 표시
        # 이렇게 하면 외부에서 직접 접근하지 않는 것이 관례
        self._name = value

    def getVal(self):
        return 'Get method called. -> self : {}, name : {}'.format(self, self._name)

    def setVal(self, value):
        print('Set method called.')
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError('Value should be string.')

    def delVal(self):
        print('Delete method called.')
        self._name = None

    # property 객체 생성 및 name 속성에 할당
    # property(getter, setter, deleter, 문서화 문자열)
    # 이렇게 하면 name 속성에 접근할 때 위의 메서드들이 자동으로 호출됨
    name = property(getVal, setVal, delVal, 'Property 테스트를 하는 name 필드입니다. 의미는 없습니다.')

# DescriptorEx2 인스턴스 생성
s2 = DescriptorEx2('Descriptor Test2')

# 최초 값 확인
print('Ex2 > ', s2.name)

# setVal 호출
s2.name = 'Descriptor Test2 Method.'

# 예외 발생
# s2.name = 10

# getVal 호출
print('Ex2 > ', s2.name)

# delVal 호출
del s2.name

# 재확인
# __get__ 호출
print('Ex2 > ', s2.name) # name: None으로 바뀜

# 속성의 문서화 문자열 확인 Doc
# property의 네 번째 인자로 전달한 문자열이 __doc__ 속성에 저장됨
print('Ex2 > ', DescriptorEx2.name.__doc__)
