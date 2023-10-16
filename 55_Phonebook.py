# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество,
# номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# 1. UI (user interface) +
# 2. Создать файл +
# 3. Читать файл +
# 4. Вывод данных на экран: +
#     - считать файл +
#     - сохранить в переменной +
#     - вывести на экран +
# 5. Запись контакта: +
#     - запросить данные +
#     - сохранить в переменную +
#     - записать в файл +
# 6. Поиск контакта:
#     - запросить данные поиска +
#     - сохранить в переменную +
#     - считать файл +
#     - сохранить в переменную +
#     - произвести поиск +

def name_data():# запросить данные 
    return input('Введите имя: ')

def patronymic_data():# запросить данные 
    return input('Введите отчество: ')

def surname_data():# запросить данные 
    return input('Введите фамилию: ')

def phone_number_data():# запросить данные 
    return input('Введите номер телефона: ')

def address_data ():# запросить данные 
    return input('Введите адрес: ')

def input_contact():# сохранить в переменную 
    name = name_data()
    patronymic = patronymic_data()
    surname = surname_data()
    phone_number = phone_number_data()
    address = address_data()
    return f'{name} {patronymic} {surname} \n {phone_number} \n {address}'

def add_contact():# записать в файл
    contact = input_contact()
    with open('Phonebook.txt', 'a', encoding= 'utf-8') as data: # оператор записи файла. utf-8' что это?
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
    

def user_interface():# создать интерфейс
    with open('Phonebook.txt', 'a', encoding= 'utf-8'): # создали принудительно нулевой фаил если его нету 
        pass
    cmd = None
    while cmd !='6':
        print('Меню:\n'
        '1. Запись контакта\n'
        '2. Вывести данные на экран\n'
        '3. Поиск контакта\n'
        '4. Поиск контакта для изменения данных\n'
        '5. Поиск контакта для удаления данных\n'
        '6. Выход из программы')
        cmd = input('Введите номер операции: ')
        while cmd not in ('1', '2', '3', '4', '5', '6'):
            print('Некорректный ввод')
            cmd = input('Введите номер операции: ')
        match cmd:
            case '1':
                add_contact()
            case '2':
                print_contacts()
            case '3':
                search_contact()
            case '4':
                update_contact()
            case '5':
                deleting_contact()
            case '6':
                print('Пока, пока!')

user_interface()
