from Logger import *

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