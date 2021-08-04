import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import random
from matplotlib.animation import FuncAnimation
import math

class corpo:
    def __init__(self, x, y, m, vmod, varg, amod, arga):
        self.x = x
        self.y = y
        self.m = m
        self.vmod = vmod
        self.varg = varg
        self.amod = amod
        self.arga = arga

class intro:
    def __init__(self):
        self.fig = plt.figure()
        self.sub = self.fig.add_subplot(1, 1, 1, projection="3d")
        times = int(input("""\nQuantidade de Iterações:\n>>> """))
        l = []
        ll = []
        global corpos
        for corpo in corpos:
            l.append([])
            ll.append([])
        self.corposx = l[::]
        self.corposy = ll[::]
        for t in range(times):
            self.Iterate(t)
        for i in range(len(corpos)):
            lx = []
            ly = []
            for x in self.corposx[i]:
                lx.append(x)
            for y in self.corposy[i]:
                ly.append(y)
            # print(lx,"\n", ly,"\n", list(range(times)))
            self.sub.plot(lx, ly, list(range(times)))
            self.sub.scatter(lx[-1], ly[-1], times - 1, s = corpos[i].m)
    
        plt.show()

    def Iterate(self, t):
        global corpos
        i = 0
        for corpo in corpos:
            corpo.x += corpo.vmod * math.cos(corpo.varg)
            corpo.y += corpo.vmod * math.sin(corpo.varg)
            vx = math.cos(corpo.varg) * corpo.vmod + math.cos(corpo.arga) * corpo.amod
            vy = math.sin(corpo.varg) * corpo.vmod + math.sin(corpo.arga) * corpo.amod
            corpo.vmod = math.sqrt(vx**2 + vy**2)
            if vx == 0:
                if vy != 0:
                    pass
                elif vy > 0:
                    corpo.varg = math.pi/2
                elif vy < 0:
                    corpo.varg = 3*math.pi/2
            else:               
                corpo.varg = math.atan(vy/vx)
            if vx < 0 and not vy == 0:
                corpo.varg += math.pi
            print(corpo.varg, corpo.arga)
            self.corposx[i].append(corpo.x)
            self.corposy[i].append(corpo.y)
            i += 1

a = corpo(x = 0, y = 0, m = 100, vmod = 0, varg = 0, amod = 1, arga = 4*math.pi/6)
b = corpo(x = 0, y = 0, m = 100, vmod = 0, varg = 0, amod = 1, arga = 5*math.pi/6)
c = corpo(x = 0, y = 0, m = 100, vmod = 0, varg = 0, amod = 1, arga = 6*math.pi/6)

d = corpo(x = 0, y = 0, m = 100, vmod = 0, varg = 0, amod = 1, arga = 1*math.pi/6)
e = corpo(x = 0, y = 0, m = 100, vmod = 0, varg = 0, amod = 1, arga = 2*math.pi/6)
f = corpo(x = 0, y = 0, m = 100, vmod = 0, varg = 0, amod = 1, arga = 3*math.pi/6)

a1 = corpo(x = 0, y = 0, m = 100, vmod = 0, varg = 0, amod = 1, arga = 7*math.pi/6)
b1 = corpo(x = 0, y = 0, m = 100, vmod = 0, varg = 0, amod = 1, arga = 8*math.pi/6)
c1 = corpo(x = 0, y = 0, m = 100, vmod = 0, varg = 0, amod = 1, arga = 9*math.pi/6)

d1 = corpo(x = 0, y = 0, m = 100, vmod = 0, varg = 0, amod = 1, arga = 10*math.pi/6)
e1 = corpo(x = 0, y = 0, m = 100, vmod = 0, varg = 0, amod = 1, arga = 11*math.pi/6)
f1 = corpo(x = 0, y = 0, m = 100, vmod = 0, varg = 0, amod = 1, arga = 12*math.pi/6)

corpos = [a, b, c, d, e, f, a1, b1, c1, d1, e1, f1]

INTRO = intro()