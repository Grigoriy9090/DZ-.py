# Домашняя задача 2: Найдите сумму цифр трехзначного числа.
# Пример: 123 -> 6 (1 + 2 + 3) 
# 100 -> 1 (1 + 0 + 0)

# Решение:
# num = int(input("Введите трехзначное число: "))
# summa = num // 100 + num // 10 % 10 + num % 10
# print("Сумма цифр трехзначного числа: ", sum)

# num = input("Введите трехзначное число: ")
# summa = int(num[0]) + int(num[1]) + int(num[2])
# print("Сумма цифр трехзначного числа: ", summa)

# Домашняя задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# Пример:
# 6 -> 1 4 1
# 24 -> 4 16 4 
# 60 -> 10 40 10

# Решение:

# s = int(input("Введите количество сделанных журавликов: "))
# ps = s // 6
# k = ps * 4
# print("Петя сделал", ps, "журавликов")
# print("Катя сделал", k, "журавликов")
# print("Сережа сделал", ps, "журавликов")

# Домашняя задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

# Пример ответа:  
# 385916 -> yes
# 123456 -> no

# Решение:

# num = input("Введите номер билета: ")
# if len(num) != 6 or not num.isdigit(): # почему когда ставишь пробел ! = програма просит :???
#     print("Некоректный номер билета")
# else: digit = [int(d) for d in num]
# sum1 = sum(digit[:3]) #Что означет : спереди или сзади???
# sum2 = sum(digit[3:len(num)])
# if sum1 == sum2:
#     print("Билет счастливый")
# else:
#     print("Билет несчастливый")

# num = input("Введите номер билета: ")
# if len(num) != 6 or not num.isdigit():
#     print("Некоректный номер билета")
# num1 = int(num[:3])
# sum1 = num1 // 100 + num1 // 10 % 10 + num1 % 10
# num2 = int(num[3:])
# sum2 = num2 // 100 + num2 // 10 % 10 + num2 % 10
# if sum1 == sum2:
#     print("Билет счастливый")
# else:
#     print("Билет несчастливый")

# Домашняя задача 8: Требуется определить, можно ли от шоколадки размером n×m 
# долек отломить k долек, если разрешается сделать один разлом 
# по прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).

# Пример проверки: 
# 3 2 4 -> yes 
# 3 2 1 -> no

# Решение: 
# n = int(input('Введите длину шоколадку: '))
# m = int(input('Введите ширину шоколадку: '))
# k = int(input('Введите как вы хотите разломить шоколадку: '))
# if k < n * m and ((k % n == 0) or (k % m == 0)):
#     print('YES')
# else:
#     print('NO')

# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N 
# (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# Input:       5
# Output:    120

# n = input("Введите целое число N: ")

# while not n.isdigit():
#     print("Вы ввели не число")
#     n = input("Введите целое число N: ")

# n = int(n)
# fact = 1

# while n > 1:
#     fact *= n
#     n -= 1

# print(fact)

# n = input("Введите целое число N: ")

# while not n.isdigit():
#     print("Вы ввели не число")
#     n = input("Введите целое число N: ")

# n = int(n)
# mult = 1
# fact = 1

# while mult <= n:
#     fact *= mult
#     mult += 1
# print(fact)

# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи 
# оно является, то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, 
# выведите число -1.

# Input:     5

# Output:  6

# Ряд чисел Фибоначчи:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 
# 2584, 4181, 6765, 10946, 17711, …

#1 num = input("Ввидите натуральное число")

# while not num.isdigit():
#     print("Вы ввели не число")
#     num = input("Введите целое число: ")
# num = int(num)
# fib1 = 0
# fib2 = 1
# fib = 1
# count = 2
# while fib < num:
#     fib = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib
#     count +=1
# if fib == num:
#     print(count)
# else:
#     print(-1)

# num = input("Ввидите натуральное число: ") #2

# while not num.isdigit():
#     print("Вы ввели не число")
#     num = input("Введите целое число: ")
# num = int(num)
# fib1 = 0
# fib2 = 1
# count = 2
# while fib2 < num:
#     fib2, fib1 = fib1 + fib2, fib2
#     count +=1
# if fib2 == num:
#     print(count)
# else:
#     print(-1)

# Пользователь вводит число N (1 ≤ N ≤ 10). Далее построчно N чисел от -50 до 50. 
# Нужно вывести наибольшее количество идущих подряд положительных чисел.

# Input:    6 -> -20 30 -40 50 10 -10
# Output: 2

# num = input("Enter number: ")
# while num not in "1, 2, 3, 4, 5, 6, 7, 8, 9, 10":
#     print("You entered incorrect number")
#     num = input("Enter correct number: ")
# num = int(num)
# count = 0
# max_count = 0

# for t in range(num):
#     tem = int(input("Enter number -50 - 50: "))
#     if tem > 0:
#         count += 1
#     elif tem <= 0:
#         count = 0
#     if count > max_count:
#         max_count = count    

# print(max_count)

# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# 
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза

# 2) Пользователь вводит одно число N.  Далее идут N чисел, записанных на новой строчке каждое. 
# Вывести максимальное и минимальное (циклы)
# Input:	5 -> 5 1 6 5 9
# Output:	1 9

# import random 


# num = random.randint(5, 10)
# min_num_kg = 1000
# max_num_kg = -1000
# for i in range(num):
#     kg = random.randint(1, 15)
#     if kg < min_num_kg:  
#         min_num_kg = kg 
#     elif kg > max_num_kg:
#         max_num_kg = kg
# print(min_num_kg)
# print(max_num_kg)

import random


num = random.randint(5, 10) # вариант 2
kg = random.randint(1, 15)
min_num_kg = kg
max_num_kg = kg
for _ in range(num - 1):
    kg = random.randint(1, 15)
    if kg < min_num_kg:  
        min_num_kg = kg 
    elif kg > max_num_kg:
        max_num_kg = kg
print(min_num_kg)
print(max_num_kg)


