class Employee:
   #ram krishna
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr

    def info(self):
        print('*'*30)
        print('Employee number',self.eno)
        print('Employee name',self.ename)
        print('Employee esal',self.esal)
        print('Employee addr',self.eaddr)
        print('*'*30)
        
e1=Employee(100,'ramakrishna',10000000,'karimnagar')
e2=Employee(200,'vamshi',10000000,'karimnagar')
e1.info()
e2.info()