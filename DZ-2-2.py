#Напишите программу, которая принимает на вход число N и
# выдает набор произведений чисел от 1 до N.

n = int(input())
factorial = 1
b = []
for i in range(1, n + 1):
    factorial = factorial * i
    b = factorial
    print(b)


