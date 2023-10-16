def change_contact():# функция для изменения контакта
    print('Варианты поиска контакта для изменения данных:\n'
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
        # преобразуем данные в список для удобства работы
        data_lst = data_str.split('\n\n')
        # проходимся по каждому контакту в списке
        for contact_str in data_lst:
            # разделяем данные контакта на отдельные элементы и убираем переносы строк
            contact_lst = contact_str.replace('\n', ' ').split()
            # если введенные данные совпадают с данными контакта, то запускаем функцию для изменения данных
            if search in contact_lst[i_choice]:
                update_contact(contact_str)
                break # останавливаем цикл после изменения первого найденного контакта
        else:
            # если цикл завершился без выполнения break, то выводим сообщение об ошибке
            print('Нет такого')



def user_interface():# создать интерфейс
    with open('Phonebook.txt', 'a', encoding='utf-8'): # создали принудительно нулевой фаил если его нету 
        pass
    cmd = None
    while cmd !='6':
        print('Меню:\n'
        '1. Запись контакта\n'
        '2. Вывести данные на экран\n'
        '3. Поиск контакта\n'
        '4. Изменение данных контакта\n'
        '5. Поиск контакта для удаления данных\n'
        '6. Выход из программы')
        cmd = input('Введите номер операции: ')
        while cmd not in ('1', '2', '3', '4'):
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
                change_contact()
            case '5':
                deleting_data()
            case '6':
                print('Пока, пока!')
             
user_interface()