def  f(n):
    if n==1:
        return 1
    else:
        return n +f(n-1)
n = int(input("정수 입력"))
fac = f(n)
print(fac)
