def avr(n,tot):
    avg = tot / n
    return avg

def total():
    tot = 0
    score = input("score").split()

    for i in score:
        tot += int(i)

        avg = avr(len(score),tot)

        print("total score: %d"% tot)
        print("avr score : %.2f"%avg)

total()
