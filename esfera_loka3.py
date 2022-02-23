import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import math


fig = plt.figure()
sub = fig.add_subplot(1, 1, 1, projection="3d")

sub.scatter(0, 0, 1, s=1000, color="#00000099")
sub.scatter(1, 0, 1, color="#ff888888")
sub.scatter(0, 1, 1, color="#8888ff88")
sub.scatter(-1, 0, 1, color="#ff888888")
sub.scatter(0, -1, 1, color="#8888ff88")
sub.scatter(0, 0, 0, color="#88ff8888")
sub.scatter(0, 0, 2, color="#88ff8888")

def f():

    x,y=[],[]

    for i in range(-0, 100):
        i/=10
        if i != 0:
            x+=[i]
            y+=[i**2]
            x+=[i]
            y+=[i**3]
            x+=[i]
            y+=[i*2]
            x+=[i]
            y+=[i/2]

    x2,y2,z2=[],[],[]

    for i in range(len(x)):
        a,b=g(x[i], y[i])
        x2+=[a]
        y2+=[b]
        z2+=[h(x[i], y[i])]

    sub.scatter(x2, y2, z2, s=1)

def g(n, m):
    mod = (n**2 + m**2)**.5
    if n != 0:
        arg = math.atan(m/n)
    elif m > 0:
        arg = math.pi
    else:
        arg = 3*math.pi/2
    if arg > math.pi/2:
        arg -= math.pi
    mod2 = math.sin(math.pi*(1-2**-mod))
    a = math.cos(arg) * mod2
    b = math.sin(arg) * mod2
    return a, b

def h(n, m):
    return (1-2**-(n**2 + m**2)**.5)*2

f()

plt.show()