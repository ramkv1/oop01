class Student:
    def __init__(self,name,rollno):
        print('constructor exeuction...')
        self.name=name
        self.rollno=rollno
    
    def display(self):
        print('method execution...')
        print('hello my self is:',self.name)
        print('my roll no is:',self.rollno)
s=Student('durga',100)
s1=Student('rk',101)
s.display()
s1.display()
