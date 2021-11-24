# code used on a math competition

for m in range(1, 100000):
    for n in range(1, 100000):
        if m%60==0 and n%60==0 and m<n and 2079000%m==0 and 2079000%n==0 and m%35==0  and m%25!=0 and n%24==0 and n%9!=0 and (m+n) in [16340,27900,36780,44580,45200]:
            print(m, n)
            input("bruh")
        else:
            print(m)