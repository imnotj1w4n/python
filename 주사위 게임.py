import random
A = random.randint(1,6)
B = random.randint(1,6)
AA=A
BB=B
print("🎲=====☝첫번째 주사위☝=====🎲")
print(  "😎{you}A(%d)🎲-----🤖{b.o.t}B(%d)🎲\n"%(A,B))


A = random.randint(1,6)
B = random.randint(1,6)

AA=AA+A
BB=BB+B
print("🎲=====✌두번째 주사위✌=====🎲")
print(  "😎{you}A(%d)🎲-----🤖{b.o.t}B(%d)🎲\n"%(A,B))


print("🎲===== 🥁게임 결과🥁 =====🎲")
print(  "😎{you}A(%d)🎲-----🤖{b.o.t}B(%d)🎲\n"%(AA,BB))

if AA>=10:
    print("🎉🏆이겻당🏆🎉=승자[you]😎")
    
if BB>=10:
    print("졋당=승자[b.o.t]🤖")

elif (AA>=10 and BB>= 10)or(AA<=10 and BB<= 10):
    if AA>BB :
        print("🎉🏆이겻당🏆🎉=승자[you]😎")
    if BB>AA :
        print("졋당=승자[b.o.t]🤖")
























































##c언어 너무 어려ㅝ요 다 끝나긴 햇는데 엉엉ㅜㅜㅜㅜ 
