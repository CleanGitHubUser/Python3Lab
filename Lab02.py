# 18 연봉 계산
# salary = int( input( '연봉을 입력하세요.> ' ) )
연봉 = 10000
while True:
    # 결혼여부 = input( '결혼 여부를 입력하세요.(y,n)> ' )
    결혼여부 = 'y'
    if 결혼여부.upper() == 'Y' or 결혼여부.upper() == 'N':
        break
    else:
        print("잘못입력하셨습니다!!")
세금 = 0
if 결혼여부 == 'Y':
    if 연봉 >= 6000:
        세금 = 연봉 * 0.25
    else:
        세금 = 연봉 * 0.1
else:
    if 연봉 >= 3000:
        세금 = 연봉 * 0.25
    else:
        세금 = 연봉 * 0.1
print('세금 : ', 세금)

# 19 윤년 계산
# 연도 = int( input( '윤년여부를 알고 싶은 년도를 입력하세요.> ' ) )
연도 = 2018
if 연도 % 4 == 0 and 연도 % 100 != 0:
    print('%d년은 윤년입니다!' % 연도)
elif 연도 % 400 == 0:
    print('%d년은 윤년입니다!' % 연도)
else:
    print('%d년은 윤년이 아닙니다!' % 연도)

# 20 복권 발생
# 3자리수, 모두일치 100만, 2개일치 1만, 1개일치 1천 지급
import random
lotto = str( random.randint(100, 999) )
# lucky = input( '복권번호를 입력하세요 ')
lucky = '123'
match = 0   # 일치여부

if (lucky[0] == lotto[0] or
    lucky[0] == lotto[1] or
    lucky[0] == lotto[2]):
    match += 1

if (lucky[2] == lotto[0] or
   lucky[2] == lotto[1] or
   lucky[2] == lotto[2]):
    match += 1

print( lotto, lucky, match )

if match == 3:
    print( "1등 당첨 : 백만원!!" )
elif match == 2:
    print( "2등 당첨 : 만원!!" )
elif match == 1:
    print("3등 당첨 : 천원!!")
else:
    print( "다음 기회에" )

# 복권 숫자 입력 받기
# 잘못입력 = '잘못 입력하셨습니다!'
# while True:
#     복권번호1 = int(input('첫번째 복권번호를 입력하세요!(1 ~ 45)> '))
#     if 복권번호1 > 0 and 복권번호1 < 46 :
#         break
#     print(잘못입력)
#
# while True:
#     복권번호2 = int(input('두번째 복권번호를 입력하세요!(1 ~ 45)> '))
#     if 복권번호2 != 복권번호1 and 복권번호2 > 0 and 복권번호2 < 46 :
#         break
#     print(잘못입력)
#
# while True:
#     복권번호3 = int(input( '세번째 복권번호를 입력하세요!(1 ~ 45)> ' ) )
#     if 복권번호3 != 복권번호2 and 복권번호3 != 복권번호1 and 복권번호3 > 0 and 복권번호3 < 46 :
#         break
#     print(잘못입력)
#
# 복권번호 = [복권번호1, 복권번호2, 복권번호3]

복권번호 = [15, 26, 34]

# 당첨번호 생성
import random
당첨번호1 = random.randint(1,45)

while True:
    당첨번호2 = random.randint(1,45)
    if 당첨번호2 != 당첨번호1:
        break

while True:
    당첨번호3 = random.randint(1,45)
    if 당첨번호3 != 당첨번호2 and 당첨번호3 != 당첨번호1:
        break

당첨번호 = [당첨번호1, 당첨번호2, 당첨번호3]

# 일치하는 숫자 갯수 확인
일치갯수 = 0
for i in range( 0, 3 ):
    for j in range( 0, 3 ):
        if 복권번호[i] == 당첨번호[j]:
            일치갯수 += 1
if 일치갯수 == 0:
    print('다음 기회에...')
elif 일치갯수 == 3:
    print( '축하합니다! 상금 백만원!!!' )
elif 일치갯수 == 2:
    print( '축하합니다! 상금 만원!!' )
elif 일치갯수 == 1:
    print( '축하합니다! 상금 천원!' )

print( '복권번호 : ', 복권번호 )
print( '당첨번호 : ', 당첨번호 )

# while True:
#     당첨번호1 = random.randint(1,45)
#
#     while True:
#         당첨번호2 = random.randint(1,45)
#         if 당첨번호2 != 당첨번호1:
#             break
#
#     while True:
#         당첨번호3 = random.randint(1,45)
#         if 당첨번호3 != 당첨번호2 and 당첨번호3 != 당첨번호1:
#             break
#
#     당첨번호 = [당첨번호1, 당첨번호2, 당첨번호3]
#     print( 당첨번호 )
#
#     if 당첨번호1 == 당첨번호2 or 당첨번호2 == 당첨번호3 or 당첨번호3 == 당첨번호1:
#         break

# 21 구구단
# 숫자만 입력받기
# 문자 - ASCII 코드값 : ord()
# ASCII 코드 값 - 문자 : chr()
# 0 : ASCII - 48, 9 : ASCII - 57

# dan = input( '출력할 단을 입력하세요 ' )
dan = '5'
if ( ord( dan[0] ) >= ord( '0' ) and
        ord( dan[0] ) <= ord( '9' ) ):
    print( '구구단 출력' )
else:
    print( '입력 오류 - 숫자만 입력하세요!' )

# 숫자 = int( input( '숫자(1 - 9)를 하나 입력하세요.> ' ) )
숫자 = 5

for i in range( 1, 10 ):
    print( '%d * %d = %d' %( 숫자, i, 숫자 * i ) )

# 22 소문자를 대문자로 변환
# 숫자나 대문자 입력시 오류메시지 출력

while True:
    # lower = input( '소문자를 입력하세요~ ' )
    lower = 's'
    if ord( lower[0] ) < ord( 'a' ) or \
        ord( lower[0] ) > ord( 'z' ):
        print( '소문자만 입력가능!!' )
    else:
        break

print( lower.upper() )

while True:
    # 소문자 = input('소문자를 입력하세요.> ')
    소문자 = 's'

    if ord(소문자) > 96 and ord(소문자) < 123:
        break
    print( '잘못 입력하셨습니다!!' )

print( 소문자.upper() )

# 23 숫자 맞추기
# 1 ~ 100 사이 난수 생성 후 맞추는 게임
key = random.randint(1, 100)

while True:
    # lucky = int( input( '1 ~ 100 사이 숫자 입력하세요 ' ) )
    lucky = key
    if key == lucky:
        print( '빙고!! 숫자를 맞췄습니다!!' )
        break
    elif key < lucky:
        print( '으음... 숫자가 크네요 : (' )
    else:
        print( '으음... 숫자가 작네요 : (' )



숫자2 = random.randint(1, 100)
count = 0
while True:
    # 숫자1 = int(input('1 ~ 100사이의 숫자를 입력하세요.> '))
    숫자1 = 숫자2
    count += 1

    if 숫자1 > 숫자2:
        print( '추측한 숫자가 큽니다' )
    elif 숫자1 < 숫자2:
        print( '추측한 숫자가 작습니다' )
    else:
        print( '빙고 숫자를 맞췄습니다.\n시도 횟수: %d회' %count )
        break

# 24

결과 = \
'''          Multiplication Table
         1   2   3   4   5   6   7   8   9
------------------------------------------
'''
# 1   |   %d  %d  %d  %d  %d  %d  %d  %d  %d
# 2   |   %d  %d  %d  %d  %d  %d  %d  %d  %d
# 3   |   %d  %d  %d  %d  %d  %d  %d  %d  %d
# 4   |   %d  %d  %d  %d  %d  %d  %d  %d  %d
# 5   |   %d  %d  %d  %d  %d  %d  %d  %d  %d
# 6   |   %d  %d  %d  %d  %d  %d  %d  %d  %d
# 7   |   %d  %d  %d  %d  %d  %d  %d  %d  %d
# 8   |   %d  %d  %d  %d  %d  %d  %d  %d  %d
# 9   |   %d  %d  %d  %d  %d  %d  %d  %d  %d
# '''

for i in range(1, 10):
    결과 = 결과 + str(i) + '''   |   '''
    for j in range(1, 10):
        임시 = format('%2d  ' %( i * j ) )
        결과 = 결과 + 임시
    결과 = 결과 + '\n'

print(결과)

# 25
# 숫자 = input('6자리 숫자 k     01를 입력하세요' )
숫자 = '356317'
if 숫자[0] == '3' and 숫자[1] == '5':
    print( 'JCB카드' )
    if 숫자 == '356317':
        print( 'NH농협카드' )
    elif 숫자 == '356901':
        print( '신한카드' )
    elif 숫자 == '356912':
        print( 'KB국민카드' )
elif 숫자[0] == '4':
    print( '비자카드' )
    if 숫자 == '404825':
        print( '비씨카드' )
    elif 숫자 == '438676':
        print( '신한카드' )
    elif 숫자 == '457973':
        print( '국민은행' )
elif 숫자[0] == 5:
    print( '마스터카드, Maestro' )
    if 숫자 == '515594':
        print( '신한카드' )
    elif 숫자 == '524353':
        print( '외환카드' )
    elif 숫자 == '540926':
        print( '국민은행' )

# 26
# 주민번호 = input( '주민번호를 입력하세요.> ')
주민번호 = '9202271251222'
테스트 = 0

for i in range(0, 12):
    임시 = int( 주민번호[i] ) * ( i % 8 + 2 )
    테스트 += 임시

if 11 - 테스트 % 11 == int( 주민번호[12] ):
    print( '정상 주민번호입니다.' )
elif 11 - 테스트 % 11 - 10 == int( 주민번호[12] ):
    print( '정상 주민번호입니다.' )
else: print( '비정상 주민번호입니다.' )

# 30
합 = 0
i = 100
while i < 10000:
    if i % 5 == 0:
        합 += i
    i += 1

print( 합 )

# 34
# 화씨 = int( input( '화씨를 입력하세요.> ' ) )
화씨 = 50
섭씨 = ( 100 / 180 ) * ( 화씨 - 32 )
print( '%dF = %dC' %(화씨, 섭씨) )

# 35
# 잔돈 = int( input( '잔돈을 입력하세요.> ' ) )
잔돈 = 99999
화폐 = [10, 50, 100, 500, 1000, 5000, 10000, 50000]
갯수 = [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(7, -1, -1):
    갯수[i] = 잔돈 // 화폐[i]
    잔돈 = 잔돈 % 화폐[i]
    print( '%d 원 : %d 개' %( 화폐[i], 갯수[i] ) )

# 36
print( '%d초는 %d일' %( 1234567890, 1234567890 // 86400 ) )
print( '%d초는 %d시간' %( 12345, 12345 // 3600 ) )
print( '%d초는 %d분' %( 67890, 67890 // 60 ) )

# 40
# 상품구매갯수 = int( input( '상품 구매 갯수를 입력하세요.> ' ) )
상품구매갯수 = 50
상품가격 = 1000

if 상품구매갯수 < 10:
   지불가격 = 상품구매갯수 * ( 상품가격 - 100 )
elif 상품구매갯수 < 30:
    지불가격 = 상품구매갯수 * ( 상품가격 - 100 )
elif 상품구매갯수 <100:
    지불가격 = 상품구매갯수 * ( 상품가격 - 100 )
else:
    지불가격 = 상품구매갯수 * ( 상품가격 - 100 )

print( '지불해야 할 가격 : ', 지불가격 )

# 41
# 키 = int( input( '키를 입력하세요.> ' ) ) / 100
키 = 174 / 100
# 몸무게 = int( input( '몸무게를 입력하세요.> ' ) )
몸무게 = 80

체질량지수 = 몸무게 / ( 키 * 키 )

if 체질량지수 < 18.5:
    print( '저체중입니다.' )
elif 체질량지수 < 23:
    print( '정상입니다.' )
elif 체질량지수 < 25:
    print( '과체중입니다.' )
else:
    print( '비만입니다.' )

