# 지금까지의 예제를 함수로 작성
# Qna8, Qna10, Qna11, Qna12
# Qna17, Qna18, Qna19, Qna20

# 이름 짓기
# 파스칼 표기법 :
#   첫단어를 대문자로 시작하며 이름을 지음
#   Employees, Departments
#   RegisterEmployee, JoinMember

# 카멜 표기법 :
#   첫단어를 소문자로 시작하며 이름을 지음
#   registerEmployee, joinMember

# 스네이크 표기법 :
#   소문자와 _ 기호를 이용해서 이름을 지음
#   register_employee, join_member

# 헝가리언 표기법 :
#   자료형을 의미하는 접두사를 이용해서 이름을 지음
#   strName, isMarried, boolMarried

# 함수로 재작성하기

import random

# 8 자취방 구하기
def compareRoom( width, height, price ):
    return width * height / price

roomA = compareRoom( 2.5, 3, 27 )
roomB = compareRoom( 4, 2, 30 )

if (roomA > roomB):
    print( '방A가 낫네요' )
else:
    print('방B가 낫네요')

# 8. 대학생 홍길동씨는 자취방을 구하고 있다. 열심히 발품을 팔며 조사한 끝에 가장 마음에 드는 방 두개를 찾았다.
# 방 A 는 가로 2.5m, 세로 3m 이고, 월세 27만원이다.
# 방 B 는 가로 4m, 세로 2m 이고, 월세 30만원이다.
# 어느 방이 가격 대비 더 넓은지 알아보는 수식을 작성하세요.

# A = [2.5, 3, 27]
# B = [4, 2, 30]
#
# def 가격대비넓이(X):
#     return X[0] * X[1] / X[2]
#
# print( 가격대비넓이(A), 가격대비넓이(B) )

# 10
def computeProfit():
    # c = int( input( '불변자본을 입력하세요. ' ) )
    # v = int( input( '가변자본을 입력하세요. ' ) )
    # s = int( input( '잉여가치액을 입력하세요. ' ) )
    v = 15
    c = 30
    s = 45

    # constant capital, variable capital
    # surplus value

    return s / ( c + v )

print( computeProfit() )

# 10 이윤율 계산 - 도메인 문제
# 지문만으로는 해결할 수 없음
# 문제에 대한 배경 지식이 필요 - 이윤율 공식
# 가변자본 = 15
# 불변자본 = 30
# 잉여가치 = 45

# def 이윤율(가변자본, 불변자본, 잉여가치):
#     return 잉여가치 / ( 불변자본 + 가변자본 )
#
# print( '이윤율 : ', 이윤율(가변자본, 불변자본, 잉여가치) )

# 11
# 달러 환율 : 1071, 2018.01.22 현재
# 유로 환율 : 1309, 2018.01.22 현재

def getExchangeRate(country):
    rate = 0
    if country.upper() == 'US':
        rate = 1071
    if country.upper() == 'EURO':
        rate = 1309
    return rate

buyUS = 780 * getExchangeRate( 'us' )
buyEuro = 650 * getExchangeRate( 'euro' )

if buyUS > buyEuro:
    print( '유로화로 구입하는게 더 싸네요' )
else:
    print( '달러로 구입하는게 더 싸네요' )

# 11 환율에 따른 노트북 구매
# 달러 : 780, 유로 : 650
# 달러 환율 : 1071, 2018.01.22 현재
# 유로 환율 : 1309, 2018.01.22 현재

# def 원달러가치환산(x):
#     return x * 1071
#
# def 원유로가치환산(x):
#     return x * 1309
#
# print( '달러노트북 %d, 유로 노트북 %d' \
#       %( 원달러가치환산(780), 원달러가치환산(650) ) )

# 12
def howManyRun(radius):
    pi = 3.14
    return 2 * radius * pi

studentA = howManyRun(50)
studentB = howManyRun(45)

print( '학생A는 학생B보다 %d만큼 더 뜀' \
       % ( studentA - studentB ) )


# 12 운동장 둘레 계산
# 원의 둘레 계산식 : pi * 지름

# def 원둘레(r):
#     pi = 3.14
#     return 2 * pi * r
#
# print('바깥학생이 %d 미터 더 달렸음' %( 원둘레( 50 ) - 원둘레 ( 45 ) ) )

# 17 계산기 (제곱연산 추가)

def intCal():
    # num1 = int( input( '좌변값을 하나 입력하세요' ) )
    # num2 = int( input( '우변값을 하나 입력하세요' ) )
    num1 = 10
    num2 = 20
    fmt = '%d + %d = %d \n%d - %d = %d \n'
    fmt += '%d * %d = %d \n%d / %d = %.2f \n'
    fmt += '%d ** %d = %d'

    print( fmt % ( num1, num2, num1 + num2, \
                   num1, num2, num1 - num2, \
                   num1, num2, num1 * num2, \
                   num1, num2, num1 / num2, \
                   num1, num2, num1 ** num2 ) )

intCal()
# 17 사칙연산 프로그램 - input 함수 이용
# a = 10
# b = 20
#
# def 사칙연산(a, b):
#     합 = a + b
#     차 = a - b
#     곱 = a * b
#     몫 = a / b
#     print('합 : %d + %d = %d' % (a, b, 합))
#     print('차 : %d - %d = %d' % (a, b, 차))
#     print('곱 : %d * %d = %d' % (a, b, 곱))
#     print('몫 : %d / %d = %.1f' % (a, b, 몫))
#     return 합, 차, 곱, 몫
#
# 사칙연산(a, b)

# 세금계산
def computeTax():
    # salary = int( input( '연봉을 입력하세요.> ' ) )
    salary = 10000
    while True:
        # isMarried = input( '결혼 여부를 입력하세요.(y,n)> ' )
        isMarried = 'y'
        if isMarried.upper() == 'Y' or isMarried.upper() == 'N':
            break
        else:
            print("잘못입력하셨습니다!!")
    tax = 0

    if isMarried == 'Y':
        if salary >= 6000:
            tax = salary * 0.25
        else:
            tax = salary * 0.1
        isMarried = "예"
    else:
        if salary >= 3000:
            tax = salary * 0.25
        else:
            tax = salary * 0.1
        isMarried = "아니오"

    fmt = '연봉 : %d, 결혼여부: %s, 세금 : %.1f'
    print( fmt % ( salary, isMarried, tax ) )

# 18 연봉 계산

# def 연봉계산(연봉, 결혼여부):
#     세금 = 0
#     if 결혼여부 == 'Y':
#         if 연봉 >= 6000:
#             세금 = 연봉 * 0.25
#         else:
#             세금 = 연봉 * 0.1
#     else:
#         if 연봉 >= 3000:
#             세금 = 연봉 * 0.25
#         else:
#             세금 = 연봉 * 0.1
#
#     print('세금 : ', 세금)
#     return 세금
#
# # salary = int( input( '연봉을 입력하세요.> ' ) )
# 연봉 = 10000
# while True:
#     # 결혼여부 = input( '결혼 여부를 입력하세요.(y,n)> ' )
#     결혼여부 = 'y'
#     if 결혼여부.upper() == 'Y' or 결혼여부.upper() == 'N':
#         break
#     else:
#         print("잘못입력하셨습니다!!")
#
# 연봉계산(연봉, 결혼여부)

# 19 윤년여부
def isLeapYear():
    # year = int( input( '윤년여부를 알고 싶은 년도를 입력하세요.> ' ) )
    year = 2018
    isleap = '윤년이 아닙니다.'

    if year % 4 == 0 and year % 100 != 0:
        isleap = '윤년입니다.'
    elif year % 400 == 0:
        isleap = '윤년입니다.'

    print( "%d년은 %s" % ( year, isleap ) )

isLeapYear()


# 19 윤년 계산
# 연도 = int( input( '윤년여부를 알고 싶은 년도를 입력하세요.> ' ) )
# 연도 = 2018
#
# def 윤년계산(연도):
#
#     if 연도 % 4 == 0 and 연도 % 100 != 0:
#         print('%d년은 윤년입니다!' % 연도)
#     elif 연도 % 400 == 0:
#         print('%d년은 윤년입니다!' % 연도)
#     else:
#         print('%d년은 윤년이 아닙니다!' % 연도)
#
# 윤년계산(연도)

# 20 복권발생

def insertLucky():
    wrongtype = '잘못 입력하셨습니다!'
    while True:
        lucky1 = int(input('첫번째 복권번호를 입력하세요!(1 ~ 45)> '))
        if lucky1 > 0 and lucky1 < 46:
            break
        print(wrongtype)

    while True:
        lucky2 = int(input('두번째 복권번호를 입력하세요!(1 ~ 45)> '))
        if lucky2 != lucky1 and lucky2 > 0 and lucky2 < 46:
            break
        print(wrongtype)

    while True:
        lucky3 = int(input('세번째 복권번호를 입력하세요!(1 ~ 45)> '))
        if lucky3 != lucky2 and lucky3 != lucky1 and lucky3 > 0 and lucky3 < 46:
            break
        print(wrongtype)

    lucky = [lucky1, lucky2, lucky3]
    return lucky

def generateLotto():
    import random

    lotto1 = random.randint(1, 45)

    while True:
        lotto2 = random.randint(1, 45)
        if lotto2 != lotto1:
            break

    while True:
        lotto3 = random.randint(1, 45)
        if lotto3 != lotto2 and lotto3 != lotto1:
            break

    lotto = [lotto1, lotto2, lotto3]
    return lotto

def checkMatch(lucky, lotto):
    match = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if lucky[i] == lotto[j]:
                match += 1
    if match == 0:
        print('다음 기회에...')
    elif match == 3:
        print('축하합니다! 상금 백만원!!!')
    elif match == 2:
        print('축하합니다! 상금 만원!!')
    elif match == 1:
        print('축하합니다! 상금 천원!')

    print('복권번호 : ', lucky)
    print('당첨번호 : ', lotto)

def rouletlotto():

    # lucky = insertLucky()
    lucky = [15, 26, 34]

    lotto = generateLotto()

    checkMatch(lucky, lotto)

rouletlotto()