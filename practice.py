class Employee:
    def __init__(self,emplid=None,name=None,salary=None):
        self.emplid=emplid
        self.name=name
        self.salary=salary
    def setEmpid(self,emplid):
        self.emplid=emplid
    def setName(self,name):
        self.name=name
    def setSalary(self,salary):
        self.salary=salary
    def getEmpid(self):
        return self.emplid
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary
e1=Employee()
e2=Employee(1,"Rahul",4000)
e1.setEmpid(2)
e1.setName("Romesh")
e1.setSalary(500000)
print(e1.getEmpid(),e1.getName(),e1.getSalary())
print(e2.getEmpid(),e2.getName(),e2.getSalary())