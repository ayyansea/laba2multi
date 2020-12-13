a = 0
b = 2
c = 3

while a != 5:
    if b % 2 == 0:
        print c
        b += 1
        a += 1
    elif c % 2 == 1:
        print b
        c += 1
        a += 1
    elif b % 2 == 1:
        print b 
        b += 1
        a += 1
    elif c % 2 == 0:
        print c
        c += 1
        a += 1