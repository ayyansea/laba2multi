import os
import sys
import string

#7 вариант - обход змейкой

data = open('data.txt', 'rw')
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

yb = len(b)
xb = len(b[0])

n = 0 
m = 0
nt = 0 
mt = 0

xstop = False
ystop = False
xmove = False
ymove = False
run = True

c = []

if run == True:
    if ystop == False:
        if n != yb - 1 and m != 0:
            if xmove == False and ymove == False:
                print b[n][m]
                c.append(b[n][m])
                m += 1
                xmove = True
            elif xmove == True and ymove == False:
                print b[n][m]
                c.append(b[n][m])
                n = m
                m = 0
                xmove = False
                ymove = True
            elif xmove == False and ymove == True:
                print b[n][m]
                c.append(b[n][m])
                n += 1
                xmove = True
            elif xmove == True and ymove == True:
                print b[n][m]
                c.append(b[n][m])
                m = n
                n = 0
                xmove = False
                ymove = False
        else:
            ystop = True
    else:
        run = False





        









    
