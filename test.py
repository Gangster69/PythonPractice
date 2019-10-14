class Record:
    def __init__(self ,name,grades):
        self.name=name
        self.grades=grades
student1=Record("Amy",56)
print(student1.name,student1.grades)
student2=Record("Steven",86)
print(student2.name,student2.grades)