class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def info(self):
        self.marks=60

s=Student('durga',101)
s.info()
s.age=21
print(s.__dict__)