import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import math


fig = plt.figure()
sub = fig.add_subplot(1, 1, 1, projection="3d")

sub.scatter(0, 0, 1, s=1000, color="#00000011")
sub.scatter(1, 0, 1, color="#000000")
sub.scatter(0, 1, 1, color="#000000")
sub.scatter(-1, 0, 1, color="#000000")
sub.scatter(0, -1, 1, color="#000000")

def f():

    x,y,z=[],[],[]

    for i in range(-100, 100):
        i/=100
        if i != 0:
            x+=[i]
            y+=[i]
            z+=[1]

    x2,y2,z2=[],[],[]

    for i in range(len(x)):
        if x[i] != 0 and y[i] != 0:
            x2+=[math.sin(math.pi*(1-2**-abs(x[i])))*abs(x[i])/x[i]]
            y2+=[math.sin(math.pi*(1-2**-abs(y[i])))*abs(y[i])/y[i]]
            z2+=[(1-2**-abs(((x[i])**2+(y[i])**2)**.5))*2]
            # z2+=[(2**-abs(x[i]))*2]

    sub.scatter(x2, y2, z2, s=1)
    print(x,y)

f()

plt.show()