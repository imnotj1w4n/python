a1=1
a2=1
a3=1
a4=1
a5=1
a6=1
a7=1
a8=1
a9=1
a10=1
#-----------------------#
b1=1
b2=1
b3=1
b4=1
b5=1
b6=1
b7=1
b8=1
b9=1
b10=1

r=0


ascore = 0
bscore = 0

while r!=10:
   a = int(input("a"))
   
   b = int(input("b"))
   
   if a1==1 and a==1:
       ##print('1')
       a1=0
   if a2==1 and a==2:
       ##print('2')
       a2=0

   if a3==1 and a==3:
       ##print('3')
       a3=0

   if a4==1 and a==4:
       ##print('4')
       a4=0

   if a5==1 and a==5:
       ##print('5')
       a5=0 

   if a6==1 and a==6:
       ##print('6')
       a6=0
       
   if a7==1 and a==7:
       ##print('7')
       a7=0

   if a8==1 and a==8:
       ##print('8')
       a8=0

   if a9==1 and a==9:
       ##print('9')
       a9=0

   if a10 == 1 and a==10:
       ##print('10')
       a10=0

   if b1==1 and b==1:
       ##print('1')
       b1=0
   if b2==1 and b==2:
       ##print('2')
       b2=0

   if b3==1 and b==3:
       ##print('3')
       b3=0

   if b4==1 and b==4:
       ##print('4')
       a4=0

   if b5==1 and b==5:
       ##print('5')
       b5=0 

   if b6==1 and b==6:
       ##print('6')
       b6=0
       
   if b7==1 and b==7:
       ##print('7')
       b7=0

   if b8==1 and b==8:
       ##print('8')
       b8=0

   if b9==1 and b==9:
       ##print('9')
       b9=0

   if b10==1 and b==10:
       ##print('10')
       b10=0
    
   if a>10:
        print("이건 안돼 0잉야")
        a==0
   if b>10:
        print("이건 안돼 0잉야")
        b=0
        
   if a>b:
        ascore+=1
   if b>a :
        bscore+=1
   if b==a:
        print("wow")
   r+=1


if ascore>bscore:
    print("우왕ㅇa가 이겻다")

if ascore<bscore:
    print("우왕ㅇb가 이겻다")

if ascore==bscore:
    print("비겻당")
