s=int(input("정수 입력"))
j=0
for i in range(1,s):
    if i % 3==0:
        j+=i
    else:
        print(":D")

print(j)
