class SungJukVO:

    def __init__( self, name, kor, eng, mat ):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat
        self.tot = 0
        self.avg = 0.0
        self.grd = 'F'

    def toString(self):
        fmt = '%5s %2d %2d %2d %3d %2.2f %s'
        return format( fmt %( self.name, self.kor, self.eng,
                  self.mat, self.tot, self.avg, self.grd ) )