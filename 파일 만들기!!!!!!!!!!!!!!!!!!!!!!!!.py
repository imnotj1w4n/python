##f = open("멋진파일.txt","w")
##name = input("name : ")
##age = input("age ; ")
##f.write("name : %s\n" %name)
##f.write("age : %s\n" %age)


##f = open ("멋진파일.txt","a")
##sch = input("sch ; ")
##f.write("sch : %s\n" %sch)
##
##f.close()

##f = open("멋진파일.txt","r")
##f.seek(23)
##while True :
## line = f.readline()
## print(line.strip())
## if not line :
##     break
##f.close()

##f = open("멋진파일.txt","w")
##f.write("abcdefghigklmnopqrstuvwxyz")
##f.close()

##f = open ("멋진파일.txt","r")
##index = int(input("정수 입력"))
##f.seek(index)
##while True :
## line = f.readline()
## print(line.strip())
## if not line :
##     break
##f.close()

f = open("fruit.txt","r")
word = f.readlines()

for  i in word:
    if len(i) > 10:
        print(i)



