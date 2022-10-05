documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def some_name():
    number = input('Введите номер документа')
    for data_list in documents:
        if data_list.get('number') == number:
            return data_list.get('name')
    return 'Документа с таким именем нет'


def some_shelf():
    number = input('Введите номер документа')
    for key, value in directories.items():
        if number in value:
            return key
    return 'На полках документа с таким именем нет'


def some_list(documents):
    for doc in documents:
        print(doc['type'], doc['number'], doc['name'])


def add_list():
    shelf = input('Введите номер полки куда положить документ.')
    if shelf in directories.keys():
        type = input('Введите тип документа. ')
        number = input('Введите номер документа. ')
        name = input('Введите имя владельца документа ')
        doc = {'type': type, 'number': number, 'name': name}
        documents.append(doc)
        directories[shelf].append(doc['number'])
        return 'Документ добавлен'
    else:
        print("Номер полки введен не верно")


while True:
    print('Возможные команды: p, s, l, a')
    comand = input('Введите название команды ')
    if comand == 'p':
        print(some_name())
    elif comand == 's':
        print(some_shelf())
    elif comand == 'l':
        print(some_list(documents))
    elif comand == 'a':
        print(add_list())
        break
    else:
        print('Введите команду правильно')
