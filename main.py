class Err(Exception):
    def __init__(self, message, etra_info):
        self.message = message
        self.etra_info = etra_info


def f(a, b):
    if b == 0:
        raise Err('Деление на нуль невозможно', {'a': a, 'b': b})
    return a / b


try:
    result = f(4, int(input()))
    print(result)
except Err as e:
    print(f'Ошибка: {e.message}')
    print(f'Инфо: {e.etra_info}')
except ValueError:
    print(f'Ошибка: Не числовой тип')
    print(f'Инфо: Введите цифры а не букву')
finally:
    print('Деление удалось!')
