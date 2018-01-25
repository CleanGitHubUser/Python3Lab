# 총점 getTotal
# 평균 getAverage
# 성적 getGrade

def getTotal():
    # pass    # pass : dummy code
    tot = kor + eng + mat
    return tot

def getAverage():
    # pass
    avg = getTotal() / 3
    return avg

def getGrade():
    avg = getAverage()
    grd = 'F'
    if avg >= 90:
        grd = 'A'
    elif avg >= 80:
        grd = 'B'
    elif avg >= 70:
        grd = 'C'
    elif avg >= 60:
        grd = 'D'
    return grd

print( '-- 성적 처리 프로그램 V2 --')

name = input( '이름을 입력하세요 ' )
kor = int( input( '국어 성적을 입력하세요 ' ) )
eng = int( input( '영어 성적을 입력하세요 ' ) )
mat = int( input( '수학 성적을 입력하세요 ' ) )

fmt = '%s %d %d %d %d %.2f %s'
print( fmt %( name, kor, eng, mat,
    getTotal(), getAverage(), getGrade() ) )

# def getTotal(kor, eng, mat):
#     tot = kor + eng + mat
#     return tot
#
# def getAverage(kor, eng, mat):
#     avg = getTotal(kor, eng, mat) / 3
#     return avg
#
# def getGrade(kor, eng, mat):
#
#     avg = getAverage(kor, eng, mat)
#
#     grd = 'F'
#     if avg >= 90:
#         grd = 'A'
#     elif avg >= 80:
#         grd = 'B'
#     elif avg >= 70:
#         grd = 'C'
#     elif avg >= 60:
#         grd = 'D'
#
#     return grd