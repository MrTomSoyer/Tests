def check_age(age: int):

    if age >= 18:
        result = 'Доступ разрешён'
    else:
        result = 'Доступ запрещён'

    return result

if __name__ == '__main__':
    # Этот код менять не нужно
    auth = check_age(10)
    assert auth == 'Доступ запрещён', f'Получен неверный ответ: {auth}'
    print('Возраст 10:', auth)

    auth = check_age(20)
    assert auth == 'Доступ разрешён',  f'Получен неверный ответ: {auth}'
    print('Возраст 20:', auth)
