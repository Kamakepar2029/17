def toit(num,base):
    num = int(num)
    base = int(base)
    newNum = ''
    while num > 0:
        if (num % base == 10):
            newNum = 'A' + newNum
        elif (num % base == 11):
            newNum = 'B' + newNum
        elif (num % base == 12):
            newNum = 'C' + newNum
        elif (num % base == 13):
            newNum = 'D' + newNum
        elif (num % base == 14):
            newNum = 'E' + newNum
        elif (num % base == 15):
            newNum = 'F' + newNum
        else:
            newNum = str(num % base) + newNum
        num //= base
    return(newNum)

kol = 0
for i in range(331,8752):
    sixt = len(toit(i,16))
    tens = len(str(i))
    if (sixt == tens and i%5==0 and i%25!=0):
        kol+=1
        if kol == 1:
            minim = i

print(kol,minim)