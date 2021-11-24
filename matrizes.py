import random


def show(l, x):
    s = ""
    for i, item in enumerate(l):
        if i % int(len(l) ** (1 / 2)) == 0:
            if i != 0:
                s += " |"
            s += "\n —" + "—" * (x * max(len(str(max(l))), len(str(min(l))) + 3)) + "\n"
        while len(str(item)) < max(len(str(max(l))), len(str(min(l)))):
            item = " " + str(item)
        s += " | " + str(item)
    s += " |" + "\n —" + "—" * x * max(len(str(max(l))), len(str(min(l))) + 3)
    print(s)


def laplace(l, x):
    if x == 3:
        return sarrus(l)
    s = 0
    for n in range(x):
        ll = []
        for i in range(len(l)):
            if i >= x and i % x != n:
                ll.append(l[i])
        s += l[n] * ((-1) ** n) * laplace(ll, x - 1)
    return s


def sarrus(l):
    return (
        (l[0] * l[4] * l[8])
        + (l[1] * l[5] * l[6])
        + (l[2] * l[3] * l[7])
        - (l[2] * l[4] * l[6])
        - (l[1] * l[3] * l[8])
        - (l[0] * l[5] * l[7])
    )


def interface(x):
    if x == "x":
        x = input(
            "Welcome to this program about matrixes!\n\nPress 'A' to calculate the determinant of a matriz\n\n>>> "
        ).lower()
    if x == "a":
        l = []
        y = input(
            "A to put a matrix manually\nB to generate a random one\n\n>>> "
        ).lower()
        if y == "a":
            length = int(input("Order: "))
            c = 0
            while c < length ** 2:
                l.append(int(input("value: ")))
                c += 1
            print("\n")
            show(l, length)
            print("\n")
            print("Determinant: " + str(laplace(l, length)))
        if y == "b":
            length = int(input("Order: "))
            lower_bound = int(input("Lower bound: "))
            upper_bound = int(input("Upper bound: "))
            for i in range(length ** 2):
                l.append(random.randint(lower_bound, upper_bound))
            print("\n")
            show(l, length)
            print("\n")
            print("Determinant: " + str(laplace(l, length)))
    else:
        print("invalid entry")
        interface("x")


interface("x")
