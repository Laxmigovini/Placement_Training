bills = [5,5,5,10,20]
def lemonade(bills):
    five = 0
    ten = 0
    n = len(bills)
    t = True
    if bills[0] != 5:
        return False
    for i in range(n):
        if bills[i] == 5:
            five += 1
        elif bills[i] == 10:
            if five > 0:
                five -= 1
            else:
                t = False
            ten += 1
        else:
            if five > 0 and ten > 0:
                five -= 1
                ten -= 1
            elif five > 2:
                five -= 3
            else:
                return False
    return True
print(lemonade(bills))