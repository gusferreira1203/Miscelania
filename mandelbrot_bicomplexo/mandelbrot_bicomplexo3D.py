import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import random

class Mandelbrot():
    def __init__(self, args = {}, x = [], y = []):
        self.x = x
        self.y = y
        default_vars = {"depth": 1000, "real_numbers": 2, "i_numbers": 2, "j_numbers": 2, "k_numbers": 2, "density": 100, "max_mod": 1}
        self.variables = self.Define_Vars(args, default_vars)
        self.Create_Fractal()


    def Define_Vars(self, args, default_vars):
        for variable in default_vars:
            if variable in args:
                default_vars[variable] = args[variable]
        return default_vars
        

    def Create_Fractal(self):
        self.Pre_Calculation()
        self.Go_Through_Universe()
        plt.show()


    def Pre_Calculation(self):
        self.fig = plt.figure()
        self.sub = self.fig.add_subplot(1, 1, 1, projection="3d")
        self.dot_size = 1
        self.x, self.y, self.z = [], [], []
        self.numbers = []

    
    def Go_Through_Universe(self):
        for i in range(500):
            real_number = -.5 + random.random()
            i_number = -.5 + random.random()
            j_number = -.5 + random.random()
            k_number = -.5 + random.random()
            z = [0, 0, 0, 0]
            z0,z1,z2,z3=[],[],[],[]
            for counter in range(self.variables["depth"]):
                z[0] += (real_number + z[0]*z[0] - z[1]*z[1] + z[2]*z[2] - z[3]*z[3])
                z[1] += (i_number + z[0]*z[1] + z[3]*z[2] + z[1]*z[0] + z[2]*z[3])
                z[2] += (j_number + z[0]*z[2] - z[1]*z[3] + z[2]*z[0] - z[3]*z[1])
                z[3] += (k_number + z[0]*z[3] + z[1]*z[2] + z[2]*z[1] + z[3]*z[0])
                if (z[0]**2 + z[1]**2 + z[2]**2 + z[3]**2)**0.5 >= self.variables["max_mod"]:
                    break
                z0.append(z[0])
                z1.append(z[1])
                z2.append(z[2])
                z3.append(z[3])
            self.sub.plot(z0,z1,z2,linewidth=.1,color="#"+["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"][random.randint(0,15)]+["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"][random.randint(0,15)]+["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"][random.randint(0,15)]+["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"][random.randint(0,15)]+["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"][random.randint(0,15)]+["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"][random.randint(0,15)])
            
a = Mandelbrot()