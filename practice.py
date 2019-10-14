class Record:
    def __init__(self,name,english,math,sport):
        self.name=name
        self.english=english
        self.math=math
        self.sport=sport

    def show(self):
        print(self.name,self.english,self.math,self.sport)
    def average(self):
       print(self.name,(self.english+self.math+self.sport)/3)
stu=Record("amy",53,86,35)
stu.show()
stu.average()
stu2=Record("steven",85,95,46)
stu2.show()
stu2.average()