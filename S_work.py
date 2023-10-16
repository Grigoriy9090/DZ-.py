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

# import random


# num = random.randint(5, 10) # вариант 2
# kg = random.randint(1, 15)
# min_num_kg = kg
# max_num_kg = kg
# for _ in range(num - 1):
#     kg = random.randint(1, 15)
#     if kg < min_num_kg:  
#         min_num_kg = kg 
#     elif kg > max_num_kg:
#         max_num_kg = kg
# print(min_num_kg)
# print(max_num_kg)

# Дан список чисел. Определите, сколько в нем встречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4]

# Output: 6

# Примечание: Пользователь может вводить значения списка или список задан изначально.

# test_1 = [1, 1, 2, 0, -1, 3, 4, 4]
# set_1 = set(test_1) # через функцию сет ищет в списке уникальные значения
# print(test_1)
# print(set_1)
# print(len(set_1))

# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть 
# всю последовательность (сдвиг - циклический) на K элементов вправо,  
# K – положительное число.

# Input:   [1, 2, 3, 4, 5] k = 3

# Output:  [3, 4, 5, 1, 2]

# Примечание: Пользователь может вводить значения списка или список задан изначально.

# k = int(input('Введите число сдвига: K '))
# list_1 = [1, 2, 3, 4, 5]
# print(list_1[k-1:] + list_1[:k-1]) # при помощи срезов можно решить эту задачу

# k = int(input('Введите число сдвига K: ')) # второй способ как в лекции
# list_1 = [1, 2, 3, 4, 5]
# for i in range(k):
#     list_1.insert(0,list_1.pop()) # функция инсерт добавляет на указанное место элемент, 
# # а функция поп удаляет элемент
# print(list_1)

# Напишите программу для печати всех уникальных значений в словаре. 

# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, 
# {"V":"S009"}, {"VIII":"S007"}] 

# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# Примечание: Список словарей задан изначально. Пользователь его не вводит

# dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
# new_set = set()
# for dict_i in dictionary:
#     for value in dict_i.values(): # (велью) значение, мы находим через значение
#         new_set.add(value) # эдд (эддит) добавляет элемент
# print(new_set) # сет ищет уникальные значения в библиотеке

#  втрой способ решения задачи подсказки как обращаться

# my_dict = {"V": 23, "VX": 56, "VI": 90, "VI": 34, "VII": 123}

#  Разяснение от преподавателя 

# print(my_dict)
# print(my_dict.keys())
# print(len(my_dict.keys()))
# print(list(my_dict.keys())[2])
# print(my_dict.values())
# print(sum(my_dict.values()))
# print(my_dict.items())

# print('\n')
# for key in my_dict:
#     print(key, end=' ')

# print('\n')
# for key in my_dict.keys():
#     print(key, end=' ')
    
# print('\n')
# for value in my_dict.values():
#     print(value, end=' ')

# print('\n')
# for items in my_dict.items():
#     print(items, end=' ')
    

# print('\n')   
# a, b, *c = (123, 456, 567, 678, 789) 
# print(a)
# print(b)
# print(c)

# print('\n')
# for key, value in my_dict.items():
#     print(key, value, sep=' -||- ', end=' ')
    
# print('\n')    
# print(*'Python', 'my', 'world', sep='-', end='\n')
# print(*my_dict, sep='\n')

# my_dict = {"V": 23, "VX": 56, "VI": 90, "VI": 34, "VII": 123}

# print(my_dict)

# print(my_dict['V'])

# my_dict['V'] = 9999
# print(my_dict)

# my_dict['V'] += 1
# print(my_dict)

# my_dict['XXX'] = my_dict['V'] 
# del my_dict['V'] 
# print(my_dict)

# my_dict['VVV'] = my_dict.pop('VII') 
# print(my_dict)

# ВТОРОЙ способ решения задачи!
# dictionary = [{"V": "S001", "VV": "S00123"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
# new_set = set()
# for dict_i in dictionary:
#     new_set.update(dict_i.values())
# print(new_set)

# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество 
# элементов массива, больших предыдущего (элемента с предыдущим номером) 

# Input: [0, -1, 5, 2, 3]

# Output: 2 

# Пояснение: (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения списка или список задан изначально

# import random

# rnd = random.randint(5, 10)
# print(rnd)
# list_1 = []
# for _ in range(rnd):
#     list_1.append(random.randint(-50, 101))
# # list_2 = [random.randint(-50, 101) for _ in range(rnd)]
# print(list_1)

# count = 0
# for i in range(len(list_1) - 1):
#     if list_1[i] < list_1[i + 1]:
#         count += 1
# print(count)

# Задача 25. Решение в группах
# Напишите программу, которая принимает на вход строку, и отслеживает, 
# сколько раз каждый символ уже встречался. Количество повторов добавляется 
# к символам с помощью постфикса формата n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию .split() a a a b c a a d c d d

# Мое решение
# s = "a a a b c a a d c d d" # считываем строку
# words = s.split() # разбиваем строку на слова

# count = {} # создаем пустой словарь для подсчета количества вхождений символов

# for word in words: # проходим по всем словам
#     for i in range(len(word)): # проходим по всем символам в слове
#         char = word[i] # получаем текущий символ
#         if char not in count: # если символ еще не встречался
#             count[char] = 1 # добавляем его в словарь с начальным значением 1
#         else: # если символ уже встречался
#             count[char] += 1 # увеличиваем его значение на 1
#         word = word[:i+1] + '_' + str(count[char]) # добавляем постфикс к символу
#     print(word, end=' ') # выводим слово с добавленными постфиксами

#  Решение в группе:

# list1 = "a a a b c a a d c d d".split()
# dict1 = {}

# for el in list1:
#     if el in dict1:
#         dict1[el] += 1
#         print(f'{el}_{dict1[el]}', end=" ")
#     else:
#         dict1[el] = 0
#         print(el, end=" ")

# Решение в группе 2:

# list1 = "a a a b c a a d c d d".split()
# list1.reverse()
# print(list1)
# for i in range(len(list1)):
#     list1[i] = f'{list1[i]}_{list1.count(list1[i]) - 1}'
# list1.reverse()
# list1 = " ".join(list1)
# list1 = list1.replace("_0", "")
# print(list1)




# Задача No27. Решение в группах
# Пользователь вводит текст(строка). Словом считается последовательность 
# непробельных символов идущих подряд, слова разделены одним или большим числом пробелов. 
# Определите, сколько различных слов содержится в этом тексте.

# Input: She sells sea shells on the sea shore The shells that she sells are 
# sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that 
# the shells are sea shore shells

# Output: 13

# text = "She sells sea shells on the sea shore The shells that she sells are \
# sea shells I'm sure So if she sells sea shells on the sea shore \
# I'm sure that the shells are sea shore shells ".upper() # считываем строку и добавляем функцию поднять все буквы до заглавных

# words = text.split() #  разбиваем строку на слова
# unique_words = set(words) # создаем множество уникальных слов
# count = len(unique_words) # считаем количество уникальных слов
# print(count) # выводим количество уникальных слов

# Задача No 29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит следующую задачу: 
# “Задана последовательность неотрицательных целых чисел. Требуется определить 
# значение наибольшего элемента последовательности, которая завершается первым 
# встретившимся нулем (число 0 не входит в последовательность)”. 
# Однако 2 друга оказались не такими смышлеными. 
# Никто из ребят не смог до конца сделать это задание. 
# Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. 
# За помощью товарищи обратились к Вам, студентам.

# # Примечание: Программные коды на следующих слайдах

# Ваня:

# n = int(input())
# max_number = 1000
# while n != 0:
#    n = int(input())
#    if max_number > n:
#        max_number = n
# print(max_number)

# Петя:

# n = int(input())
# max_number = -1
# while n < 0:
#    n = int(input())
#    if max_number < n:
#        n = max_number
# print(n)
 

# Решение в группе: 

# n = int(input())
# max_number = n  # 1) n
# while n != 0:
#     n = int(input())
#     if max_number < n:  # 2) < n
#         max_number = n
# print(max_number)


# # Петя:

# n = int(input())
# max_number = n  # 1) -1 > n
# while n != 0:  # 2) != 0
#     n = int(input())
#     if max_number < n:
#         max_number = n  # 3) присваивание наоборот
# print(max_number)  # 3) n > max_number

# Задача No31. Решение в группах
# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи
# Input: 7 Output: 21
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181

# Задача No33. Решение в группах
# Хакер Василий получил доступ к классному журналу и хочет заменить все 
# свои минимальные оценки на максимальные. Напишите программу, которая заменяет 
# оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4 Output: 1 3 3 3 1

# Не работает 
# grades = input('Введите неудовлетворительные оценки: ').split()[1:]
# max_grade = max(grades)
# min_grade = min(grades)
# for i in range(len(grades)):
#     if grades[i] == max_grade:
#         grades[i] = min_grade
#     elif grades[i] == min_grade:
#         grades[i] = max_grade
# print(' '.join(grades))

# # import random
# from random import randint
# # from random import *
# import time

# start = time.time()
# # def invertMaxMarks(marks):
# #     max_mark, min_mark = max(marks), min(marks)
# #     for i in range(len(marks)):
# #         if marks[i] == max_mark:
# #             marks[i] = min_mark
# #     return marks

# def invertMaxMarks(marks):
#     max_mark = min_mark = marks[0]
#     index_max_mark = [0]
#     for i in range(len(marks)):
#         if marks[i] > max_mark:
#             max_mark = marks[i]
#             index_max_mark = [i]
#         elif max_mark == marks[i]:
#             index_max_mark.append(i)
#         if marks[i] < min_mark:
#             min_mark = marks[i]
#     for i in index_max_mark:
#         marks[i] = min_mark
#     return marks

# n = randint(5, 10)
# marks = [randint(1, 5) for _ in range(n)]
# print(marks)
# for i in range(100000):
#     invertMaxMarks(marks)
# print(invertMaxMarks(marks))
# end = time.time()
# print(end - start)

#  Задача 35 
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

# Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)


# Input: 5

# Output: yes

# Моё решение

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5)+1):
#         if num % i == 0:
#             return False
#     return True

# num = int(input('Введите простое число: '))
# if is_prime(num):
#     print("Да")
# else:
#     print("Нет")



# Задача 37 
# Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы 
# (даже для ввода и вывода).
# Input: 2 -> 3 4 Output: 4 3

# Моё решение 

# num = int(input('Введите натуральное число: '))
# if num == 1:
#     print(input('Введите последовательность из натуральных чисел: '))
# else:
#     print(input().split()[::-1])

# Другое решешин

# def num_revers(nat_num):
#     if nat_num == 0:
#         return ''
#     k = input('Укажите очередное число: ')
#     return num_revers(nat_num -1) + k + ' '

# num = int(input('Введите натуральное число: '))
# print(num_revers(num).strip())


# Задача No39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы первого массива 
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. 
# Пользователь вводит число N - количество элементов в первом массиве, 
# затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. 
# Затем элементы второго массива

# rom random import randint


# def create_list(n):
#     new_list = [randint(0, 9) for _ in range(n)]
#     return new_list


# def get_diff_elements(list1, list2):
#     list4 = [el for el in list1 if el not in list2]# лист комприхендшен

#     return list4

# n = randint(5, 9)
# m = randint(5, 9)
# list1 = create_list(n)
# list2 = create_list(m)
# print(n, ' -> ', list1)
# print(m, ' -> ', list2)
# print(get_diff_elements(list1,list2))
# 
# list3 = []
# for el in list1:
#     if el not in list2:
#         list3.append(el)
# print(list3)
# 
# list4 = [el for el in list1 if el not in list2]
# 
# list5 = [el if el not in list2 else 0 for el in list1]

# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5               5
# 1 2 3 4 5       1 5 1 5 1
# Вывод: Вывод:
# 0 2
# (каждое число вводится с новой строки)

# from random import randint

# def create_list(n):
#     new_list = [randint(0, 9) for _ in range(n)]
#     return new_list

# def count_elements(list1):
#     count = 0
#     for i in range(1, len(list1) - 1):
#         if list1[i - 1] < list1[i] > list1[i + 1]:
#             count += 1
#     return count


# n = randint(5, 10)
# list1 = create_list(n)
# print(n, ' -> ', list1)
# print(count_elements(list1))

# Задачи 43 (пользовательский ввод можно заменить на рандомный)
# Пользователь вводит  размер массива – N
# и элементы массива (целые числа). 
# нужно посчитать сколько повторений у каждого числа
# посчитанные числа можно посчитать повторно в паре с другими числами

# Ввод:			Вывод:
# 1 2 3 2 3 2			4


# Мое решение
# import random

# n = int(input("Введите размер массива: "))
# arr = []
# for i in range(n):
#     arr.append(random.randint(1, 10)) # генерируем случайные числа от 1 до 10

# count_dict = {}
# for num in arr:
#     if num not in count_dict:
#         count_dict[num] = arr.count(num)

# total_count = 0
# for count in count_dict.values():
#     total_count += count * (count - 1) // 2 # формула для подсчета количества пар

# print("Количество пар чисел с повторениями:", total_count)

# Решение в группе
# list1 = [1, 2, 3, 2, 3, 2, 2]
# print(list1)

# count = 0

# for i in range(len(list1) - 1):
#     for j in range(i + 1, len(list1)):
#         if list1[i] == list1[j]:
#             count += 1
# print(count)

# Решение преподавателя
# list1 = [1, 2, 3, 2, 3, 2, 2]
# print(list1)

# count = 0

# for i in range(len(list1) - 1):
#     for j in range(i + 1, len(list1)):
#         if list1[i] == list1[j]:
#             count += 1
# print('результат первого решения: ', count)

# count_list = []            
# for i in range(len(list1) - 1):
#     for j in range(i + 1, len(list1)):
#         if list1[i] == list1[j]:
#             count_list.append(1)
# print('результат второго решения: ', sum(count_list))

# res = sum([1  for i in range(len(list1) - 1) for j in range(i + 1, len(list1))  if list1[i] == list1[j]])
# print('результат третьего решения: ', res)

# Задача 45 (пользовательский ввод можно заменить на рандомный)
# Пользователь вводит  натуральное число  – k
# В диапазоне от 0 до k нужно вывести все пары чисел N и M, в которых сумма делителей N равняется M, 
# а сумма делителей M равняется N (число само на себя делить нельзя)
# Пары необходимо выводить по одной паре в строке, разделяя числа пробелами. Каждая пара выводится только один раз, без повторов. 

# Пример: Возьмём 2 числа 220 и 284. Найдём их делители 
# Делители 220 – (1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110)
# 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110  = 284
# Делители 284 – (1, 2, 4, 71, 142 )
# 1 + 2 + 4 + 71 + 142 = 220

# def find_sum_of_div(n):
#     sum_n = 1
#     for div in range(2, int(n ** 0.5) + 1):
#         if n % div == 0:
#             if div == n / div:
#                 sum_n += div
#             else:
#                 sum_n += div + n // div
#     return sum_n

# def find_friendly_pairs(k_num):
#     list_res = []
#     for first_num in range(2, k_num + 1):
#         second_num = find_sum_of_div(first_num)
#         if first_num == find_sum_of_div(second_num) and first_num > second_num:
#             list_res.append((first_num, second_num))
#     return list_res

# k = input('Введите число k > 1: ')
# while not (k.isdigit() and int(k) > 1):
#     print('Некорректный ввод')
#     k = input('Введите число k > 1: ')

# k = int(k)
# print(*find_friendly_pairs(k), sep='\n')

# Задача No47. Решение в группах

transformation = lambda el: el * 2
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
print(transormed_values)
if values == transormed_values:
         print('ok')
else:
         print('fail')

# - В переменную transformation нужно прописать такую функцию, что бы в переменной transformed_values 
# получилась копия списка values

# Задача  49 - Дан список размеров(длина, ширина) эллипсов 
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# Напишите функцию find_farthest_orbit(list_of_orbits), которая находит площадь самого большого 
# эллипса и возвращает кортеж с его размерами.
# Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b – длины и ширина осей эллипса
# -   Площадь кругов учитывать не нужно, т.е если у эллипса a == b, то это круг.
# При решении задачи используйте списочные выражения.
# Гарантируется, что самый большой эллипс всего один.

# def find_farthest_orbit(list_of_orbits):
#     sizes = list(filter(lambda item : item[0] != item[1], list_of_orbits))
#     areas = list(map(lambda item : 3.14 * item[0] * item[1], sizes))
#     maximum = areas[0]
#     imax = 0
#     for i, area in enumerate(areas[1:], 1):
#         if area > maximum:
#             maximum = area
#             imax = i
#         # maximum = max(maximum, area)
#     return sizes[imax]

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farthest_orbit(orbits))

# def same_by(characteristic, objects):  
#     for i in range(1, len(objects)):
#         print(f'индекс i - 1 = {i - 1}')
#         print(f'элемент i - 1= {objects[i - 1]}')
#         print(f'Характеристика i - 1= {characteristic(objects[i - 1])}')
#         print(f'индекс i  = {i}')
#         print(f'элемент i = {objects[i]}')
#         print(f'Характеристика i= {characteristic(objects[i])}')
#         print()
#         if characteristic(objects[i - 1]) != characteristic(objects[i]):
#             return False
#     return True
    


# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):  
#     print('same')
# else:
#     print('different')

