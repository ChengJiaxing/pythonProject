# class Mama:
#     def says(self):
#         print("do your homework")
# class Sister(Mama):
#     def says(self):
#         Mama.says(self)
#         print("and clean your bedroom")
# Sister().says()

# class Mama:
#     def says(self):
#         print("do your homework")
# class Sister(Mama):
#     def says(self):
#         super(Sister,self).says()
#         print("and clean your homework")
# class Sister1(Mama):
#     def says(self):
#         super().says()
#         print("and clean your homework")
# Sister().says()
# Sister1().says()
# antia=Sister1()
# super(antia.__class__,antia).says()

# class People():
#     def says(self):
#         print("I'm a human")
# class Student(People):
#     def says(self):
#         super().says()
#         print("and student")
# class Student1(People):
#     def says(self):
#         super(Student1,self).says()
#         print("and student")
# Student1().says()
# antia=Student1()
# super(antia.__class__,antia).says()
# Student().says()
# super(Student().__class__,Student()).says()
# anita=Student()
# super(anita.__class__,anita).says()


# class Pizza:
#     def __int__(self,toppings):
#         self.toppings=toppings
#     def __repr__(self):
#         return "Pizza with"+"and".join(self.toppings)
#     @classmethod
#     def recommend(cls):
#         return cls(['spm','ham','eggs'])
# class ViKingPizzaZ(Pizza):
#     @classmethod
#     def recommend(cls):
#         recommended=super(ViKingPizzaZ).recommend()
#         recommended.toppings+=['spm']*5
#         return recommended

# class Base1:
#     pass
# class Base2:
#     def method(self):
#         print('Base2')
# class Myclass(Base1,Base2):
#     pass
# Myclass().method()
# class CommonBase:
#     def method(self):
#         print("CommonBase")
# class Base1(CommonBase):
#     pass
# class Base2(CommonBase):
#     def method(self):
#         print("Base2")
# class MyClass(Base1,Base2):
#     pass
# MyClass().method()

# class CommonBase:
#     def method(self):
#         print('commonBase')
# class Base1(CommonBase):
#     pass
# class Base2(CommonBase):
#     def method(self):
#         print('Base2')
# class MyClass(Base1,Base2):
#     pass
# # MyClass().method()
#
# def L(klass):
#     return [k.__name__ for k in  klass.__mro__]
# print(L(MyClass))

# class A:
#     def __int__(self):
#         print("A",end=" ")
#         super().__init__()
# class B:
#     def __init__(self):
#         print("B",end=" ")
#         super().__init__()
# class C(A,B):
#     def __init__(self):
#         print("C",end=" ")
#         A.__init__(self)
#         B.__init__(self)
# print("MRO:",[x.__name__ for x in C.__mro__])


# class CommonBase:
#     def __init__(self,*args,**kwargs):
#         print("CommonBase")
#         super().__init__()
# class Base1(CommonBase):
#     def __init__(self,*args,**kwargs):
#         print("Base1")
#         super().__init__(*args,**kwargs)
# class Base2(CommonBase):
#     def __init__(self,*args,**kwargs):
#         print("Base2")
#         super().__init__(*args,**kwargs)
# class MyClass(Base1,Base2):
#     def __init__(self,arg):
#         print("my base")
#         super().__init__(arg)
# MyClass(10)

class RevealAccess(object):
    def __init__(self,initval=None,name="var"):
        self.val=initval
        self.name=name
    def __get(self,obj,objtype):
        print('Retrieving',self.name)
        return self.val
    def __set__(self,obj,val):
        print('Updating',self.name)
        self.val=val
class MyClass(object):
    x=RevealAccess(10,'var "x"')
    y=5
m=MyClass()
print(m.x)




