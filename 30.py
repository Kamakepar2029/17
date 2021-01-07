summ = 0
p = 0
mini = 0
for i in range(1529,8433):
    if (bin(i)[-2:] == '01' and i%5 == 3):
        #print(bin(i))
        #print(bin(i)[-2:])
        summ+=i
        if mini == 0:
            mini = i

print(mini,summ)


#1533 1715685