# Задайте список из n чисел последовательности
# $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


n = int(input('Введите число; '))

val = []
summa = 0

for e in range(1, n + 1):
    val = round((1 + (1/e))**e, 3)
    summa += val
print(summa)









