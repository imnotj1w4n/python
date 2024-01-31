for i in range(2,100):
    s=1

    for j in range(2,i):
       
        if i%j==0:
            s=0
            
        
    if s==1:
        print(i)
