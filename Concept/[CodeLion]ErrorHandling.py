# Title         : [CodeLion]ErrorHandling.py
# Description   : 예외 처리 방법
#                 프로그램은 돌아가도록 구현하는 것이 목표이다.                
#                 또한, 문법적으로 에러가 없지만, 코드 실행(런타임) 프로세스에서 발생하는 예외 처리도 존재

'''
Error 종류와 처리 기법은 아래와 같다.

SyntaxError : 잘못된 문법, 고치기 가장 쉬운 에러
print('test)

NameError : 참조변수 없음, 정의되지 않은 에러
a = 10
print(b)

ZeroDivisionEror : div 0
100/0

InderError : 인덱스 범위 오버
x = [10, 20, 30]
print(x[3]), 예외 발생

KeyError : dictionary에 없는 index -> get method로 극복
dic = {'name' : 'kim'}
print(dic['hobby']) -> print(dic.get['hobby'])로 극복

AttributeError : 모듈, 클래스에 없는 잘못된 속성 사용시에 예외
import time
print(time.time())
print(time.month())

ValueError : 참조 값이 없을 때 발생
x = [1, 5, 9]
x.remove[10]

FileNotFoundError : 읽을 파일 없을 때 발생
f = open('test.txt', 'r')

TypeError : tuple, dict와 같은 서로 다른 타입끼리 연산 불가능함, 이때 발생하는 예외
x = [1, 2]
y = (1, 2)
print(x + y)

예외가 발생하지 않는다 가정하고 코딩 후 예외 발생시 예외 처리(EAFP 스타일)

예외 처리 기본
try : 에러가 발생할 가능성이 있는 코드 실행
except : 에러명 정의
else : 에러가 발생하지 않았을 경우 실행
finally : 항상 실행
'''

# 예제1

name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim'  # 'Cho' 예외 발생
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))
except ValueError:
    print('Not found it! - Occurred ValueError!')
else:
    print('ok! else!')

print()

# 예제2

try:
    z = 'Kim'  # 'Cho' 예외 발생
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))
except:  # 모든 에러를 처리(Exception) : 어떤 에러가 나올지 모를때
    print('Not found it! - Occurred ValueError!')
else:
    print('ok! else!')

print()

# 예제3

try:
    z = 'Kim'  # 'Cho' 예외 발생
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))
except Exception as e:
    print(e)  # 에러 내용 출력
    # pass # 임시로 에러 해결 시 예외 처리
else:
    print('ok! else!')
finally:
    print('ok! finally!')  # 무조건 수행 됨

print()

# 예제4
# 예외처리는 하지 않지만, 무조건 수행 되는 코딩 패턴

try:
    print('try')
finally:
    print('finally')

print()

# 예제5
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생, 관리자가 직접 Error형태를 정의

try:
    a = 'Park' # Kim 일때 else도 출력
    if a == 'Kim':
        print('Ok! pass')
    else:
        raise ValueError
except ValueError: # 넘겨받는 형태로 여기서 다시 출력
    print('Raise! Occurred ValueError')
except Exception:
    print('Occurred Exception')
else:
    print('ok! else!')