#Oops 

'''class A:
    def show(self):
        print('Hi')
o=A()
o.show()'''
# encapsulation talks about data packaging and data hiding
# Abstraction talks about showing all posiible features
#Encapsulation

'''class A:
    def add(self):
        print('Hi')
    def sub(self):
        print('Hello')
        self.__mul(3,4)
    def __mul(self,a,b):
        print(a*b)
         
o=A()
o.add()    #when we write o. only the sub and add function is showing because __mul is encapsulated
o.sub()'''

#Inheritance

'''class A:
    def add(self):
        print('Hi')
    def sub(self):
        print('Hello')
        self.__mul(3,4)
    def __mul(self,a,b):
        print(a*b)
class B(A):            # B is child class of A thats why 'sub' func will not work in class A
    def div(self,x,y):  #child class can access the parent class property but parent class can't
        print(int(x/y))
    def sub(self):
        print('Good')
b=A()
b=B()
b.add()
b.sub()
b.div(12,3)'''

#User defined data type Stack

'''class stack:
    def checklist(self):
        self.lis=[]
    def push(self,val):
        self.lis.append(val)
    def pop(self):
        self.lis.pop()
    def display(self):
        print(self.lis)
o=stack()
o.checklist()
o.push(9)
o.push(10)
o.display()
o.pop()
o.display()'''

#Encapsu..

'''class stack:
    def checklist(self):
        self.__lis=[]
    def push(self,val):
        self.__lis.append(val)
    def pop(self):
        self.__lis.pop()
    def display(self):
        print(self.__lis)
o=stack()
o.checklist()
o.push(8)
o.push(10)
o.          '''                        # lis is not showing bcz of encapsu
                                    # we don't need object like 'lis' to show
#  Constructor

'''class stack:                   #Can take argument like
    def __init__(self):         #def __init__(self,a) time of calling the class will call
        self.__lis=[]            #call with argument like o=stack(a)
    def push(self,val,vab):
        self.__lis.append(val)
        self.__lis.append(vab)       
    def pop(self):
        self.__lis.pop()
    def display(self):
        print(self.__lis)
o=stack()
o.push(2,4)
#o.push(14)
#o.display()
o.push(5,6)
#o.display()
o.pop()
o.display()'''

#passing argument in constructor

#Polymorphism( Overloading )

'''class stack:
    def __init__(self):       
        self.__lis=[]         
    def push(self,val,vab):
        self.__lis.append(val)
        self.__lis.append(vab)       
    def pop(self,a):
        self.__lis.pop(a)  #passing  arguments in pop , if it is assign value it is overloading
    def display(self):
        print(self.__lis)
o=stack()
o.push(2,4)
#o.push(14)
#o.display()
o.push(5,6)
#o.display()
o.pop(1)
o.display()'''

#Properties getter and setter

'''class A:
    def __init__(self,a):
        self.__y=a
    @property    
    def x(self):
        return self.__y
    @x.setter
    def x(self,v):
        if v>0:
            self.__y=v
        else:
            print('Invalid')
o=A(5)
print(o.x)
o.x=20
print(o.x)'''

#Name and age

'''class B:
    def __init__(self,a,b):
        self.__x=a
        self.__y=b
    @property  
    def Name(self):
        return self.__x
    @Name.setter
    def Name(self,nam):
        self.__x=nam
    @property
    def Age(self):
        return self.__y
    @Age.setter
    def Age(self,ag):
        self.__y=ag
o=B('chinmay',20)
print(o.Name)
print(o.Age)
o=B('Cocunut',50)
print(o.Name)
print(o.Age)'''

#Age program

'''class B:
    def __init__(self):
        self._age=0
    @property
    def age(self):
        print('Getter method is called')
        return self._age
    @age.setter
    def age(self,a):
        if (a<18):
            raise ValueError('Your age is below eligibility criteria')
        print('Setter method is called')
        self._age=a
exam=B()
exam.age=19
print(exam.age)'''

#Email program

'''class E:
    def __init__(self,first,last):
        self.first=first
        self.last=last
        self.email=first+'.'+last+'@email.com'
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
emp=E('Raj','Kapoor')
print(emp.first)
print(emp.email)
print(emp.fullname()) '''

#Using separate email function

'''class E:
    def __init__(self,first,last):
        self.first=first
        self.last=last
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
emp=E('John','Smith')
emp.first='Jim'
print(emp.first)
print(emp.email())
print(emp.fullname())'''

#Using Property decorator

'''class E:
    def __init__(self,first,last):    #Constructor
        self.first=first
        self.last=last
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    @fullname.setter
    def fullname(self, name):
        first,last=name.split(' ')
        self.first=first
        self.last=last
emp=E('Raj','Kapoor')
emp.fullname='Ranveer Kapoor'
print(emp.first)
print(emp.email)
print(emp.fullname)'''

#Addition and subtraction

'''class A:
    def __init__(self,add,sub):
        self.add=add
        self.sub=sub
    @property
    def Add(self):
        return self.add=res
    @Add.setter
    def Add(self,res):
        res=a+b
    @property
    def Sub(self):
        return self.sub=res
    @Sub.setter
    def Sub(self,res):
        res=a-b
r=A(8,4)
print(r.Add)'''

#Name enter

'''class A:
    def __init__(self,name):
        self.__name=name
    def Name(self):
        return self.__name
    def Name(self,name):
        print(name)'''

# Abstract Class
# There is no Interface in Python


'''from abc import ABC , abstractmethod
class A(ABC):
    def add(self):
        print('Hello')
o=A()'''

#Abstract method

'''from abc import ABC , abstractmethod
class A(ABC):
    @abstractmethod
    def add(self):
        print('Hello')
o=A() '''              #Can't instantiate abstract class A with abstract methods add

#Using Inheritance

'''from abc import ABC , abstractmethod
class A(ABC):
    @abstractmethod
    def add(self):
        print('Hello')
class B(A):
    def sub(self):
        print('Hii')
o=B()'''

#WITHOUT DEFINITION ABSTRACT BASE METHOD

'''from abc import ABC , abstractmethod
class A(ABC):
    @abstractmethod
    def add(self):
        pass         #Not using definition of method
    def sub(self):
        print('Genious')
class B(A):
    def sub(self):
        print('Heloo')
    def add(self):
        print('Hii')
o=B()
o.add()
o.sub()'''

#Polygon program

'''from abc import ABC, abstractmethod
class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass
class Triangle(Polygon):
    def noofsides(self):          #function overiding
        print('I have 3 sides')
class Pentagon(Polygon):
    def noofsides(self):          #function overiding
        print('I have 5 sides')
class Hexagon(Polygon):
    def noofsides(self):
        print('I have 6 sides')
class Quadrilateral(Polygon):
    def noofsides(self):
        print('I have 4 sides')
a=Triangle()
a.noofsides()

b=Pentagon()
b.noofsides()

c=Hexagon()
c.noofsides()

d=Quadrilateral()
d.noofsides()'''

#Moves program

'''from abc import ABC, abstractmethod
class Animals(ABC):
    @abstractmethod
    def moves(self):
        pass
class Human(Animals):
    def moves(self):
        print('I can walk, run, climb')
class Snakes(Animals):
    def moves(self):
        print('I can crawl')
class Fishes(Animals):
    def moves(self):
        print('I can swim')
class Dog(Animals):
    def moves(self):
        print('I can bark')
a=Human()
a.moves()

b=Snakes()
b.moves()

c=Fishes()
c.moves()

d=Dog()
d.moves()'''

#Fabonacci series             f(n)=f(n-1)+f(n-2)   f(0)=0, f(1)=1

def fab(a):
    if a<0:
        print('Incorrect')
    elif a==0:
        return 0
    elif a==1 or a==2:
        return 1
    else:
        return fab(a-1)+fab(a-2)
fab(9)
print(fab(9))











