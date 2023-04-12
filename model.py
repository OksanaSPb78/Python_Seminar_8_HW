# 1. переменная в которой лежит наш словарь
phone_book = []
# копия телефонной книги
original_book = []
PATH = 'phone_book.txt'

# 1. открытие файла
def open_file():
    # 10. копия телеф.книги
    global original_book
# баг- дублирование контактов при запуске убираем
    phone_book.clear()
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        # отрезаем всё лишнее от строки вначале и в конце
        contact = contact.strip().split(';')
        # 1. добавление списка в телефонную книгу
        phone_book.append({'name': contact[0],
                           'phone': contact[1],
                           'comment': contact[2]})
#     original_book = phone_book.copy()

# 9. сохранение изменений
def save_file() -> None:
    # 10.
    global original_book
    save_book = []
    for contact in phone_book:
# из словаря нужно сделать строки (склеиваем)
        save_book.append(';'.join(contact.values()))
    data = '\n'.join(save_book)
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write(data)
        # 10. копия телефонной книги
    original_book = phone_book.copy()


def get_phone_book() -> list[dict]:
    return phone_book

# 4.создаем функцию добавления контакта
def add_contact(new_contact: dict[str, str]) -> None:
    phone_book.append(new_contact)

# 5.создаем функцию поиска контакта
def find_contact(word: str) -> list[dict[str, str]]:
    result = []
    for contact in phone_book:
        for field in contact.values():
            print(field)
            if word in field:
                result.append(contact)
                break
    return result

#6. функция изменения контакта
def edit_contact(edited_contact: tuple[int, dict[str, str]]) -> None:
    index, contact = edited_contact
    original_contact = phone_book.pop(index - 1)
    contact = {'name': contact.get('name') if contact.get('name') else original_contact.get('name'),
               'phone': contact.get('phone') if contact.get('phone') else original_contact.get('phone'),
               'comment': contact.get('comment') if contact.get('comment') else original_contact.get('comment')}
    phone_book.insert(index - 1, contact)

# 7. функция удаление контакта
def remove_contact(index: int) -> str:
    deleted_element = phone_book.pop(index - 1)
    return deleted_element.get('name')