import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import random
from matplotlib.animation import FuncAnimation

class Mandelbrot():
    def __init__(self, args = {}, x = [], y = [], j = 0, k = 0):
        print(j,k)
        self.x = x
        self.y = y
        default_vars = {"depth": 100, "real_numbers": 1, "i_numbers": 1, "density": 20, "max_mod": 2}
        self.variables = self.Define_Vars(args, default_vars)
        self.j_number = j
        self.k_number = k
        self.Create_Fractal()


    def Define_Vars(self, args, default_vars):
        for variable in default_vars:
            if variable in args:
                default_vars[variable] = args[variable]
        return default_vars
        

    def Create_Fractal(self):
        self.Pre_Calculation()
        self.Go_Through_Universe()


    def Pre_Calculation(self):
        self.fig = plt.figure()
        self.sub = self.fig.add_subplot(1, 1, 1, projection="3d")
        self.universe_set_of_real_numbers = range(- self.variables["real_numbers"] * self.variables["density"], self.variables["real_numbers"] * self.variables["density"])
        self.universe_set_of_i_numbers = range(- self.variables["i_numbers"] * self.variables["density"], self.variables["i_numbers"] * self.variables["density"])
        self.dot_size = .5
        self.x, self.y = [], []
        self.numbers = []

    
    def Go_Through_Universe(self):
        for real_number in self.universe_set_of_real_numbers:
            real_number /= self.variables["density"]
            for i_number in self.universe_set_of_i_numbers:
                i_number /= self.variables["density"]
                z = [0, 0, 0, 0]
                self.x += [0]
                self.y += [0]
                for counter in range(self.variables["depth"]):
                    z[0] += (real_number + z[0]*z[0] - z[1]*z[1] + z[2]*z[2] - z[3]*z[3])
                    z[1] += (i_number + z[0]*z[1] + z[3]*z[2] + z[1]*z[0] + z[2]*z[3])
                    z[2] += (self.j_number + z[0]*z[2] - z[1]*z[3] + z[2]*z[0] - z[3]*z[1])
                    z[3] += (self.k_number + z[0]*z[3] + z[1]*z[2] + z[2]*z[1] + z[3]*z[0])
                    self.x[-1] = z[0]
                    self.y[-1] = z[1]
                    if (z[0]**2 + z[1]**2 + z[2]**2 + z[3]**2)**0.5 >= self.variables["max_mod"]:
                        self.x.remove(self.x[-1])
                        self.y.remove(self.y[-1])
                        break
                

def InitAnimation():
    global size
    plt.scatter([-size,size,size,-size],[-size,-size,size,size],color="#ffffff")
    return ln


def Update(frame):
    depth = 30
    a = Mandelbrot(j = -1 + 2*(frame % depth)/depth, k = -1 + 2*(frame // depth)/depth)
    ln.set_data(a.x, a.y)
    return ln

fig, ax = plt.subplots()
xdata, ydata = [], []
plt.axis('equal')
ln, = plt.plot([], [], 'ko')
size = 2
ani = FuncAnimation(fig, Update, init_func=InitAnimation, interval=50)

plt.show()