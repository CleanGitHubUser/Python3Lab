from SungJukVO import SungJukVO
from SungJukImpl import SungJukService
import sys

# 성적 처리프로그램 V4
# 클래스 이용

# sj = SungJuckVO('a', 99, 98, 99)
class SungJukMain:

    sjs = SungJukService()

    ctnfmt = '계속 하시려면 (n/ㄴ)을 입력하세요.\n계속 하시려면 아무 키나 입력하세요.> '

    cntfmt = '건의 성적을 처리했습니다.'

    wist = '잘못 입력하셨습니다!'

    def selectMenu(self):
        while True:
            str_list = []
            str_list.append(
                '-- 성적 처리 프로그램 V4 --\n'
                '1. 성적 입력\n'
                '2. 전체 성적 확인\n'
                '3. 상세 성적 확인\n'
                '4. 성적 수정\n'
                '5. 성적 삭제\n'
                '6. 프로그램 종료\n'
                '어떤 작업을 하시겠습니까> '
            )
            format = ''.join(str_list)
            command = input( format )

            if command == '1':
                self.case1()
            elif command == '2':
                self.case2()
            elif command == '3':
                self.case3()
            elif command == '4':
                self.case4()
            elif command == '5':
                self.case5()
            elif command == '6':
                sys.exit(1)
            else:
                print( self.wist )

    def case1(self):
        count = 0
        while True:
            name = input('이름을 입력하세요.> ')
            kor = int(input('국어 성적을 입력하세요.> '))
            eng = int(input('영어 성적을 입력하세요.> '))
            mat = int(input('수학 성적을 입력하세요.> '))

            sj = SungJukVO(name, kor, eng, mat)

            self.sjs.insertSungJuk(sj)

            count += 1

            iscontinue = input( self.ctnfmt )
            print()

            if iscontinue.upper() == 'N' or iscontinue == 'ㄴ':
                print(count, self.cntfmt )
                break

    def case2(self):
        self.sjs.viewSungJuk()

    def case3(self):
        while True:

            str_list = []
            str_list.append(
                '성적을 확인할 학생의 이름을 입력하세요.> '
            )
            dname = input( ''.join( str_list ) )

            self.sjs.dViewSungJuk( dname )

            iscontinue = input('확인을 마치시려면 (n/ㄴ)을 입력하세요.\n계속 확인하려면 아무 키나 입력하세요.>')

            if iscontinue.upper() == 'N' or iscontinue == 'ㄴ':

                break

    def case4(self):

        while True:

            uname = input('성적을 수정할 학생의 이름을 입력하세요.> ')

            str_list = []
            str_list.append(
                '어떤 데이터를 수정하시겠습니까.\n'
                '[ 이름( ㅇㄹ / n ), 국어( ㄱㅇ / k ), 영어( ㅇㅇ / e ), 수학( ㅅㅎ / m ) ]\n'
                '> '
            )

            uwhat = input( ''.join( str_list ) )

            if uwhat == '이름' or uwhat == 'ㅇㄹ' or uwhat == 'n':
                uwhat = 'name'
            elif uwhat == '국어' or uwhat == 'ㄱㅇ' or uwhat == 'k':
                uwhat = 'kor'
            elif uwhat == '영어' or uwhat == 'ㅇㅇ' or uwhat == 'e':
                uwhat = 'eng'
            elif uwhat == '수학' or uwhat == 'ㅅㅎ' or uwhat == 'm':
                uwhat = 'mat'
            else:
                print( self.wist )
                continue

            towhat = input('새로운 데이터를 입력하세요.>')

            print( self.sjs.updateSungJuk(uname, uwhat, towhat) )

            iscontinue = input( self.ctnfmt )
            print()

            if iscontinue.upper() == 'N' or iscontinue == 'ㄴ':

                break

    def case5(self):

        while True:

            delname = input('성적을 삭제할 학생의 이름을 입력하세요.> ')

            self.sjs.deleteSungJuk(delname)

            iscontinue = input(self.ctnfmt)
            print()

            if iscontinue.upper() == 'N' or iscontinue == 'ㄴ':
                break