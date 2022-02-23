import matplotlib.pyplot as plt 
import math

plt.plot([-1, 1], [0, 0])
plt.plot([0, 0], [-1, 1])

x,y=[],[]

for i in range(-2000, 2000):
    i/=2
    if i == 0:
        x+=[i]
        y+=[1/i]

# plt.plot(x, y)

x2,y2=[],[]

for i in range(len(x)):
    if x[i] != 0 and y[i] != 0:
        x2+=[(1-2**-abs(x[i]))*(abs(x[i])/x[i])]
        y2+=[(1-2**-abs(y[i]))*(abs(y[i])/y[i])]


plt.plot(x2, y2)

plt.show()
