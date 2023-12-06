def login (id,pw):
    id = int(input("아이디를 입력하세용ㅇ"))
    pw = int(input("비번응 입력하셍ㅇㅛ"))

    if id=='cube' and pw==1234:
         result = 1
    if id=='cube' and pw!=1234:
         result = 2
    if id!='cube' and pw==1234:
         result = 3
    if id!='cube' and pw!=1234:
         result = 4
def say (n):
     if result == 1: 
         return "로그인 지존이당"
     if result == 2:
         return "비밀번호를 확인해라ㅏ!"
     if result == 3:
         return "아이디가 이상해ㅐ"
     if result == 4:
         return "완전 나빠"


n = login(id,pw)



     
