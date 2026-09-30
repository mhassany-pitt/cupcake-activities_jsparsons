class Student():
    def __init__(self, name):
        self.name=name
    def getName(self):
        return self.name
class Score(Student):
    def __init__(self, name, score):
        self.score=score
        Student.__init__(self,name)
    def getScore(self):
        return self.score
