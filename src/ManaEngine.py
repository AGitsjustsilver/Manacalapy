"""
Manacala
Board = 14 length array
6 & 13 are goal posts
x = 0- 5,  6
y = 7-12, 13

"""
class ManaEngine:

    def __init__(self):
        self.xturn = True
        self.playArr = self.create_area()

    def restart(self):
        self.xturn = True
        self.playArr = self.create_area()

    def create_area(self):
        return [6, 6, 6, 6, 6, 6, 0, 6, 6, 6, 6, 6, 6, 0]

    def play(self, x):
        if self.valid(x):
            pos = (6 if self.xturn else 13) - x
            for moves in range(pos+1,self.playArr[pos]+pos):
                asd = 0 # look into reverse addressing for python

    def valid(self, pos):
        return ((pos < 0) and (pos >= 13)) or (pos == 6)
