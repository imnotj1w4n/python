def login(id,pw):##로그인 시스템
    if id=='cube' and pw=='1234' :
         return 1
    elif id=='cube':
         return 2
    elif pw=='1234' :
         return 3
    else:
         return 4
         
def say(n):##로그인할때 나오는 문자들
     if i == 1: 
         return "로그인 지존이당"
     elif i == 2:
         return "비밀번호를 확인해라ㅏ!"
     elif i == 3:
         return "아이디가 이상해ㅐ"
     elif i == 4:
         return "완전 나빠"


a = input("아이디를 입력하세용ㅇ")
b = input("비번응 입력하셍ㅇㅛ")
result = 0
i = login(a,b)
print(say(i))
        





