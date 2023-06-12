# class Person:
#     def __init__(self,name):
#         print('Constructor')
#         self.name=name

#     def show(self):
#         print(self.name)

#     def __del__(self):
#         print('destructor')

# p = Person('Arun')
# p.show()

# # Inheritance
# class Person:
#     def __init__(self,name):
#         self.name=name
    
#     def getName(self):
#         return self.name
    
#     def isEmployee(self):
#         return False
    
# class Employee(Person):
#     def isEmployee(self):
#         return True
    

# p=Person('Rahul')
# print(p.getName(),p.isEmployee())

# e=Employee('Ajith')
# print(e.getName(),e.isEmployee())

# class base:
#     def __init__(self,name):
#         self.name=name
    
#     def getName(self):
#         return self.name
    
# class child(base):
#     def __init__(self, name,age):
#         base.__init__(self,name)
#         self.age=age
    
#     def getAge(self):
#         return self.age
    
# class grandChild(child):
#     def __init__(self,name,age,address):
#         child.__init__(self,name,age)
#         self.address=address
    
#     def getAddress(self):
#         return self.address
    

# gc=grandChild('abc',5,'KA')
# print(gc.getName(),gc.getAge(),gc.getAddress())

class C(object):
    def __init__(self):
        self.c=21
        self.__d=42 #Private

class D(C):
    def __init__(self):
        self.e=10
        C.__init__(self)

d=D()
print(d.e,d.c)