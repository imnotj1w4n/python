import random
c = random.randint(1,3)

a=0 ##나
b=0 ##컴

u = int(input('가위 :1 // 바우ㅏㅣㅇ :2// 보 :3 \n'))


   
if u == 1:
     a="가위"
     
if u == 2:
     a="바으ㅟ "

if u == 3:
    a = "보 "
#################################
if c == 1:
    b="가위"
     
if c == 2:
     b="바으ㅟ "

if c == 3:
    b = "보 "

print("나 : %s == 컴 : %s"%(a,b))

if (u==1 and c ==3) or (u==2 and c ==1) or (u==3 and c ==2) :
        print ("이겻당")

elif (c==1 and u ==3) or (c==2 and u ==1) or (c==3 and u ==2) :
        print ("졋당")
else :
    print("비겻당")


 
