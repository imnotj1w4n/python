from random import*
##졸려요 응앙ㅇ
def lotto():
    lot = set()

    for i in range(6):
        lot.add(randint(1,45))
    
    lot = list(lot)
    lot.sort()
    print(lot)

lotto()
