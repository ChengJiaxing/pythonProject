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

# class RevealAccess(object):
#     def __init__(self,initval=None,name="var"):
#         self.val=initval
#         self.name=name
#     def __get(self,obj,objtype):
#         print('Retrieving',self.name)
#         return self.val
#     def __set__(self,obj,val):
#         print('Updating',self.name)
#         self.val=val
# class MyClass(object):
#     x=RevealAccess(10,'var "x"')
#     y=5
# m=MyClass()
# m.x=20

# class InitOnAccess:
#     def __init__(self,klass,*args,**kwargs):
#         self.klass=klass
#         self.args=args
#         self.kwargs=kwargs
#         self.__initialized=None
#     def __get__(self,instance,owner):
#         if self.__initialized is None:
#             print('initialized!')
#             self.__initialized=self.klass(*self.args,**self.kwargs)
#         else:
#             print('cached!')
#         return self.__initialized


# def short_repr(cls):
#     cls.__repr__ = lambda self: super(cls, self).__repr__()[:8]
#     return cls
#
#
# @short_repr
# class ClassWithRelativelyLongName:
#     pass
# ClassWithRelativelyLongName()

# from math import hypot
# class Vector:
#     def __init__(self,x=0,y=0):
#         self.x=x
#         self.y=y
#     def __repr__(self):
#         return 'Vector(%r,%r)'%(self.x,self.y)
#     def __abs__(self):
#         return hypot(self.x,self.y)
#     def __bool__(self):
#         return bool(self.x or self.y)
#     def __add__(self, other):
#         x=self.x+other.x
#         y=self.y+other.y
#         return Vector(x,y)
#     def __mul__(self,scalar):
#         return Vector(self.x*self.scalar,self.y*scalar)

# symbols = '$¢£¥€¤'
# codes = []
# for symbol in symbols:
#   codes.append(ord(symbol))
# print(codes)
# codes=[ord(symbol) for symbol in symbols]
# print(codes)
#
# x='ABC'
# dummy=[ord(x) for x in x]
# print(x)
# print(dummy)
symbols = '$¢£¥€¤'
# beyond_ascii=[ord(s) for s in symbols if ord(s)>127]
# beyond_ascii=[ord(s) for s in symbols if ord(s)>164]
# print(beyond_ascii)
# print(beyond_ascii)
# beyond_ascii=list(filter(lambda c: c>127,map(ord,symbols)))
# beyond_ascii=list(filter(lambda c: c>164,map(ord,symbols)))
# print(beyond_ascii)

# colors=['black','white']
# sizes=['S','M','L']
# tshirts=[(color,size) for color in colors for size in sizes]
# print(tshirts)
#
# tshirts=[(size,color) for size in sizes for color in colors]
# print(tshirts)
# subjects=['math','english']
# students=['a','b','c']
# student_subject=[(subject,student) for student in students for subject in subjects]
# print(student_subject)
# print(student_subject[0])




