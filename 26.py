dels = [2,7]
ndels = [15,28,41]

summ = 0
minim = 0
maxim = 0
for i in range(3394,8600):
    if (i % 3 == 1 and i % 7 == 5):
        summ += i
        if i > maxim:
            maxim = i

print(maxim,summ)

#8587 1486388