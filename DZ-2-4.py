#Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

n = int(input('Введите длину списка: '))
list_count = []
for i in range(n):
    list_count.append(random.randint(-n, n))

with open('file.txt', 'w', encoding='UTF-8') as count_txt:
    for i in list_count:
        count_txt.write(str(i) + '\n')

with open('file.txt') as f:
    d = f.read().split()
print(d)
print(eval('*'.join(map(str, d))))