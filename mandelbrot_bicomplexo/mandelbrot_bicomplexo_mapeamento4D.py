import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

class Mandelbrot():
    def __init__(self, args = {}, x = [], y = []):
        self.x = x
        self.y = y
        default_vars = {"depth": 5, "real_numbers": 2, "i_numbers": 2, "j_numbers": 2, "k_numbers": 2, "density": 1, "max_mod": 2}
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
        self.Pseudo4D()


    def Pre_Calculation(self):
        self.fig = plt.figure()
        self.sub = self.fig.add_subplot(1, 1, 1, projection="3d")
        self.universe_set_of_real_numbers = range(- self.variables["real_numbers"] * self.variables["density"], self.variables["real_numbers"] * self.variables["density"])
        self.universe_set_of_i_numbers = range(- self.variables["i_numbers"] * self.variables["density"], self.variables["i_numbers"] * self.variables["density"])
        self.universe_set_of_j_numbers = range(- self.variables["j_numbers"] * self.variables["density"], self.variables["j_numbers"] * self.variables["density"])
        self.universe_set_of_k_numbers = range(- self.variables["k_numbers"] * self.variables["density"], self.variables["k_numbers"] * self.variables["density"])
        self.dot_size = 100
        self.x, self.y, self.z = [], [], []
        self.numbers = []

    
    def Go_Through_Universe(self):
        for real_number in self.universe_set_of_real_numbers:     
            percent = round(50 + 100 * real_number / len(self.universe_set_of_real_numbers), 2)
            print(percent, " %")
            real_number /= self.variables["density"]
            for i_number in self.universe_set_of_i_numbers:
                i_number /= self.variables["density"]
                for j_number in self.universe_set_of_j_numbers:
                    j_number /= self.variables["density"]
                    for k_number in self.universe_set_of_k_numbers:
                        k_number /= self.variables["density"]
                        z = [0, 0, 0, 0]
                        for counter in range(self.variables["depth"]):
                            z[0] += (real_number + z[0]*z[0] - z[1]*z[1] + z[2]*z[2] - z[3]*z[3])
                            z[1] += (i_number + z[0]*z[1] + z[3]*z[2] + z[1]*z[0] + z[2]*z[3])
                            z[2] += (j_number + z[0]*z[2] - z[1]*z[3] + z[2]*z[0] - z[3]*z[1])
                            z[3] += (k_number + z[0]*z[3] + z[1]*z[2] + z[2]*z[1] + z[3]*z[0])
                            if (z[0]**2 + z[1]**2 + z[2]**2 + z[3]**2)**0.5 >= self.variables["max_mod"]:
                                self.numbers.append(z)
                                break

    def Pseudo4D(self):
        biggest = 0
        for number in self.numbers:
            if number[3] > biggest:
                biggest = number[3]
        loaded = 0
        for number in self.numbers:
            loaded += 1
            print(str(loaded) + "/" + str(len(self.numbers)))
            digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
            counter, counter1, counter2 = 0, 0, 0
            while counter < 255 * (number[3]//biggest):
                if counter1 == 15:
                    counter1 = 0
                    counter2 += 1
                else:
                    counter1 += 1
                counter += 1
            self.sub.scatter(number[0], number[1], number[2], s = self.dot_size, color = "#" + digit[counter2] + digit[counter1] + "0000")
        print("Building the graph")
        plt.show()

a = Mandelbrot()