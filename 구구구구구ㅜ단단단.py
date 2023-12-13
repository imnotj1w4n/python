def f(a,b):
    if a>b:
        for i in range (b,a+1):
            for j in range (1,9):
                n = i*j
                print(n)
    
    for i in range (a,b+1):
        for j in range (1,9):
            n = i*j
            print(n)


a=int(input("첫번째!"))
b=int(input("두번째ㅐㅐ"))

f(a,b)
