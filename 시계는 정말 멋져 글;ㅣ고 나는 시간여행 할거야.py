h = int(input("시 입력:"))
m = int(input("분 입력:"))
s = int(input("초 입력:"))
t = int(input("초 입력하세용ㅇ:"))

s = s- t%60
t = t/60
if (t>59):
 h = h- t/60
 m =m - t%60

else :
    m = m-t

if(m<0):
    h-=1
    m6

print ("%d %d %d"%(h,m,s))
