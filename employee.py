class person (object):
    def __init__ (self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
class employee(person):
    def __init__(self,name,idnumber,salary):
        self.salary= salary
        person.__init__(self,name,idnumber)
a= employee("hwa",200,1000)
a.display()