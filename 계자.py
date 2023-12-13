def m(n):
    if n>=3 and n<=5:
        print("봄")
    if n>=6 and n<=8:
        print("여름")
    if n>=9 and n<=11:
        print("가을")
    if n==12 or n==1 or n==2:
        print("겨울")
            
n = int(input("엄"))
m(n)
