h = int(input("시 입력:"))
m = int(input("분 입력:"))
t = int(input("하하:"))

if (t>59):
 h = h+ t/60
 m = m + t%60

else :
    m = m+t

if(m<0):
    h+=1
    m=m*(-1)
    
    
if(m>59):
 h+=1
 m-=60
 
if(h>=24):
 h-=24

print ("%d %d"%(h,m))
