import numpy as np
b=np.arange(24).reshape(2,12)
print(b)    #print array

print(b.ndim)   #dimension

print(b.size)   #the number of elements

print(b.itemsize)   #The number of bytes each element occupies

print(b.nbytes)     #The number of bytes required for the entire array

print(b.size*b.itemsize)    #The number of each element multiplied by the number of bytes they occupy

b.resize(6,4),print(b) #resize the array

print(b.T)  #the same as resizing the array

c=np.array([1.j+1,2.j+3])   #creat a cmoplex array
print(c)                    #print compolex array
print(c.real)               #print real
print(c.imag)               #print complex
print(c.dtype)              #print data,type
print(c.dtype.str)

b=np.arange(4).reshape(2,2)
print(b)
f=b.flat
print(f)
for item in f :print(item)
print(b.flat[2])
b.flat=7
print(b)
b.flat[[1,3]]=1
print(b)
