import random
n = 0
c  = random.randint(1,100)
print("%s"%c)
while n != c:
    n = int(input("수를 입력하세요"))
    if n > c:
        print("down")
    if n < c:
        print("up")
    if n ==c:
        print("correct")
