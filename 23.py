dels = [2,7]
ndels = [15,28,41]

kol = 0
summ = 0
minim = 0
maxim = 0
for i in range(3232,8300):
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
    if ndelit == len(ndels) and delit > 0:
    #if delit ==  2:
        #kol+=1
        if maxim < i:
            maxim = i
        if summ == 0:
            minim = i
            summ+=1
                
    #    summ += i

#print(kol)
print(minim)
print(maxim)

#3232 8298