def toit(num,base):
    num = int(num)
    base = int(base)
    if not(2 <= base <= 9):
        return('Nothing good')
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return(newNum)

kol = 0
for i in range(3712,8433):
    if (toit(i,2)[-1:] == toit(i,4)[-1:] and i%13==0 and i%14==0 or i%15==0):
        if kol == 0:
            minim = i
        kol=kol+1

print(kol,i)

#327 8432