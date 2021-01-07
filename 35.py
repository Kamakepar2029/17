kol = 0
minim = 0
maxim = 0

for i in range(1476,7040):
    last = (i//10)%10
    if (i%2==0 and i%16!=0 and last >3):
        kol+=1
        if kol == 1:
            minim = i
        if maxim < i:
            maxim = i

print(kol,(minim+maxim)//2)