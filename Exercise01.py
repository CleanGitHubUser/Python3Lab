# 26
import random
A = random.randint(1, 6)
B = random.randint(1, 6)

print( 'A의 주사위 숫자는 %d 입니다.' %A)
print( 'B의 주사위 숫자는 %d 입니다.' %B)
if A > B:
    print( 'A가 이겼다.' )
elif A < B:
    print( 'B가 이겼다.' )
else:
    print( '비겼다.' )

# 31
# 단 = int( input( '몇 단? ' ) )
단 = 9
for i in range( 9, 0, -1 ):
    print( '%d X %d = %d ' %( 단, i, 단 * i ) )

# 32
합 = 0
for i in range( 0, 101 ):
    if ( i % 2 == 0 ):
        합 += i

print( '0 에서 100 까지의 짝수의 합 : ', 합 )

합 = 0
i = 0

while i <= 100:
    if ( i % 2 == 0):
        합 += i
    i += 1

print( '0 에서 100 까지의 짝수의 합 : ', 합 )

# 33
합 = 0
i = 0
while 합 <= 1000:
    i += 1
    if i % 2 == 1:
        합 += i

print( '1 ~ 100의 홀수의 합에서 최초로 1000이 넘는 위치 : ', i )

# 34
숫자 = input( '숫자를 여러개 입력하세요: ' )

for i in range(0, len(숫자) ):
        print( '★' * 2 * int( 숫자[i] ) )

