import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import random
from matplotlib.animation import FuncAnimation
import math

class corpo:
    def __init__(self, x, y, r, m, vmod, varg, amod, arga, cor = "#00ff00"):
        self.x = x
        self.y = y
        self.r = r
        self.m = m
        self.vmod = vmod
        self.varg = varg
        self.amod = amod
        self.arga = arga
        self.cor = cor

        # KMH = False

        # if KMH:
        #     self.x *= 1000
        #     self.y *= 1000
        #     self.r *= 1000
        #     self.vmod *= 3.6
        #     self.amod *= 12960

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
            self.sub.plot(lx, ly, list(range(times)), color = corpos[i].cor, linewidth = corpos[i].r/10)
            self.sub.scatter(lx[-1], ly[-1], times - 1, s = corpos[i].r/1, color = corpos[i].cor)
    
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
            corpo.varg = self.arcotangente(vx, vy)
            self.corposx[i].append(corpo.x)
            self.corposy[i].append(corpo.y)
            i += 1
        self.gravidade()

    def arcotangente(self, x, y):
        atan = 0
        if x == 0:
            if y != 0:
                pass
            elif y > 0:
                atan = math.pi/2
            elif y < 0:
                atan = 3*math.pi/2
        else:               
            atan = math.atan(y/x)
        if x < 0 and not y == 0:
            atan += math.pi
        return atan

    def gravidade(self):
        for i in range(len(corpos)):
            corpo = corpos[i]
            outros_corpos = corpos[:i] + corpos[i + 1:]
            mod_aceleracoes = []
            arg_aceleracoes = []
            for j in outros_corpos:
                arg_aceleracoes.append(self.arcotangente(corpo.x - j.x, corpo.y - j.y))
                if ((corpo.y - j.y)**2 + (corpo.x - j.x)**2)**.5 > corpo.r + j.r:
                    mod_aceleracoes.append(6.67408 * 10 ** -11 * j.m / ((j.y - corpo.y)**2 + (j.x - corpo.x)**2))
                else:
                    corpo.varg += j.varg - corpo.varg
                    mod_aceleracoes.append(6.67408 * 10 ** -11 * j.m / ((corpo.r + j.r)**2))
            ax = 0
            ay = 0
            for j in range(len(mod_aceleracoes)):
                ax += mod_aceleracoes[j] * -math.cos(arg_aceleracoes[j])
                ay += mod_aceleracoes[j] * -math.sin(arg_aceleracoes[j])
            corpo.amod = math.sqrt(ax**2 + ay**2)
            corpo.arga = self.arcotangente(ax, ay)
            


Terra = corpo(x = 0, y = 0, r = 1737400, m = 73600000000000000000000, vmod = 0, varg = 0, amod = 0, arga = 0, cor = "#0000ff")
Lua = corpo(x = 384400000, y = 0, r = 6371000, m = 5972200000000000000000000, vmod = 0, varg = 0, amod = 0, arga = 0, cor = "#554433")
Sol = corpo(x = 149600000000, y = 0, r = 696340000, m = 1989000000000000000000000000000, vmod = 0, varg = 0, amod = 0, arga = 0,  cor = "#ffff00")

Gustavo = corpo(x = 0, y = 0, r = 1, m = 80, vmod = 0, varg = 0, amod = 0, arga = 0)
Fischer = corpo(x = 0, y = 10, r = 1, m = 48.9, vmod = 0, varg = 0, amod = 0, arga = 0)

# a = corpo(x = 0, y = 100, r = 50, m = 500000000000, vmod = 0, varg = 0, amod = 0, arga = 0, cor = "#0000ff")
# b = corpo(x = 0, y = 0, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ff4400")
# b2 = corpo(x = 0, y = 0, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ff8800")
# b3 = corpo(x = 1, y = 0, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ffbb00")
# b4 = corpo(x = 2, y = 0, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ffff00")
# b5 = corpo(x = 3, y = 0, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#bbff00")
# b = corpo(x = 4, y = 0, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ff4400")
# b21 = corpo(x = 5, y = 0, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ff8800")
# b31 = corpo(x = 6, y = 0, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ffbb00")
# b41 = corpo(x = 7, y = 0, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ffff00")
# b51 = corpo(x = 8, y = 0, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#bbff00")
# ab = corpo(x = 9, y = 0, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ff4400")
# ab2 = corpo(x = 10, y = 0, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ff8800")
# ab3 = corpo(x = 11, y = 0, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ffbb00")
# ab4 = corpo(x = 12, y = 0, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ffff00")
# ab5 = corpo(x = 13, y = 0, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#bbff00")
# bb = corpo(x = 14, y = 0, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ff4400")
# bb2 = corpo(x = 15, y = 0, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ff8800")
# bb3 = corpo(x = 16, y = 0, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ffbb00")
# bb4 = corpo(x = 17, y = 0, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ffff00")
# bb5 = corpo(x = 18, y = 0, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#bbff00")

# a = corpo(x = 0, y = 100, r = 50, m = 500000000000, vmod = 0, varg = 0, amod = 0, arga = 0, cor = "#0000ff")
# b = corpo(x = 0, y = 18, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ff4400")
# b2 = corpo(x = 0, y = 17, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ff8800")
# b3 = corpo(x = 1, y = 16, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ffbb00")
# b4 = corpo(x = 2, y = 15, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ffff00")
# b5 = corpo(x = 3, y = 14, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#bbff00")
# b = corpo(x = 4, y = 13, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ff4400")
# b21 = corpo(x = 5, y = 12, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ff8800")
# b31 = corpo(x = 6, y = 11, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ffbb00")
# b41 = corpo(x = 7, y = 10, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ffff00")
# b51 = corpo(x = 8, y = 9, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#bbff00")
# ab = corpo(x = 9, y = 8, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ff4400")
# ab2 = corpo(x = 10, y = 7, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ff8800")
# ab3 = corpo(x = 11, y = 6, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ffbb00")
# ab4 = corpo(x = 12, y = 5, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ffff00")
# ab5 = corpo(x = 13, y = 4, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#bbff00")
# bb = corpo(x = 14, y = 3, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ff4400")
# bb2 = corpo(x = 15, y = 2, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ff8800")
# bb3 = corpo(x = 16, y = 1, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ffbb00")
# bb4 = corpo(x = 17, y = 0, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ffff00")
# bb5 = corpo(x = 18, y = -1, r = 5, m = .01, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#bbff00")


a = corpo(x = 0, y = 100, r = 50, m = 500000000000, vmod = 0, varg = 0, amod = 0, arga = 0, cor = "#0000ff")
b = corpo(x = 0, y = 18, r = 5, m = 1, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ff4400")
c = corpo(x = 0, y = 17, r = 5, m = 1, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ff8800")
d = corpo(x = 1, y = 16, r = 5, m = 1, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ffbb00")
e = corpo(x = 2, y = 15, r = 5, m = 1, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ffff00")
f = corpo(x = 3, y = 14, r = 5, m = 1, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#bbff00")
g = corpo(x = 4, y = 13, r = 5, m = 1, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ff4400")
h = corpo(x = 5, y = 12, r = 5, m = 1, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ff8800")
i = corpo(x = 6, y = 11, r = 5, m = 1, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ffbb00")
j = corpo(x = 7, y = 10, r = 5, m = 1, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ffff00")
k = corpo(x = 8, y = 9, r = 5, m = 1, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#bbff00")
l = corpo(x = 9, y = 8, r = 5, m = 1, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ff4400")
m = corpo(x = 10, y = 7, r = 5, m = 1, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ff8800")
n = corpo(x = 11, y = 6, r = 5, m = 1, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ffbb00")
o = corpo(x = 12, y = 5, r = 5, m = 1, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ffff00")
p = corpo(x = 13, y = 4, r = 5, m = 1, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#bbff00")
q = corpo(x = 14, y = 3, r = 5, m = 1, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ff4400")
r = corpo(x = 15, y = 2, r = 5, m = 1, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ff8800")
s = corpo(x = 16, y = 1, r = 5, m = 1, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ffbb00")
t = corpo(x = 17, y = 0, r = 5, m = 1, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#ffff00")
u = corpo(x = 18, y = -1, r = 5, m = 1, vmod = .1, varg = 3, amod = 0, arga = 0, cor = "#bbff00")

# c = corpo(x = 100, y = 0, r = 50, m = 500000000000, vmod = 0, varg = 0, amod = 0, arga = 0, cor = "#00ff00")

corpos = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u]

INTRO = intro()