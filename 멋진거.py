n = int(input("난 멋져"))
num = 0
for i in range(1,n+1):
    if i % 3 == 0:
        num+=i
        print("%d"%num)
