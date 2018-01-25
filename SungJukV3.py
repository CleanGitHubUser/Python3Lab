# 성적 처리프로그램 V3
# 리스트 자료구조를 활용한다.

name_list = ['a']
kor_list = [98]
eng_list = [99]
mat_list = [98]

tot_list = [98]
avg_list = [99.99]
grd_list = ['ㅁ']

index = 0
fmt = '%5s %2d %2d %2d %3d %2.2f %s'
format = '''
-- 성적 처리 프로그램 V3 --
1. 성적 입력
2. 전체 성적 확인
3. 상세 성적 확인
4. 성적 수정
5. 성적 삭제
6. 프로그램 종료
어떤 작업을 하시겠습니까> '''

format2 = '''
어떤 데이터를 수정하시겠습니까.
[ 이름( ㅇㄹ / n ), 국어( ㄱㅇ / k ), 영어( ㅇㅇ / e ), 수학( ㅅㅎ / m ) ]
> '''

def getGrade_list():
    avg = avg_list[index]
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


def insertSungJuk():
    count = 0
    while True:

        name_list.append(input('이름을 입력하세요.> '))
        kor_list.append(int(input('국어 성적을 입력하세요.> ')))
        eng_list.append(int(input('영어 성적을 입력하세요.> ')))
        mat_list.append(int(input('수학 성적을 입력하세요.> ')))

        index = len(name_list) - 1      # 인덱스 지정

        tot_list.append(kor_list[index] + eng_list[index] + mat_list[index])
        avg_list.append(tot_list[index] / 3)
        grd_list.append(getGrade_list())
        # grd_list.append( '가' )

        print()
        print( fmt % (name_list[index], kor_list[index], eng_list[index], \
                     mat_list[index], tot_list[index], avg_list[index], grd_list[index]))
        print()

        count += 1

        iscontinue = input('그만 입력하시려면 (n/ㄴ)을 입력하세요.\n계속 입력하시려면 아무 키나 입력하세요.>')
        print()

        if iscontinue.upper() == 'N' or iscontinue == 'ㄴ':

            print( count, '건의 성적을 처리했습니다.')
            break


def viewSungJuk():
    for i in range( 0, len( name_list ) ):

        print(fmt % ( name_list[i], kor_list[i], eng_list[i], \
             mat_list[i], tot_list[i], avg_list[i], grd_list[i] ) )

def dViewSungJuk():
    while True:

        dname = input( '성적을 확인할 학생의 이름을 입력하세요.> ')
        dindex = name_list.index( dname )

        print()
        print(fmt % (name_list[dindex], kor_list[dindex], eng_list[dindex], \
                 mat_list[dindex], tot_list[dindex], avg_list[dindex], grd_list[dindex]))
        print()

        iscontinue = input('확인을 마치시려면 (n/ㄴ)을 입력하세요.\n계속 확인하려면 아무 키나 입력하세요.>')

        if iscontinue.upper() == 'N' or iscontinue == 'ㄴ':

            break


def updateSungJuk():
    while True:
        uname = input( '성적을 수정할 학생의 이름을 입력하세요.> ')

        uindex = name_list.index( uname )

        uwhat = input( format2 )

        print()
        towhat = input( '새로운 데이터를 입력하세요.>')
        print()

        if uwhat == '이름' or uwhat == 'ㅇㄹ' or uwhat == 'n':
            name_list[uindex] = towhat
        elif uwhat == '국어' or uwhat == 'ㄱㅇ' or uwhat == 'k':
            kor_list[uindex] = int( towhat )
        elif uwhat == '영어' or uwhat == 'ㅇㅇ' or uwhat == 'e':
            eng_list[uindex] = int(towhat)
        elif uwhat == '수학' or uwhat == 'ㅅㅎ' or uwhat == 'm':
            mat_list[uindex] = int(towhat)

        print(fmt % (name_list[uindex], kor_list[uindex], eng_list[uindex], \
                     mat_list[uindex], tot_list[uindex], avg_list[uindex], grd_list[uindex]))
        print()

        iscontinue = input('수정을 마치시려면 (n/ㄴ)을 입력하세요.\n계속 수정하려면 아무 키나 입력하세요.>')
        print()

        if iscontinue.upper() == 'N' or iscontinue == 'ㄴ':

            break


while True:

    # print( '-- 성적 처리 프로그램 V3 --')

    command = input( format )
    print()

    if command == '1':
        insertSungJuk()
    elif command == '2':
        viewSungJuk()
    elif command == '3':
        dViewSungJuk()
    elif command == '4':
        updateSungJuk()
    # elif comman == '5':
    #     deleteSungJuk()
    # elif command == '6':
    #     import sys
    #     sys.exit()
    else:
        print( '잘못 입력하셨습니다.')

