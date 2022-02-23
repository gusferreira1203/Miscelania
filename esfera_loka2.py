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

    x,y=[],[]

    for i in range(-0, 100):
        i/=10
        if i != 0:
            x+=[i]
            y+=[i]

    x2,y2,z2=[],[],[]

    for i in range(len(x)):
        if x[i] != 0 and y[i] != 0:
            x2+=[g(x[i])]
            y2+=[g(y[i])]
            z2+=[h(x[i], y[i])]
    sub.scatter(x2, y2, z2, s=1)

def g(n):
    return math.sin(math.pi*(1-2**-n))

def h(n, m):
    return (1-2**-(n**2 + m**2)**.5)*2

f()

plt.show()