dels = [5]
ndels = [7,13,17,19]

kol = 0
summ = 0
minim = 0
for i in range(1200,11201):
    #print(i)
    print('__________')
    delit = 0
    ndelit = 0
    for d in dels:
        if i % d == 0:
            delit+=1
    for de in ndels:
        if i % de != 0:
            ndelit += 1
    #for de in dels:
        #if (i%de==0):
        #    delit +=1
    #print(ndelit)
    #print(delit)
    if ndelit == 4 and delit == 1:
    #if delit ==  2:
        kol+=1
        if summ == 0:
            minim = i
            summ+=1
                
    #    summ += i

print(kol)
print(minim)

#Answ: 1414 1200