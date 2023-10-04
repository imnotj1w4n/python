from random import *

n1=randint(1,9)
n2=randint(1,9)
n3=randint(1,9)
n4=randint(1,9)
n5=randint(1,9)

print ("%d %d %d %d %d"%(n1,n2,n3,n4,n5))
num=(n1*n1+n2*n2+n3*n3+n4*n4+n5*n5)
print("%d"%(num%10))
