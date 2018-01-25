from SungJukVO import SungJukVO

class SungJukService:

    sj = SungJukVO( '혜교', 99, 98, 99 )
    sj_list = [ sj ]

    fmt = '%5s %2d %2d %2d %3d %2.2f %s'

    def getTotal(self, sj):
        tot = sj.kor + sj.eng + sj.mat
        return tot


    def getAverage(self, sj):
        avg = self.getTotal( sj ) / 3
        return avg

    def getGrade(self, sj ):
        avg = self.getAverage( sj )
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

    def processSungJuk(self, sj):
        sj.tot = self.getTotal(sj)
        sj.avg = self.getAverage(sj)
        sj.grd = self.getGrade(sj)

    def insertSungJuk(self, sj):

        self.processSungJuk( sj )

        self.sj_list.append( sj )

        print()
        print( sj.toString() )
        print()

    def viewSungJuk(self):
        for i in range( 0, len( self.sj_list ) ):
            sj = self.sj_list[i]
            print( sj.toString() )

    def dViewSungJuk(self, dname ):

            dsj = SungJukVO( '존재하지 않는 이름입니다.', 0, 0, 0 )
            for i in range( 0, len( self.sj_list ) ):
                sj = self.sj_list[i]
                if sj.name == dname:
                    dsj = sj
                    break

            print( dsj.toString() )

    def updateSungJuk(self, uname, uwhat, towhat):

        sj = SungJukVO( '존재하지 않는 이름입니다.', 0, 0, 0 )
        for i in range( 0 , len( self.sj_list ) ):
            if self.sj_list[i].name == uname:
                sj = self.sj_list[i]

                if uwhat == 'name':
                    sj.name = towhat
                elif uwhat == 'kor':
                    sj.kor = int( towhat )
                elif uwhat == 'eng':
                    sj.eng = int( towhat )
                elif uwhat == 'mat':
                    sj.mat = int( towhat )

                self.processSungJuk( sj )

                self.sj_list.append( sj )

                break

        return sj.toString()

    def deleteSungJuk(self, delname):

        result = '존재하지 않는 이름입니다.'
        for i in range( 0 , len( self.sj_list ) ):
            if self.sj_list[i].name == delname:
                sj = self.sj_list[i]
                self.sj_list.remove( sj )
                result = '해당 데이터가 삭제됐습니다!'
                break

        print( result )