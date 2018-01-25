import random

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

# 20 복권발행
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

# 성적 데이터 클래스
class SungJukVO:
    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat

    def getTot(self):
        return tot

    def getAvg(self):
        return avg

    def getGrd(self):
        return grd

    def getName(self):
        return name

    def getKor(self):
        return kor

    def getEng(self):
        return eng

    def getMat(self):
        return mat

    def setTot(self, tot):
        self.tot = tot

    def setAvg(self, avg):
        self.avg = avg

    def setGrd(self, grd):
        self.grd = grd

    def setName(self, name):
        self.name = name

    def setKor(self, kor):
        self.kor = kor

    def setEng(self, eng):
        self.eng = eng

    def setMat(self, mat):
        self.mat = mat

    def toSting(self):
        fmt = '%5s %2d %2d %2d %3d %2.2f %s'
        return format(fmt % (name, kor, eng, mat, tot, avg, grd))

# 성적 처리용 클래스
class SungJukService:

    def getTotal(self, sj):
        tot = sj.kor + sj.eng + sj.mat
        return tot

    def getAverage(self, sj):
        avg = self.getTotal(sj) / 3
        return avg

    def getGrade(self, sj):
        avg = self.getAverage(sj)
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

            index = len(name_list) - 1  # 인덱스 지정

            tot_list.append(kor_list[index] + eng_list[index] + mat_list[index])
            avg_list.append(tot_list[index] / 3)
            grd_list.append(getGrade_list())
            # grd_list.append( '가' )

            print()
            print(fmt % (name_list[index], kor_list[index], eng_list[index], \
                         mat_list[index], tot_list[index], avg_list[index], grd_list[index]))
            print()

            count += 1

            iscontinue = input('그만 입력하시려면 (n/ㄴ)을 입력하세요.\n계속 입력하시려면 아무 키나 입력하세요.>')
            print()

            if iscontinue.upper() == 'N' or iscontinue == 'ㄴ':
                print(count, '건의 성적을 처리했습니다.')
                break

    def viewSungJuk():
        for i in range(0, len(name_list)):
            print(fmt % (name_list[i], kor_list[i], eng_list[i], \
                         mat_list[i], tot_list[i], avg_list[i], grd_list[i]))

    def dViewSungJuk():
        while True:

            dname = input('성적을 확인할 학생의 이름을 입력하세요.> ')
            dindex = name_list.index(dname)

            print()
            print(fmt % (name_list[dindex], kor_list[dindex], eng_list[dindex], \
                         mat_list[dindex], tot_list[dindex], avg_list[dindex], grd_list[dindex]))
            print()

            iscontinue = input('확인을 마치시려면 (n/ㄴ)을 입력하세요.\n계속 확인하려면 아무 키나 입력하세요.>')

            if iscontinue.upper() == 'N' or iscontinue == 'ㄴ':
                break

    def updateSungJuk():

        format = '어떤 데이터를 수정하시겠습니까.\n\
            [ 이름( ㅇㄹ / n ), 국어( ㄱㅇ / k ), 영어( ㅇㅇ / e ), 수학( ㅅㅎ / m ) ]\n\
            > '

        while True:
            uname = input('성적을 수정할 학생의 이름을 입력하세요.> ')

            uindex = name_list.index(uname)

            uwhat = input(format2)

            print()
            towhat = input('새로운 데이터를 입력하세요.>')
            print()

            if uwhat == '이름' or uwhat == 'ㅇㄹ' or uwhat == 'n':
                name_list[uindex] = towhat
            elif uwhat == '국어' or uwhat == 'ㄱㅇ' or uwhat == 'k':
                kor_list[uindex] = int(towhat)
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