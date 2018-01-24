# 1 print()를 이용 다음 내용이 출력

"*   *   **   ****   ****   *   *"
"*   *  *  *  *   *  *   *  *   *"
"***** *    * ****   ****    * * "
"*   * ****** *   *  *   *    *  "
"*   * *    * *    * *    *   *  "

print("*   *   **   ****   ****   *   *")
print("*   *  *  *  *   *  *   *  *   *")
print("***** *    * ****   ****    * * ")
print("*   * ****** *   *  *   *    *  ")
print("*   * *    * *    * *    *   *  ")

print("  /////  ")
print(" | o o | ")
print("(|  ^  |)")
print(" | [_] | ")
print("  -----  ")

print("            +---+")
print("            |   |")
print("        +---+---+")
print("        |   |   |")
print("    +---+---+---+")
print("    |   |   |   |")
print("+---+---+---+---+")
print("|   |   |   |   |")
print("+---+---+---+---+")

print(" /\\_/\\     -----   ")
print("( ' ' )  / Hello \\ ")
print("(  -  ) <  Junior |")
print(" | | |   \\ Coder!/ ")
print("(__|__)    -----   ")

# 2 이름, 나이, 몸무게
name = '정지웅'
weight = 80
age = 27
print('이름 {0}, 몸무게 {1}, 나이 {2}'
      .format(name, weight, age))

# 3 수학식을 파이썬 표현식으로 작성
x = 2
y = 3
z = 4
print('3x = ', 3 * x)
print('3x + y = ', 3 * x + y)
print('(x + y) / 7 = ', (x + y) / 7)
print('(3x + y) / (z + 2) = ', (3 * x + y) / (z + 2))

# 4 다음 표현식을 완성
x, y = 4, 8
x *= y
print('x *= y : ', x )
x -= y
print('x -= y : ', x )

# 5 다음 수식을 파이썬으로 작성
x = 3  # x = 3
print(x + 7 == 10)  # True

# 6 다음 표현식의 결과는?
print( (-32 + 95) * 12 / 3 ) # 252.0
print(3 * 4 - ((-27 + 67) / 4) ** 8)# 256.0
print( (512 + 1968 - 432) / 2 ** 4 + 128 ) # 256.0
print( 256 == 2 ** 8 ) # True
print( 50 + 50 <= 10 * 10 ) # True
print(99 != 10 ** 2 - 1 ) # False

# 7 다음 변수에 정의된 값을 이용해서 표현식의 실행결과는 무엇인지 서술하세요.
x, y, m, n = 2.5, -1.5, 18, 4
# a
print('x + n * y - ( x + n ) * y = ', x + n * y - (x + n) * y)
# x + n * y - ( x + n ) * y =  6.25

# b
print('m / n + m % n = ', m / n + m % n)
# m / n + m % n =  6.5

# c
print(' 5 * x - n / 5 = ', 5 * x - n / 5)
# 5 * x - n / 5 =  11.7

# d
print(' 1 - ( 1 - ( 1 - ( 1 - ( 1 - n ) ) ) ) = ', 1 - (1 - (1 - (1 - (1 - n)))))
# 1 - ( 1 - ( 1 - ( 1 - ( 1 - n ) ) ) ) =  -3

# 8. 대학생 홍길동씨는 자취방을 구하고 있다. 열심히 발품을 팔며 조사한 끝에 가장 마음에 드는 방 두개를 찾았다.

# 방 A 는 가로 2.5m, 세로 3m 이고, 월세 27만원이다.
# 방 B 는 가로 4m, 세로 2m 이고, 월세 30만원이다.
# 어느 방이 가격 대비 더 넓은지 알아보는 수식을 작성하세요.
Aa, Ab, Ac = 2.5, 3, 27
Ba, Bb, Bc = 4, 2, 30
print(' Aa * Ab / Ac = ', Aa * Ab / Ac)
# Aa * Ab / Ac =  0.2777777777777778
print(' Ba * Bb / Bc = ', Ba * Bb / Bc)
# Ba * Bb / Bc =  0.26666666666666666
# A가 가격 대비 더 넓다.

# 9. 각 표현식에 대한 결과 값을 계산하세요. 틀린 식이 있다면 수정하세요.
# a
print( ' 3 + 4.5 * 2 + 27 / 8 = ',
       3 + 4.5 * 2 + 27 / 8 )
# 3 + 4.5 * 2 + 27 / 8 =  15.375

# b
print( ' True or False and 3 < 4 or not ( 5 == 7 ) = ',
       True or False and 3 < 4 or not ( 5 == 7 ) )
# True or False and 3 < 4 or not ( 5 == 7 ) =  True

# c
print( 'True or ( 3 < 5 and 6 >= 2 ) = ',
       True or ( 3 < 5 and 6 >= 2 ))
# True or ( 3 < 5 and 6 >= 2 ) =  True

# d
# print( " not True > 'A' ", not True > 'A')
# 문자에 비교연산자

# e
# print( " 7 % 4 + 3 - 2 / 6 * 'Z' = ",
#        7 % 4 + 3 - 2 / 6 * 'Z')
# 문자에 산술 연산자

# f
# print( " 'D' + 1 + 'M' % 2 / 3 = ",
#        'D' + 1 + 'M' % 2 / 3 )
# 문자에 산술 연산자

# g
print( ' 5.0 / 3 + 3 / 3 = ',
       5.0 / 3 + 3 / 3)
# 5.0 / 3 + 3 / 3 =  2.666666666666667

# h
print( ' 53 % 21 < 45 / 18 = ',
       53 % 21 < 45 / 18)
# 53 % 21 < 45 / 18 =  False

# i
print( ' ( 4 < 6 ) or True and False or False and ( 2 > 3 ) = ',
       (4 < 6) or True and False or False and (2 > 3))
# ( 4 < 6 ) or True and False or False and ( 2 > 3 ) =  True

# j
print( ' 7 - ( 3 + 8 * 6 + 3 ) - ( 2 + 5 * 2 ) = ',
       7 - (3 + 8 * 6 + 3) - (2 + 5 * 2))
# 7 - ( 3 + 8 * 6 + 3 ) - ( 2 + 5 * 2 ) =  -59

# 10 이윤율 계산 - 도메인 문제
# 지문만으로는 해결할 수 없음
# 문제에 대한 배경 지식이 필요 - 이윤율 공식
가변자본 = 15
불변자본 = 30
잉여가치 = 45
이윤율 = 잉여가치 / ( 불변자본 + 가변자본 )
print( '이윤율 : ', 이윤율 )

# K = 30
# L = 15
# P = 45
# print( P / ( K + L ) )  # 1.0

# 11 환율에 따른 노트북 구매
# 달러 : 780, 유로 : 650
# 달러 환율 : 1071, 2018.01.22 현재
# 유로 환율 : 1309, 2018.01.22 현재
달러노트북 = 780 * 1071
유로노트북 = 650 * 1309
print( '달러노트북 %d, 유로 노트북 %d' \
      %( 달러노트북, 유로노트북 ) )

# dp = 780    # 달러 가격
# ep = 650    # 유로 가격
# epd = 0.818169918   # 0.81...유로/달러
# print( dp * epd )   # 638.1725360400001
# # 달러로 사는게 더 싸다

# 12 운동장 둘레 계산
# 원의 둘레 계산식 : pi * 지름
pi = 3.14
바깥학생거리 = pi * 100
안쪽학생거리 = pi * 90
거리차이 = 바깥학생거리 - 안쪽학생거리
print('바깥학생이 %d 미터 더 달렸음' %거리차이)

# R = 50
# r = R - 5
# pi = 3.14
# print( ' 2 * pi * R - 2 * pi * r = ',
#        2 * pi * R - 2 * pi * r )
# 2 * pi * R - 2 * pi * r =  31.399999999999977
# 약 31.4m 더 달려야한다.

# 13
# a
print( "Check out this line " )
# Check out this line

# b
# print( " //hello there " + '9' + 7 )
# 문자와 숫자 간 산술연산

# c
# print( 'H' + 'I' " is " + 1 + "more example" )

# d
# print( 'H' + 6.5 + 'I' + " is " + 1 + "more example" )

# e
print( "Print both of us" , "Me too" )

# f
print( "Reverse " + 'I' + 'T' )

# g
# print( "Nonot here is" + 1 + "more example" )

# j
# print( "Here is " + 10 * 10 ) )

# k
# print( "Not x is " + True )
# 문자와 블리언

# l
print()

# m
print

# n
# print("how about this one" ++ '?' + 'Huh' )
# 증가연산자

# 14
# a
True and False and True or True
# True
# b
True or True and True and False
# True
# c
( True and False ) or ( True and not False ) \
    or ( False and not False )
# True
# d
( 2 < 3 ) or ( 5 > 2 ) and not ( 4 == 4 ) \
    or 9 != 4
# True
# e
6 == 9 or 5 < 6 and 8 < 4 or 4 > 3
# True

# 15 표현식 결과 알아보기
# a
27 / 13 + 4
# 6.076923076923077
# b
27 / 13 + 4.0
# 6.076923076923077
# c
42.7 % 3 + 18
# 18.700000000000003
# d
( 3 < 4 ) and 5 / 8
# 0.625
# e
23 / 5 + 23 / 5.0
# 9.2
# f
# 2.0 + 'a'
# g
# 2 + 'a'
# h
'a' + 'b'
# 'ab'
# i
# 'a' / 'b'
# j
'a' and not 'b'
# False
# k
# ( double ) 'a' / 'b'
# float() 실수변환 함수

# 16 증감연산자가 파이썬에도 있나?
# 파이썬에서는 기본적으로 ++, --는 지원X
n = 3
++n # +(+n), ++n, n--
print( "n == ", n )
--n # -(-n)
print( "n == ", n )
n += 1
print(n)
n = 3
n -= 1
print(n)

# 17 사칙연산 프로그램 - input 함수 이용
a = 10
b = 20
print( '%d + %d = %d' %( a, b, a + b ) )
print( '%d - %d = %d' %( a, b, a - b ) )
print( '%d * %d = %d' %( a, b, a * b ) )
print( '%d / %d = %.1f' %( a, b, a / b ) )