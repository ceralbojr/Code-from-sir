class studentNum1:
    id_no = 0
    name = ''
    grade1 = 0
    grade2 = 0
    grade3 = 0
    grade4 = 0

    def getAve(self):
        sum = self.grade1 + self.grade2 + self.grade3 + self.grade4
        return sum /4
    def getName(self):
        return self.name