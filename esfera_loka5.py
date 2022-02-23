import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import math

fig = plt.figure()
sub = fig.add_subplot(1, 1, 1, projection="3d")
sub.set_box_aspect([1,1,1])

def g(n, m):
    if n != 0:
        arg = math.atan(m/n)
    elif m > 0:
        arg = math.pi/2
    else:
        arg = -math.pi/2
    if n < 0:
        arg += math.pi
    mod = (n**2 + m**2)**.5
    mod2 = math.sin(math.pi*(1-2**-mod))
    n = math.cos(arg) * mod2
    m = math.sin(arg) * mod2
    return n, m, mod

def h(n, m, mod):
    if mod > 1:
        z = (1 - n**2 - m**2)**.5 + 1
    else:
        z = 1 - (1 - n**2 - m**2)**.5
    return z

# sub.plot([-1, 1], [0, 0], [1, 1], color="#ff0000")
# sub.plot([0, 0], [-1, 1], [1, 1], color="#0000ff")
# sub.plot([0, 0], [0, 0], [0, 2], color="#00ff00")

cu_x, cu_y, cu_z = [], [], []

for i in range(0, 6283):
    cu_x+= [math.cos(i/1000)]
    cu_y+= [math.sin(i/1000)]
    cu_z+= [1]

sub.plot(cu_x, cu_y, cu_z, color="#008800")

eixo_sin, eixo_cos, eixo_const1, eixo_const0 = [], [], [], []

for i in range(0, 6283):
    eixo_cos+= [math.cos(i/1000)]
    eixo_sin+= [math.sin(i/1000)+1]
    eixo_const1+= [0]

sub.plot(eixo_const1, eixo_cos, eixo_sin, color="#0000ff")
sub.plot(eixo_cos, eixo_const1, eixo_sin, color="#ff0000")
# sub.plot(cu_x, cu_y, cu_z, color="#00ff00")

x, y, z = [], [], []

for i in range(-100, 100):
    if i == 0:
        continue
    i/=10
    x+=[i]
    y+=[i/i]
    z+=[0]

# sub.scatter(x, y, z)

x2, y2, z2 = [], [], []

for i in range(len(x)):
    a, b, mod = g(x[i], y[i])
    x2+=[a]
    y2+=[b]
    z2+=[h(a, b, mod)]

sub.plot(x2, y2, z2, color="#00000088")
sub.scatter(x2, y2, z2, color="#000000", s=.1)
    
sub.scatter(0, 0, 1, s=32500, color="#aaaaaa22")

plt.show()