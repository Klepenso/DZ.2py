# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint
n = int(input('Введите число N: '))
def list(n):
    list = []
    for i in range(n):
        list.append(randint(-n, n))
    return list

numbers = list(n)
print(numbers)
x = open('file.txt')
result = numbers[int(x.readline())]*numbers[int(x.readline(2))]
print(result)