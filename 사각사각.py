def f(n):
 for j in range(1,n+1):
     print()
     for i in range(1,n+1):
         print (j*i,end=' ')


n = int(input("100이하 정수 입력"))
f(n)
