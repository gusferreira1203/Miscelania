import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import random
from matplotlib.animation import FuncAnimation

class GAME_OF_LIFE():
    
    def __init__(self):
        self.x = []
        self.y = []
        self.maximum_x = 0
        self.maximum_y = 0
        self.default_variables = {"graph_style": "simple_scatter", "color": "#000000", "plot_axises":False}
        self.variables = self.default_variables
        self.Welcome()
        plt.show()

    def SetVariable(self):#fazer o negócio das variaveis
        pass

    def ColorPicker(self):#padrões de cor
        pass

    def Welcome(self):
        print(
            """
        Jogo da Vida de John Conway (1937 - 2020)\n
            """
        )

        mode = input("""
        Escolha um modo:\n\n
        A - Animação\n
        B - Eixo Z para tempo\n\n
        >>> """)

        structure = input("""
        A - Aleatório\n
        E - Estruturas\n\n
        >>> """)

        if structure.upper() == "A":
            self.starting_area = int(input("""
            Tamanho inicial:\n
            >>> """))
            self.density = int(input("""\n
            Densidade de pontos(em porcentagem):\n
            >>> """))
            self.RandomMap()

        finish = False

        while not finish:
            instruction = input("Digite\n'A' para acrescentar um Glider\n'B' para acrescentar um blinker 3x1\n'X' para gerar o gráfico\n>>> ").upper()
            finish = instruction == "X"
            if instruction == 'A':
                self.GenerateGlider(int(input("Menor Abicissa da estrutura: ")), int(input("Menor Ordenada da estrutura: ")), int(input("Sentido do quadrante: ")))
            if instruction == 'B':
                self.GenerateBlinker3x1(int(input("Menor Abicissa da estrutura: ")), int(input("Menor Ordenada da estrutura: ")), input("'V' para vertical e 'H' para horizontal: ").upper())               
            if instruction == 'C':
                self.GenerateBlinker(int(input("Menor Abicissa da estrutura: ")), int(input("Menor Ordenada da estrutura: ")))

        if mode.upper() == "A":
            self.fig, self.ax = plt.subplots()
            self.xdata, self.ydata = [], []
            plt.axis('equal')
            self.ln, = plt.plot([], [], 'ko')
            self.ani = FuncAnimation(self.fig, self.Update, init_func=self.InitAnimation, interval=100)

        if mode.upper() == "B":
            self.fig = plt.figure()
            self.sub = self.fig.add_subplot(1, 1, 1, projection="3d")
            self.amount_of_iterations = int(input("""
            Quantidade de Iterações:\n
            >>> """))
            self.MainLoop()


    def RandomMap(self):
        for point in range(int(self.starting_area ** 2 * self.density / 100)):
            self.x.append(random.randint(0,self.starting_area))
            self.y.append(random.randint(0,self.starting_area))

    def InitAnimation(self):
        plt.scatter([-55,55,55,-55],[-55,-55,55,55],color="#ffffff")
        return self.ln


    def Update(self, frame):
        self.Iterate()
        self.ln.set_data(self.x, self.y)
        return self.ln


    def MainLoop(self):
        for iteration in range(self.amount_of_iterations):
            z_axis = []
            print(str(iteration + 1) + " de " + str(self.amount_of_iterations))
            self.list_length = len(self.x)
            for counter in range(self.list_length):
                z_axis.append(iteration)
            if self.variables["graph_style"] == "simple_scatter":
                self.sub.scatter(self.x, self.y, z_axis, s = .1) #, color = self.variables["color"])
            else:
                for index in range(self.list_length):
                    x1 = self.x[index] - .5
                    x2 = self.x[index] + .5
                    y1 = self.y[index] - .5
                    y2 = self.y[index] + .5
                    z1 = iteration
                    if self.variables["graph_style"] == "flat_squares":
                        self.sub.plot(
                            [x1,x2,x2,x1,x1],
                            [y1,y1,y2,y2,y1],
                            [z1,z1,z1,z1,z1],
                            color='#000000',
                            linewidth=.1)
                    elif self.variables["graph_style"] == "cubes":
                        z2 = iteration + 1
                        self.sub.plot(
                            [x1,x2,x2,x1,x1],
                            [y1,y1,y2,y2,y1],
                            [z1,z1,z1,z1,z1],
                            color='#000000',
                            linewidth=.1) # FORMAR CUBO
            if self.variables["plot_axises"]:
                if max(self.x) > self.maximum_x:
                    self.maximum_x = max(self.x)
                if max(self.y) > self.maximum_y:
                    self.maximum_y = max(self.y)
            if self.x == []:
                break
            self.Iterate()
        if self.variables["plot_axises"]:
            self.sub.plot([0,max(self.maximum_x,self.maximum_x,iteration)],[0,0],[0,0])
            self.sub.plot([0,0],[0,max(self.maximum_x,self.maximum_x,iteration)],[0,0])
            self.sub.plot([0,0],[0,0],[0,max(self.maximum_x,self.maximum_x,iteration)])


    def Iterate(self):
        new_x = []
        new_y = []
        x_range = range(min(self.x) - 1, max(self.x) + 2)
        y_range = range(min(self.y) - 1, max(self.y) + 2)
        for x_coordenate in x_range:
            for y_coordenate in y_range:
                alive_neighboring_cells = 0
                self.list_length = len(self.x)
                for index in range(self.list_length):
                    if x_coordenate - 1 == self.x[index] and y_coordenate - 1 == self.y[index]:
                        alive_neighboring_cells += 1
                    if x_coordenate - 1 == self.x[index] and y_coordenate == self.y[index]:
                        alive_neighboring_cells += 1
                    if x_coordenate - 1 == self.x[index] and y_coordenate + 1 == self.y[index]:
                        alive_neighboring_cells += 1
                    if x_coordenate == self.x[index] and y_coordenate - 1 == self.y[index]:
                        alive_neighboring_cells += 1
                    if x_coordenate == self.x[index] and y_coordenate + 1 == self.y[index]:
                        alive_neighboring_cells += 1
                    if x_coordenate + 1 == self.x[index] and y_coordenate - 1 == self.y[index]:
                        alive_neighboring_cells += 1
                    if x_coordenate + 1 == self.x[index] and y_coordenate == self.y[index]:
                        alive_neighboring_cells += 1
                    if x_coordenate + 1 == self.x[index] and y_coordenate + 1 == self.y[index]:
                        alive_neighboring_cells += 1
                if alive_neighboring_cells == 3:
                    new_x.append(x_coordenate)
                    new_y.append(y_coordenate)
                for index in range(self.list_length): # possivelmente irrelevante, mas não sei
                    if x_coordenate == self.x[index] and y_coordenate == self.y[index] and alive_neighboring_cells == 2:
                        new_x.append(x_coordenate)
                        new_y.append(y_coordenate)
        self.x = new_x
        self.y = new_y

    def GenerateGlider(self, x, y, quadrant):
        if quadrant == 1:
            self.x += [x + 2, x + 1, x, x + 2, x + 1]
            self.y += [y + 2, y + 2, y + 2, y + 1, y]
        if quadrant == 2:
            self.x += [x, x + 1, x + 2, x, x + 1]
            self.y += [y + 2, y + 2, y + 2, y + 1, y]
        if quadrant == 3:
            self.x += [x, x + 1, x + 2, x, x + 1]
            self.y += [y, y, y, y + 1, y + 2]
        if quadrant == 4:
            self.x += [x + 2, x + 1, x, x + 2, x + 1]
            self.y += [y, y, y, y + 1, y + 2]
        else:
            print("Escolha um número válido para o quadrante.")

    def GenerateBlinker3x1(self, x, y, horizontal_or_vertical):
        if horizontal_or_vertical == "H":
            self.x += [x, x + 1, x + 2]
            self.y += [y, y, y]
        if horizontal_or_vertical == "V":
            self.x += [x, x, x]
            self.y += [y, y + 1, y + 2]
        else:
            print("Escolha uma orientação válida")

    def GenerateBlinker(self, x, y):
        self.x += [x, x + 1, x + 2, x + 1, x + 1]
        self.y += [y, y, y, y + 1, y - 1]

teste = GAME_OF_LIFE()