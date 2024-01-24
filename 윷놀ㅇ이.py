import random 


for r in range(0,3):

    a=random.randint(0,1)
    b=random.randint(0,1)
    c=random.randint(0,1)
    d=random.randint(0,1)

    if a+b+c+d==0:
        print("E")
    if a+b+c+d==1:
        print("A")
    if a+b+c+d==2:
        print("B")
    if a+b+c+d==3:
        print("C")
    if a+b+c+d==4:
        print("D")
