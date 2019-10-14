class File:
    def __init__(self,name ):
        self.name=name
        self.file=None
    def open(self):
        self.file=open(self.name,mode="r")
    def read(self):
        return self.file.read()
f1=File("data.txt")
f1.open()
data=f1.read()
print(data)