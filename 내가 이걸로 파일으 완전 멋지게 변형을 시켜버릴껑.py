def read_file(file_name):
    f = open(file_name,"r")
    while True :
     line = f.readline()
     print(line.strip())
     if not line :
         break
    f.close()

########################

def write_file(file_name,mode):
    f = open(file_name,mode)
    i  = input("아무거나 입력하셍용ㅇ")
    
    f.write("%s"%i)

##############################

file_name = input("file_name:")
mode = input("file mode(r/w/a):")

if mode == "r":
    read_file(file_name)
else :
    write_file(file_name,mode)
