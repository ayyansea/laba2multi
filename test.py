i = 1
n = 0
m = 0

num = 4

dcount_1 = 4
dcount_2 = 7

# i - номер диагонали
# j - количество элементов в диагонали

# идем включительно до главной диагонали
for i in range(1, dcount_1 + 1):
    if i % 2 != 0:
        if i == 1:
            n = 0
        else:
            n = i - 1
        m = 0
        for j in range(i):
            if i == 1:
                print(n, m)
                m += 1
            else:
                print(n, m)
                n -= 1
                m += 1
        print("\n")
    elif i % 2 == 0:
        n = 0
        m = i - 1
        for j in range(i):
            print(n, m)
            n += 1
            m -= 1
        print("\n")

dcount_3 = dcount_1 + 1

# смотрим диагонали после главной 

for i in range(dcount_3, dcount_2 + 1):
    if i % 2 != 0:
        n = num - 1
        m += 2
        for j in range((dcount_2 + 1) - i):
            print(n, m)
            n -= 1
            m += 1
        print("\n")
    elif i % 2 == 0:
        m = 3
        n += 2
        for j in range((dcount_2 + 1) - i):
            print(n, m)
            n += 1
            m -= 1
        print("\n")


for j in range(1):
    print(j)