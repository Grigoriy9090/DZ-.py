from data_create import *


def input_contact():# сохранить в переменную 
    name = name_data()
    patronymic = patronymic_data()
    surname = surname_data()
    phone_number = phone_number_data()
    address = address_data()
    return f'{name} {patronymic} {surname} \n {phone_number} \n {address}'

def add_contact():# записать в файл
    contact = input_contact()
    with open('Phonebook.txt', 'a', encoding= 'utf-8') as data: # - второй аргумент - это кодировка для нормального распознавания русских букв,
# если в файле буквы только английские, то кодировку указывать не нужно
        data.write(contact + '\n\n')

def read_file():
    with open('Phonebook.txt', 'r', encoding= 'utf-8') as data: # оператор записи файла
        return data.read()

def print_contacts():
    data = read_file()
    print()
    print(data)

def search_contact():
    print('Варианты поиска:\n'
        '1.По имени\n'
        '2.По фамилии\n'
        '3.По отчеству\n'
        '4.По номеру телефона\n'
        '5.По адресу\n')
    choice = input('Выберите вариант поиска: ')
    i_choice = int(choice) - 1
    search = input('Введите данные для поиска: ')
    data_str = read_file().rstrip()# убирает лишние элементы \n\n
    if search not in data_str:
        print('Нет такого')
    else:
        # print([data_str])
        data_lst = data_str.split('\n\n')
        # print(data_lst)
        for contact_str in data_lst:
            contact_lst = contact_str.replace('\n', ' ').split()
            if search in contact_lst[i_choice]:
                # print(contact_lst)
                print(contact_str)
                print()

# # первая мысль
# def update_contact():# функция для изменения данных контакта
# # преобразуем строку контакта в список и убираем переносы строк
#     contact_lst = contact_str.replace('\n', ' ').split()
#     # запрашиваем новые данные для каждого поля контакта
#     name = name_data()
#     patronymic = patronymic_data()
#     surname = surname_data()
#     phone_number = phone_number_data()
#     address = address_data()
#     # заменяем старые данные на новые в списке
#     contact_lst[0] = name
#     contact_lst[1] = patronymic
#     contact_lst[2] = surname
#     contact_lst[3] = phone_number
#     contact_lst[4] = address
#     return f'{name} {patronymic} {surname} \n {phone_number} \n {address}' == contact_lst
# # преобразуем список обратно в строку и добавляем переносы строк
# updated_contact = '\n'.join(contact_lst)
# contact_str = contact_lst.replace('\n', ' ').split()
# # открываем файл для записи и заменяем старую строку контакта на новую
# with open('Phonebook.txt', 'r+', encoding='utf-8') as data:
#     data_str = data.read()
#     updated_data = data_str.replace(contact_lst, updated_contact)
#     data.seek(0) # перемещаем указатель в начало файла
#     data.write(updated_data) # записываем обновленные данные в файл
#     data.truncate() # обрезаем файл до текущей позиции указателя, чтобы удалить старые данные

    
             
# Вторая мысль
def update_contact():
    print('Введите контакт который хотите найти и изменить: \n')
    print('Варианты поиска:\n'
        '1.По имени\n'
        '2.По фамилии\n'
        '3.По отчеству\n'
        '4.По номеру телефона\n'
        '5.По адресу\n')
    choice = input('Выберите вариант поиска: ')
    i_choice = int(choice) - 1
    search = input('Введите данные для поиска: ')
    data_str = read_file().rstrip()# убирает лишние элементы \n\n
    if search not in data_str:
        print('Нет такого')
    else:
        print('Введите новую запись контакта')
        new_contact = input_contact()
    # открываем файл для записи и заменяем старую строку контакта на новую
    with open('Phonebook.txt', 'w', encoding='utf-8') as data2:
        new_contact = new_contact.read()
        new_contact = data_str.replace(new_contact)
        # data2.write(data = read_file()) # записываем обновленные данные в файл
        # data2.truncate() # обрезаем файл до текущей позиции указателя, чтобы удалить старые данные

def deleting_contact():
    print('Введите контакт который хотите удалить: ')
    contact = input_contact()
    contact_str = read_file()
    if contact in contact_str:
       with open('Phonebook.txt', 'w', encoding='utf-8') as data2:
           contact_str = contact_str.replace(contact + '\n\n', '' )
           data2 = write(data2)
    else:
        print('Такого контакта нет') 