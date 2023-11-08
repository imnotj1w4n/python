##가위[1] 바위[2] 보[3]
import random
w1=0
w2=0
w3=0
w4=0
w5=0
##플레이어 카드 선택
p1=random.randint(1,3)

if p1==1:
    p1="가위"
if p1==2:
    p1="바위"
if p1==3:
    p1="보"
    
p2=random.randint(1,3)

if p2==1:
    p2="가위"
if p2==2:
    p2="바위"
if p2==3:
    p2="보"
    
p3=random.randint(1,3)

if p3==1:
    p3="가위"
if p3==2:
    p3="바위"
if p3==3:
    p3="보"
    
p4=random.randint(1,3)

if p4==1:
    p4="가위"
if p4==2:
    p4="바위"
if p4==3:
    p4="보"
    
p5=random.randint(1,3)

if p5==1:
    p5="가위"
if p5==2:
    p5="바위"
if p5==3:
    p5="보"

print("you[%s %s %s %s %s]"%(p1,p2,p3,p4,p5))

##컴 카드 선택
C1=random.randint(1,3)

if C1==1:
    C1="가위"
if C1==2:
    C1="바위"
if C1==3:
    C1="보"
    
C2=random.randint(1,3)

if C2==1:
    C2="가위"
if C2==2:
    C2="바위"
if C2==3:
    C2="보"
    
C3=random.randint(1,3)

if C3==1:
    C3="가위"
if C3==3:
    C3="보"
if C3==2:
    C3="바위"
    
C4=random.randint(1,3)

if C4==1:
    C4="가위"
if C4==2:
    C4="바위"
if C4==3:
    C4="보"
    
C5=random.randint(1,3)

if C5==1:
    C5="가위"
if C5==2:
    C5="바위"
if C5==3:
    C5="보"

print("BOT[%s %s %s %s %s]"%(C1,C2,C3,C4,C5))

##첫번쨰플레이어 카드 사용#########

num =int(input('사용할 카드 번호'))

if num== 1:
    
    print("p1 사용불가")
if num== 2:
    
    print("p2 사용불가")
if num== 3:
    
    print("p3 사용불가")
if num== 4:
    
    print("p4 사용불가")
if num== 5:
    
    print("p5 사용불가")

##첫번쨰플레이어 카드 사용 끝#############
    ###컴퓨터의 사용 1####
cnum = random.randint(1,5)
    
if cnum== 1:
    
    print("C1 사용불가")
if cnum== 2:
    
    print("C2 사용불가")
if cnum== 3:
    
    print("C3 사용불가")
if cnum== 4:
    
    print("C4 사용불가")
if cnum== 5:
    
    print("C5 사용불가")
###########################
if num == 1:
    if p1 == "가위":
        w1=1
    if p1 == "바위":
        w1=2
    if p1 == "보":
        w1=3
     
if num == 2:
    if p2 == "가위":
     w2="1"
    if p2 == "바위":
     w2="2"
    if p2 == "보":
     w2="3"
     
if num == 3:
    if p3 == "가위":
     w3="1"
    if p3 == "바위":
     w3="2"
    if p3 == "보":
     w3="3"
     
if num == 4:   
    if p4 == "가위":
     w4="1"
    if p4 == "바위":
     w4="2"
    if p4 == "보":
     w4="3"
     
if num == 5:    
    if p5 == "가위":
     w5="1"
    if p5 == "바위":
     w5="2"
    if p5 == "보":
     w5="3"



     
print("%d"%w1)




