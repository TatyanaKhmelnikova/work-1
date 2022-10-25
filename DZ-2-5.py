# реализуйте алгоритом перемешивания списка


from random import random

data = [i for i in input('Введите данные: ')]
print(data)
print(sorted(data, key=lambda i: random()))
