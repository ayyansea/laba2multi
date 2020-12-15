import os
import sys
import string

#7 вариант - обход змейкой (квадратный массив) с выводом в файл output.txt

#открываем файл с изначальным массивом
data = open('data.txt', 'r')
#считываем из него текст
txt = data.read()

#кладем в массив a[] каждую строку отдельно 
a = txt.splitlines()
#объявляем вспомогательный массив b[]
b = []

#разбиваем строки на отдельные элементы и кладем их в массив b
for i in a:
    temp = i.split(' ')
    b.append(temp)
    temp = []

#приводим элементы к целочисленному типу (можно было бы и без этого, но пусть будет)
for i in b:
    for j in range(len(i)):
        i[j] = int(i[j])

#определяем размерность массива
num = len(b)

#функция, определяющая количество диагоналей в массиве
#количество диагоналей основывается на простой арифметической прогрессии
#a(n+1) = 2a(n) - 1 
def diagCount(num):
    count = 2*num - 1
    return count

#кладем в переменную dcount количество диагоналей
dcount = diagCount(num)

#объявляем одномерный массив c
c = []

#n и m - индексы элементов в массиве b, начинаем с нулей (с первого элемента)
n = 0
m = 0

#dcount_1 - количество диагоналей до главной (включительно)
#dcount_2 - количество оставшихся диагоналей после главной (не включительно)
dcount_1 = round(dcount/2 - 0.01) + 1
dcount_2 = dcount_1 + 1

#цикл, считывающий элементы в диагоналях до главной (включительно)
#принцип работы:
#если диагональ нечетная (i % 2 != 0), в каждой диагонали индекс n уменьшается, а m увеличивается
#если диагональ четная (i % 2 == 0), то наоборот
#так же есть условие, при котором на первом проходе цикла индекс n = 0, а на всех дальнейших n = i - 1, то есть возрастает
#и если диагональ четная, то возрастает m (m = i -1), но без учета первого элемента, т.к. проход всегда начинается с нечетной диагонали
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

#сбрасываем m до 1
#это позволяет правильно осуществить проход, если первая диагональ после главной нечетная
m = 1

#цикл, считывающий элементы в диагоналях после главной (не включительно)
#тоже есть условия четности и нечетности, принцип работы схож с тем, что применяется в предыдущем цикле
#в конце условия четности увеличиваем m на 2
#это потому, что на каждой следующей нечетной диагонали индекс m ВСЕГДА увеличивается на 2
#видно, если на бумаге подробно расписать все шаги прохода змейкой с индексами
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

#записываем наш одномерный массив в файл
with open("output.txt", 'w') as f:
    for item in c:
        f.write("%s\n" % str(item))

#я в шоке с того, что это действительно работает







        









    
