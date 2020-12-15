import os
import sys
import string

#7 вариант - обход змейкой (квадратный массив)

data = open('data.txt', 'r')
txt = data.read()

a = txt.splitlines()
b = []

for i in a:
    temp = i.split(' ')
    b.append(temp)
    temp = []

for i in b:
    for j in range(len(i)):
        i[j] = int(i[j])

num = len(b)

def diagCount(num):
    count = 2*num - 1
    return count

dcount = diagCount(num)

c = []

n = 0
m = 0

dcount_1 = round(dcount/2 - 0.01) + 1 # до главной диагонали включительно
dcount_2 = dcount_1 + 1 # оставшиеся диагонали

for i in range(1, dcount_1 + 1):
    if i % 2 != 0:
        if i == 1:
            n = 0
        else:
            n = i - 1
        m = 0
        for j in range(i):
            if i == 1:
                c.append(b[n][m])
                m += 1
            else:
                c.append(b[n][m])
                n -= 1
                m += 1
        print("\n")
    elif i % 2 == 0:
        n = 0
        m = i - 1
        for j in range(i):
            c.append(b[n][m])
            n += 1
            m -= 1
        print("\n")

# смотрим диагонали после главной 
m = 1

for i in range(dcount_2, dcount + 1):
    if i % 2 != 0:
        if i != dcount:
            n = num - 1
            for j in range((dcount + 1) - i):
                c.append(b[n][m])
                n -= 1
                m += 1
            print("\n")
        if i == dcount:
            c.append(b[num - 1][num - 1])
    elif i % 2 == 0:
        m = num - 1
        n += 2
        for j in range((dcount + 1) - i):
            c.append(b[n][m])
            n += 1
            m -= 1
        print("\n")
        m += 2


with open("output.txt", 'w') as f:
    for item in c:
        f.write("%s\n" % str(item))







        









    
