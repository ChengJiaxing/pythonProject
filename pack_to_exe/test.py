import copy
import os
yL=[148623.91,32960.49,75508.72,14091.52,75040.31,138570.39,98641.28,114074.27,104637.72,58023.82]
yW=[1519.91,999.35,1232.32,920.62,1573.71,844.99,1184.54,879.02,969.02,1785.45]
yN=[5,10,8,2,3,10,12,9,3,10]
dL=[44351.13,39229.01,54787.74,45284.39,53479.79,897.32,896.09,1096.33,890.53,422.88,970.16,998.29,1024.87,621.91,1243.03]
dW=[422.88,282.88,268.36,277.70,332.29,603.06,714.72,435.84,343.08,641.45,667.21,472.30,340.51,476.60,471.25]
dN=[36,29,42,32,18,38,23,31,40,42,34,25,24,22,28]
yS=[]
dS=[]
for i in range(0,10):
    yS.append([yL[i]*yW[i],yL[i],yW[i],yN[i],i+1])
for i in range(0,5):
    dS.append([dL[i]*dW[i],dL[i],dW[i],dN[i],i+1])
y = sorted(yS, key=(lambda x: [x[0],x[1], x[2],x[3],x[4]]))
d = sorted(dS, key=(lambda x: [x[0],x[1], x[2],x[3],x[4]]))
y.reverse()
d.reverse()
y2=copy.deepcopy(y)
d2=copy.deepcopy(d)
result=1
n=0
x=0
k=y[n][2]
p1=[]
p2=[]
p3=[]
z=0
sy=0
sd=0
for i in range(0,5):
    for j in range(0,d[i][3]):
        z=z+1
        sd=sd+d[i][0]#算成材率
        p1.append(d[i][4])
        if y[n][2]<d[i][2]:
            p1.pop()
            p2.append(p1)
            p1=[d[i][4]]
            if j==0:
                y[n][1]=y[n][1]-d[i-1][1]
            else:
                y[n][1]=y[n][1]-d[i][1]
            if y[n][1]>=d[i][1]:
                y[n][2]=y2[n][2]
                y[n][2]=y[n][2]-d[i][2]
            elif y[n][1]<d[i][1]:
                sy=sy+y[n][0]#算成材率
                p3.append(p2)
                p3.append(y[n][4])
                p2=[]
                y[n][3]=y[n][3]-1
                result=result+1
                if y[n][3]==0:
                    n=n+1
                    y[n][2]=y[n][2]-d[i][2]
                else:
                    y[n][1]=y2[n][1]
                    y[n][2]=y2[n][2]-d[i][2]
        else:
            y[n][2]=y[n][2]-d[i][2]
if i==4 and j==(d[i][3]-1):
    p2.append(p1)
    p3.append(p2)
    p3.append(y[n][4])
c=sd/sy
print(result,p3,c)
os.system('pause')
