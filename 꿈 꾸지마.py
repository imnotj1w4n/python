t=int(input("4611686018427387904 이하의 숫자를 입력해라"))
n=0
c=0
i=0
m=0
while(t>10):
 i=t%10
 n=n+i
 c+=1
 print(n)
 m=t/10
