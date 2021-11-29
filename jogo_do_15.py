import random, struct

hasmatplot = (
    "y"
    == input(
        "Este programa utiliza da biblioteca matplotlib. Digite 'y' se a possui. Caso contrário, funcionalidades dependentes não serão executadas. > "
    ).lower()
)
if hasmatplot:
    import matplotlib.pyplot as plt

    plt.style.use("dark_background")
import time


class Game:
    def __init__(
        self, x=4, printgame=True, solve=True, fair=False, shuffle=1000, worst=False
    ):
        self.printgame = printgame
        self.x = x

        self.counter = 0
        self.kup, self.kdown, self.kleft, self.kright = (
            ["w", "^[[A"],
            ["s", "^[[B"],
            ["a", "^[[D"],
            ["d", "^[[c"],
        )

        if worst:
            a = The_Worst(x=x)
            self.l = a.l
        elif fair:
            self.fairFill(shuffle)
            self.counter -= shuffle
        else:
            self.fill()
        # self.l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 13, 14, 12, 0]

        if solve:
            self.solve()
        else:
            self.play()

    def fairFill(self, shuffle):
        backup_printgame = self.printgame
        self.printgame = False
        self.l = list(range(1, self.x ** 2)) + [0]
        for i in range(shuffle):
            self.move(["w", "a", "s", "d"][random.randint(0, 3)])
        self.printgame = backup_printgame

    def fill(self):
        self.l = list(range(self.x ** 2))
        random.shuffle(self.l)

    def solve(self):
        self.timer = time.time()
        if self.x > 2:
            for i in range(1, len(self.l) - 3 * self.x + 1):
                if self.l[i - 1] == i:
                    self.move("d" * self.x)
                    continue
                self.toLine(i)
                self.toColumn(i)
                self.vPlace(i)
                self.hPlace(i)
                self.place(i)
            l1 = list(range(len(self.l) - 3 * self.x + 1, len(self.l) - 2 * self.x - 1))
            l2 = list(range(len(self.l) - 2 * self.x + 1, len(self.l) - 1 * self.x - 1))
            l3 = list(range(len(self.l) - 1 * self.x + 1, len(self.l) - 1))
            new_l = []
            for i in range(self.x - 2):
                new_l += [l1[i], l2[i], l3[i]]
            for i in new_l:
                if self.l[i - 1] == i:
                    continue
                self.alt_toColumn(i)
                self.alt_toLine(i)
                self.alt_hPlace(i)
                self.alt_vPlace(i)
                self.alt_place(i)
            self.final6(
                len(self.l) - self.x * 2 - 1,
                len(self.l) - self.x * 2,
                len(self.l) - self.x - 1,
                len(self.l) - self.x,
                len(self.l) - 1,
            )
        else:
            self.final4(len(self.l) - self.x - 1, len(self.l) - self.x, len(self.l) - 1)
        self.timer = time.time() - self.timer

        print("\n\nTempo: " + str(self.timer) + "\n")
        print("Movimentos: " + str(self.counter) + "\n\n")

    def play(self):
        print(
            "W -> Subir o espaço livre\nA -> Recuar o espaço livre\nS -> Descer o espaço livre\nD -> Avançar o espaço livre\n\nX -> Parar"
        )
        self.show()
        t = ""
        self.timer = time.time()
        while "x" != t.lower():
            if self.l == list(range(1, self.x ** 2)) + [0]:
                self.timer = time.time() - self.timer
                print(
                    """\nParabéns! Você Venceu!
                
                
       ///////////////////////////// 
        /////////////////////////// 
   ////////////////////////////////////// 
 ////////////////////////////////////////// 
////      ///////////////////////       //// 
///       ///////////////////////        /// 
//        ///////////////////////        /// 
///     ///////////////////////////      /// 
///    /////////////////////////////    //// 
 ///   /// ///////////////////// ///    /// 
 ////   /// /////////////////// ////  //// 
   ////  ////////////////////////// ///// 
    //////// ///////////////// ///////// 
      //////  ///////////////   ////// 
               ///////////// 
                 ///////// 
                   ///// 
                   ///// 
                   ///// 
                   ///// 
               ///////////// 
            /////////////////// 
            /////////////////// 
            ///             /// 
            ///   w(·o·)w   /// 
            ///             ///"""
                )
                print(
                    "            ///"
                    + " " * (6 - len(str(self.x)))
                    + str(self.x)
                    + "x"
                    + str(self.x)
                    + " " * (6 - len(str(self.x)))
                    + "///"
                )
                print(
                    """            ///             /// 
            /////////////////// 
            /////////////////// 
          /////////////////////// 
         /////////////////////////"""
                )
                print("\n\nTempo: " + str(self.timer) + "\n")
                print("Movimentos: " + str(self.counter) + "\n\n")
                t = "x"
            t = input(" >>>")
            self.move(t)

    def show(self):
        s = ""
        for i, item in enumerate(self.l):
            if i % int(len(self.l) ** (1 / 2)) == 0:
                if i != 0:
                    s += " |"
                s += "\n —" + "—" * (self.x * (len(str(max(self.l))) + 3)) + "\n"
            if item == 0:
                item = " "
                while len(str(item)) < len(str(max(self.l))):
                    item += " "
            else:
                while len(str(item)) < len(str(max(self.l))):
                    item = "0" + str(item)
            s += " | " + str(item)
        s += " |" + "\n —" + "—" * self.x * (len(str(max(self.l))) + 3)
        print(s)

    def move(self, T):
        for t in T:
            self.counter += 1
            l2 = self.l[::]
            i0 = self.l.index(0)
            if t.lower() in self.kup and i0 > self.x - 1:
                self.l[i0] = l2[i0 - self.x]
                self.l[i0 - self.x] = 0
            if t.lower() in self.kleft and i0 % self.x != 0:
                self.l[i0] = l2[i0 - 1]
                self.l[i0 - 1] = 0
            if t.lower() in self.kdown and i0 < len(self.l) - self.x:
                self.l[i0] = l2[i0 + self.x]
                self.l[i0 + self.x] = 0
            if t.lower() in self.kright and i0 % self.x != self.x - 1:
                self.l[i0] = l2[i0 + 1]
                self.l[i0 + 1] = 0
            if self.printgame:
                self.show()

    def toLine(self, n):
        i0 = self.l.index(0)
        i = self.l.index(n)
        if i0 % self.x == self.x - 1 and i % self.x == self.x - 1:
            self.move("a")
            i0 = self.l.index(0)
            i = self.l.index(n)
        elif i0 % self.x == i % self.x:
            self.move("d")
            i0 = self.l.index(0)
            i = self.l.index(n)
        while i0 // self.x > i // self.x:
            self.move("w")
            i0 = self.l.index(0)
            i = self.l.index(n)
        while i0 // self.x < i // self.x:
            self.move("s")
            i0 = self.l.index(0)
            i = self.l.index(n)

    def toColumn(self, n):
        i0 = self.l.index(0)
        i = self.l.index(n)
        while i0 % self.x > i % self.x:
            self.move("a")
            i0 = self.l.index(0)
            i = self.l.index(n)
        while i0 % self.x < i % self.x:
            self.move("d")
            i0 = self.l.index(0)
            i = self.l.index(n)

    def vPlace(self, n):
        i = self.l.index(n)
        while i // self.x < (n - 1) // self.x + 1:
            self.move("sawds")
            i = self.l.index(n)
        while i // self.x > (n - 1) // self.x + 1:
            self.move("wasdw")
            i = self.l.index(n)

    def hPlace(self, n):
        i = self.l.index(n)
        while i % self.x < self.x - 2:
            self.move("asddw")
            i = self.l.index(n)
        if n % self.x == 0:
            self.move("a")
            i = self.l.index(n)
        else:
            while i % self.x > n % self.x - 1:
                self.move("saawd")
                i = self.l.index(n)

    def place(self, n):
        i0 = self.l.index(0)
        i = self.l.index(n)
        if n % self.x == 0:
            while i0 % self.x > 0:
                self.move("a")
                i0 = self.l.index(0)
                i = self.l.index(n)
            self.move("w")
            i0 = self.l.index(0)
            i = self.l.index(n)
            while i0 % self.x < i % self.x:
                self.move("d")
                i0 = self.l.index(0)
                i = self.l.index(n)
            self.move("saw")
            while i0 % self.x > 0:
                self.move("a")
                i0 = self.l.index(0)
                i = self.l.index(n)
            self.move("s")
            i0 = self.l.index(0)
            i = self.l.index(n)
        else:
            self.move("wasd")
            i0 = self.l.index(0)
            i = self.l.index(n)

    def alt_toColumn(self, n):
        self.move("s")
        i0 = self.l.index(0)
        i = self.l.index(n)
        if i0 // self.x == i // self.x:
            if i // self.x == self.x - 1:
                self.move("w")
                i0 = self.l.index(0)
                i = self.l.index(n)
            else:
                self.move("s")
                i0 = self.l.index(0)
                i = self.l.index(n)
        while i0 % self.x > i % self.x:
            self.move("a")
            i0 = self.l.index(0)
            i = self.l.index(n)
        while i0 % self.x < i % self.x:
            self.move("d")
            i0 = self.l.index(0)
            i = self.l.index(n)

    def alt_toLine(self, n):
        i0 = self.l.index(0)
        i = self.l.index(n)
        while i0 // self.x > i // self.x:
            self.move("w")
            i0 = self.l.index(0)
            i = self.l.index(n)
        while i0 // self.x < i // self.x:
            self.move("s")
            i0 = self.l.index(0)
            i = self.l.index(n)

    def alt_hPlace(self, n):
        i = self.l.index(n)
        while i % self.x < (n - 1) % self.x + 1:
            self.move("dwasd")
            i = self.l.index(n)
        while i % self.x > (n - 1) % self.x + 1:
            self.move("awdsa")
            i = self.l.index(n)

    def alt_vPlace(self, n):
        i = self.l.index(n)
        while i // self.x < self.x - 2:
            self.move("wdssa")
            i = self.l.index(n)
        if n // self.x == self.x - 1:
            self.move("w")
            i = self.l.index(n)
        else:
            while i // self.x > (n - 1) // self.x:
                self.move("dwwas")
                i = self.l.index(n)

    def alt_place(self, n):
        if n // self.x == self.x - 1:
            self.move("wassdwawd")
        else:
            self.move("awd")

    def final6(self, a, b, c, d, e):
        self.move("dssaww")
        while a != self.l[a - 1]:
            if a == self.l[b - 1]:
                self.move("d")
            elif a == self.l[c - 1]:
                self.move("s")
            else:
                self.move("ssdwwa")
        self.move("dssaw")
        while b != self.l[b - 1]:
            while b != self.l[e]:
                self.move("dsaw")
            self.move("dwaassdwdsaawwddss")
        self.final4(c, d, e)

    def final4(self, a, b, c):
        self.move("ds")
        verifier = 0
        while not (a == self.l[a - 1] and b == self.l[b - 1] and c == self.l[c - 1]):
            verifier += 1
            self.move("wasd")
            if verifier > 5:
                if self.printgame:
                    print("Impossível!")
                break


class Worst(Game):  # the next is always in last
    def __init__(self, x=4, printgame=False):
        self.printgame = printgame
        self.x = x

        self.counter = 0
        self.kup, self.kdown, self.kleft, self.kright = (
            ["w", "^[[A"],
            ["s", "^[[B"],
            ["a", "^[[D"],
            ["d", "^[[c"],
        )

        self.l = []

        for i in range(self.x ** 2):
            self.l.append(i)

        self.l = self.update(self.l, 0, self.l[0])
        self.l = self.update(self.l, 1, self.l[-1])

        self.ordem = list(range(1, len(self.l) - 3 * self.x + 1))

        l1 = list(range(len(self.l) - 3 * self.x + 1, len(self.l) - 2 * self.x - 1))
        l2 = list(range(len(self.l) - 2 * self.x + 1, len(self.l) - 1 * self.x - 1))
        l3 = list(range(len(self.l) - 1 * self.x + 1, len(self.l) - 1))

        self.new_l = []

        for i in range(self.x - 2):
            self.new_l += [l1[i], l2[i], l3[i]]
        self.ordem += self.new_l

        findWorst_timer = time.time()
        self.findWorst()
        print("Tempo para gerar Pior cenário:", time.time() - findWorst_timer)

    def findWorst(self):
        backup_l = self.l[::]
        for i in self.ordem:
            for j in self.ordem[: self.ordem.index(i)]:
                self.solve(j)
            backup_l = self.update(backup_l, i, self.l[-1])
            self.l = backup_l[::]
            if i == self.ordem[-1]:
                print("\nPior cenário:", self.l)

    def update(self, l, a, b):
        nl = []
        for i in range(len(l)):
            if l[i] == a:
                nl.append(b)
            elif l[i] == b:
                nl.append(a)
            else:
                nl.append(l[i])
        return nl

    def solve(self, i):
        self.timer = time.time()
        if self.x > 2:
            if i in list(range(1, len(self.l) - 3 * self.x + 1)):
                if self.l[i - 1] == i:
                    self.move("d" * self.x)
                else:
                    self.toLine(i)
                    self.toColumn(i)
                    self.vPlace(i)
                    self.hPlace(i)
                    self.place(i)
            if i in self.new_l:
                if self.l[i - 1] == i:
                    pass
                else:
                    self.alt_toColumn(i)
                    self.alt_toLine(i)
                    self.alt_hPlace(i)
                    self.alt_vPlace(i)
                    self.alt_place(i)
        #     self.final6(len(self.l) - self.x * 2 - 1, len(self.l) - self.x * 2, len(self.l) - self.x - 1, len(self.l) - self.x, len(self.l) - 1)
        # else:
        #     self.final4(len(self.l) - self.x - 1, len(self.l) - self.x, len(self.l) - 1)


class The_Worst(Worst):  # the actuall worst
    def findWorst(self):
        backup_l = self.l[::]

        for i in self.ordem:
            for j in self.ordem[: self.ordem.index(i)]:
                self.solve(j)

            if not i in self.new_l:
                if (i - 1) % self.x < self.x // 2:
                    backup_l = self.update(backup_l, i, self.l[-1])
                else:
                    backup_l = self.update(backup_l, i, self.l[-self.x])
            else:
                if i // self.x < self.x - 2:
                    backup_l = self.update(backup_l, i, self.l[-1])
                else:
                    backup_l = self.update(backup_l, i, self.l[-2 * self.x - 1])

            self.l = backup_l[::]
            if i == self.ordem[-1]:
                print("\nPior jogo:", self.l)


class Interface:
    def __init__(self):

        onoff = True

        while onoff:
            ABC = input(
                "\n\nEscolha uma das opções:\n\n  A. Jogar\n  B. Ver uma resolução \n  C. Gerar gráfico\n  D. Sobre\n\n >>> "
            )
            if ABC.lower() == "a":
                a = Game(
                    x=int(
                        input(
                            "\nEscolha o tamanho do Tabuleiro (default: 4, mínimo: 2):\n >>> "
                        )
                    ),
                    printgame=True,
                    solve=False,
                    fair=True,
                    shuffle=int(
                        input(
                            "\nEscolha a quantidade de embaralhamentos (default: 1000):\n >>> "
                        )
                    ),
                )
            elif ABC.lower() == "b":
                if "y" == input("(Y/n) Pior cenário? (!! bastante pesado !!)").lower():
                    a = Game(
                        x=int(
                            input(
                                "\nEscolha o tamanho do Tabuleiro (default: 4, mínimo: 2):\n >>> "
                            )
                        ),
                        printgame=True,
                        solve=True,
                        worst=True,
                    )
                elif "y" == input("(Y/n) Necessariamente resolvível?").lower():
                    a = Game(
                        x=int(
                            input(
                                "\nEscolha o tamanho do Tabuleiro (default: 4, mínimo: 2):\n >>> "
                            )
                        ),
                        printgame=True,
                        solve=True,
                        fair=True,
                        shuffle=int(
                            input(
                                "\nEscolha a quantidade de embaralhamentos (default: 1000):\n >>> "
                            )
                        ),
                    )
                else:
                    a = Game(
                        x=int(
                            input(
                                "\nEscolha o tamanho do Tabuleiro (default: 4, mínimo: 2):\n >>> "
                            )
                        ),
                        printgame=True,
                        solve=True,
                        fair=False,
                    )
            elif ABC.lower() == "c":
                grafico = input(
                    "\n\nEscolha um gráfico:\n\n  A. Movimentos\n  B. Tempo\n\n >>> "
                )
                while grafico.lower() not in ["a", "b"]:
                    print("\nTecla inválida!")
                    grafico = input(
                        "\n\nEscolha um gráfico:\n\n  A. Movimentos\n  B. Tempo\n\n >>> "
                    )

                prova = (
                    input(
                        "\n\nAplicar prova de que o crescimento é polinomial? ('y' para confirmar)\n(Ao aplicar a fórmula f(x+1)/f(x) com x tendendo ao infinito, o resultado tende a 1 caso f(x) seja um polinômio, e à base caso seja exponencial)\n\n>>>"
                    ).lower()
                    == "y"
                )

                self.label_x = "Tamanho"
                L = []
                m = int(input("Precisão (repetições / média) > "))
                if hasmatplot:
                    fig, ax = plt.subplots()
                if grafico.lower() == "a":
                    if prova:
                        self.label_y = "Movimentos (f(x+1)/f(x))"
                        self.title = (
                            "Relação Movimentos por Tamanho com precisão de "
                            + str(m)
                            + " repetições\n(com f(x+1)/f(x) tendendo a 1) "
                        )
                    else:
                        self.label_y = "Movimentos"
                        self.title = (
                            "Relação Movimentos por Tamanho com precisão de "
                            + str(m)
                            + " repetições"
                        )
                elif grafico.lower() == "b":
                    if prova:
                        self.label_y = "Tempo (f(x+1)/f(x))"
                        self.title = (
                            "Relação Tempo por Tamanho com precisão de "
                            + str(m)
                            + " repetições\n(com f(x+1)/f(x) tendendo a 1) "
                        )
                    else:
                        self.label_y = "Tempo"
                        self.title = (
                            "Relação Tempo por Tamanho com precisão de "
                            + str(m)
                            + " repetições"
                        )
                first = int(input("Tamanho inicial (mínimo e recomendado: 3) > "))
                last = (
                    int(
                        input(
                            "Tamanho final (recomendado 20 para execução regular e 12 para comparação com pior cenário) >"
                        )
                    )
                    + 1
                )
                R = range(first, last)
                for i in R:
                    numero = 0
                    for j in range(m):
                        print("\nTamanho:", i, "| Iteração:", j + 1)
                        a = Game(x=i, printgame=False, solve=True, fair=False)
                        if grafico.lower() == "a":
                            numero += a.counter
                        elif grafico.lower() == "b":
                            numero += a.timer
                    L.append(numero / m)
                R = list(R)
                if prova:
                    if hasmatplot:
                        plt.plot([first, last - 1], [1, 1], label="1")
                    R = R[1:]
                    L2 = []
                    for i in range(1, len(L)):
                        L2.append(L[i] / L[i - 1])
                    L = L2
                elif (
                    "y"
                    == input(
                        "Comparar com um tabuleiro do tipo 'Pior cenário', que necessita do máximo número de lances? ('y' para aceitar)\n (!!Bastante pesado!!)\n\n >>> "
                    ).lower()
                ):
                    L2 = []
                    for i in R:
                        print("Tamanho:", i, "| Pior cenário")
                        a = Game(x=i, printgame=False, fair=False, worst=True)
                        if grafico.lower() == "a":
                            L2.append(a.counter)
                        elif grafico.lower() == "b":
                            L2.append(a.timer)
                    title = self.title
                    if hasmatplot:
                        plt.plot(R, L2, "r-o", label="Pior cenário")
                    self.title = "Pior cenário:"
                    self.table(R, L2)
                    self.title = title
                self.table(R, L)
                if hasmatplot:
                    plt.plot(R, L, "g-o", label="Médias de " + str(m) + " repetições")
                    plt.title(self.title)
                    plt.xlabel(self.label_x)
                    plt.ylabel(self.label_y)
                    ax.legend()
                    plt.show()
            elif ABC.lower() == "d":
                print(
                    """
            O jogo original
        O jogo do 15 é um jogo composto por um tabuleiro de 4x4, onde números de 1 a 15 preenchem-no, permanecendo apenas uma casa livre. 
        O objetivo do jogo é organizá-los em ordem crescente, da esquerda à direita; começando no topo e descendo, deixando vazia a última casa. 
        Para mexer os números ao redor, basta usar a casa desocupada para locomover em seu lugar todo e qualquer número que estiver ao seu redor. 
        O número escolhido é trocado de lugar com a casa, criando assim uma nova casa vazia na posição desse mesmo número. 
        Como há no máximo quatro lados de escolha de troca, logo há no máximo quatro maneiras de locomover-se (esquerda, direita, cima, baixo).
            Tabuleiro Embaralhado:          Tabuleiro Resolvido:
            —————————————————————           —————————————————————
            | 08 | 03 | 02 | 14 |           | 01 | 02 | 03 | 04 |
            —————————————————————           —————————————————————
            | 12 | 15 | 06 | 11 |           | 05 | 06 | 07 | 08 |
            —————————————————————           —————————————————————
            | 04 |    | 01 | 05 |           | 09 | 10 | 11 | 12 |
            —————————————————————           —————————————————————
            | 09 | 13 | 10 | 07 |           | 13 | 14 | 15 |    |
            —————————————————————           —————————————————————
            Nosso programa
        Criamo-lo inicialmente com o quixotesco ímpeto por resolver a lendária questão P vs NP.
        Este programa genaraliza o Jogo do 15 para qualquer tamanho de tabuleiro quadrado, conforme requisição.
            Tablueiro de Tamanho 3 por 3:   Tablueiro de Tamanho 5 por 5:
                                             ——————————————————————————
                                             | 02 | 17 | 03 | 01 | 05 |
                   —————————————             ——————————————————————————
                   | 1 | 7 | 4 |             | 08 | 06 | 07 |    | 15 |
                   —————————————             ——————————————————————————
                   |   | 8 | 5 |             | 13 | 23 | 22 | 16 | 24 |
                   —————————————             ——————————————————————————
                   | 2 | 6 | 3 |             | 04 | 21 | 18 | 10 | 09 |
                   —————————————             ——————————————————————————
                                             | 12 | 11 | 20 | 19 | 14 |
                                             ——————————————————————————
        Com isso buscamos provar que a quantidade de operações necessárias cresce de forma polinomial em relação ao tamanho do tabuleiro,
        assim, provando que P é igual a NP, uma vez que este seja um problema do tipo 'NP completo'.
        
        Nas opções iniciais, pressioine 'A' para jogar o jogo usando 'w','a','s' e 'd' para movimentação;
        'B' para ver o algoritmo resolvendo um jogo;
        'C' para gerar um relatório de performance e 
        'D' para retornar a esta seção.
        
        Na seção de relatórios, é possível conferir a prova de que a quantidade de movimentos e o tempo do programa são polinomiais.
        Caso requisitado pelo usuário, o programa aplica a operação f(x+1)/f(x) sobre os tempos e quantidades de movimentos, sendo
        esta função uma prova do caráter polinomial do algoritmo, pois, para qualquer 'f(x)' polinomial o resultado de tal operação 
        tende a 1, e para 'f(x)' exponencial, ela tende à base da exponenciação.
        """
                )
            else:
                print("\nTecla inválida! Escolha uma das opções!")
            onoff = (
                input("Pressione 'Enter' para seguir e 'x' para encerrar > ").lower()
                != "x"
            )

    def table(self, R, L):
        s = ""
        n = 0
        self.label_x += " "
        self.label_y += " "

        while len(self.label_x) < len(self.label_y):
            self.label_x += " "

        while len(self.label_y) < len(self.label_x):
            self.label_y += " "

        for i in L:
            if len(str(i)) > n:
                n = len(str(i))
        s += "\n" + self.title + "\n"
        s += (
            len(self.label_x) * " " + "—" * ((n + 3) * len(L) + 1) + "\n" + self.label_x
        )
        for i in R:
            i = str(i)
            while len(i) < n:
                i += " "
            s += "| " + i + " "
        s += "|\n"

        s += (
            len(self.label_x) * " " + "—" * ((n + 3) * len(L) + 1) + "\n" + self.label_y
        )
        for i in L:
            i = str(i)
            while len(i) < n:
                i += " "
            s += "| " + i + " "
        s += "|\n"
        s += len(self.label_x) * " " + "—" * ((n + 3) * len(L) + 1) + "\n\n"
        print(s)


a = Interface()
