# 성적 처리프로그램 V1
# 이름name, 국어kor, 영어eng, 수학mat
# 총점tot, 평균avg, 학점grd

print( '-- 성적 처리 프로그램 v1 --')

name = input( '이름을 입력하세요.> ' )
kor = int( input( '국어 성적을 입력하세요.> ' ) )
eng = int( input( '영어 성적을 입력하세요.> ' ) )
mat = int( input( '수학 성적을 입력하세요.> ' ) )

tot = kor + eng + mat
avg = tot / 3
grd = 'F'
if avg >= 90:
    grd = 'A'
elif avg >= 80:
    grd = 'B'
elif avg >= 70:
    grd = 'C'
elif avg >= 60:
    grd = 'D'

print( name, kor, eng, mat, tot, avg, grd )
print( '{0} {1} {2} {3} {4} {5:.2f} {6}'
    .format( name, kor, eng, mat, tot, avg, grd ) )
print( '이름 : %s, 국어 : %d, 영어 : %d, 수학 : %d,\n'
       '총점 : %d, 평균 : %.2f, 학점 : %s' \
       %( name, kor, eng, mat, tot, avg, grd) )