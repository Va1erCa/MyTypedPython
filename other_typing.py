# Примеры не отсносящиеся к проекту, о приемах типизации в Python
from typing import Tuple


# (1) Опциональные данные
# def print_hello(name: str ='Tom') -> None:             # не опциональный вариант (значение по умолчанию - 'Tom)
def print_hello(name: str | None = None) -> None :  # опциональный вариант (значение по умолчанию - None)
    print(f"hello, {name}" if name is not None else "hello anon!")


# (2) Контейнеры (указания для какго типа этот контейнер) Iterable, Sequence, Mapping ...
from datetime import datetime
from dataclasses import dataclass


@dataclass
class User :
    name: str
    birthday: datetime


my_users1 = [User(name='Tom', birthday=datetime.fromisoformat("1988-01-01")),
             User(name='Bob', birthday=datetime.fromisoformat("1985-07-29")),
             User(name='Paul', birthday=datetime.fromisoformat("2000-10-10"))
             ]

my_users2 = (User(name='Tom', birthday=datetime.fromisoformat("1988-01-01")),
             User(name='Bob', birthday=datetime.fromisoformat("1985-07-29")),
             User(name='Paul', birthday=datetime.fromisoformat("2000-10-10"))
             )


def get_younger_user(users: list[User]) -> User :  # 1й вариант с явным указанием списка
    if not users :
        raise ValueError("empty users!")
    ordered_users = sorted(users, key=lambda x : x.birthday)
    return ordered_users[0]


from typing import Iterable  # 2й вариант с использованием применимости типаов в sorted


def get_younger_user2(users: Iterable[User]) -> User | None :  # используем тип допустимый в sorted() - Iterable
    if not users :
        return None
    ordered_users = sorted(users, key=lambda x : x.birthday)
    return ordered_users[0]


from typing import Sequence  # 3й вариант с сохранением возможностей индекса


def get_younger_user3(users: Sequence[User]) -> User | None :  # используем тип допустимый в sorted() - Iterable
    if not users :
        return None
    print(users[0])
    ordered_users = sorted(users, key=lambda x : x.birthday)
    return ordered_users[0]


# (3) Кастомный контейнер (основанный на Sequence)
from typing import Sequence


class Users :
    def __init__(self, users: Sequence[User]) :
        self._users = users

    def __getitem__(self, key: int) -> User :
        return self._users[key]

    def __len__(self) -> int :
        return len(self._users)


my_users3 = Users([User(name='Tom', birthday=datetime.fromisoformat("1988-01-01")),
                   User(name='Bob', birthday=datetime.fromisoformat("1985-07-29")),
                   User(name='Paul', birthday=datetime.fromisoformat("2000-10-10"))
                   ])

# (4) Словари / Mapping
some_users_dict: dict[str, User] = {"managers" : User(name='Alex', birthday=datetime.fromisoformat("1990-01-01")),
                                    "drivers" : User(name='Petr', birthday=datetime.fromisoformat("1988-10-23"))
                                    }

from typing import Mapping


def smth(some_users: Mapping[str, User]) -> None :
    for k, v in some_users.items() :
        print(k, v)


# (5) размеры контейнеров
Tuple_three_ints = tuple[int, int, int]  # задаем тип: кортеж целых чисел размера 3

def print_tuple_three(tup: Tuple_three_ints) -> None :
    print(tup[0], tup[1], tup[2])


List_any_ints = list[int, ...]           # задаем тип: список целых чисел любого размера

def print_tuple_any(tup: List_any_ints) -> None :
    for t in tup:
        print(t)


# (6) Дженерики (обобщенные типы)
from typing import TypeVar, Iterable

T = TypeVar("T")                    # Буквально - T - любой тип


def first(iterable: Iterable[T]) -> T | None :  # функция принимает любой итерируемый контейнер типа Т и возвращает тип Т
    for element in iterable :
        return element                  # возврат первого элемента из контейнера


# (7) тип - вызываемый объект (функция)
from typing import Callable                     # тип - Вызываемый объект

def mysum(a: int, b: int) -> int:               # функция
    return a + b

# функция принимающая аргумент типа - вызываемый объект, принимающий два аргумента типа int и возвращающая
# результат типа int
def process_operation(operation: Callable[[int, int], int], a: int, b: int) -> int:
    return operation(a, b)


# (8) указание типа переменной

# при получении значения из нетипизированной функции
def get_user_by_username(name) :                  # функция без типизации
    return name


user: str = get_user_by_username("Иннокентий")    # типизируем переменную получающую значение из не типизированной функции

# типизируем атрибут класса (словарь) который инициализируется пустым значением
class SomeClass():
    def __init__(self):
        self.dict_attribute: dict[str, int] = {}            # типизируем атрибут-словарь

    def __str__(self):
        return '{'+', '.join([f'{k} : {v}' for k,v in self.dict_attribute.items()])+'}'



if __name__ == '__main__' :
    # (1)
    print_hello()       # все Ok
    print_hello('Bob')  # все Ok
    print_hello(125)    # предупреждение от IDE - некорректный тип/ ошибка от mypy

    # (2)
    print(get_younger_user(my_users1))  # все Ok
    # User(birthday=datetime.datetime(1985, 7, 29, 0, 0))

    print(get_younger_user(my_users2))      # код работает, но предупреждение от IDE - некорректный тип / ошибка от mypy
    print(get_younger_user2(my_users2))     # код работает, предупреждений от IDE нет/ mypy - нет
    print(get_younger_user3(my_users2))     # код работает, можно обращаться по индексу

    # (3)
    print('\nИтерируем кастомный контейнер в цикле for:')
    for u in my_users3 :        # кастомный контейнер итерируется но mypy выдет ошибку об отсутствии атрибута __iter__
        print(u)
    print('\nUser с индексом в кастомном контейнере - 2:')
    print(my_users3[2])         # и предоставляет доступ по индексу
    print('\nРазмер кастомного контейнера: ')
    print(len(my_users3))       # переопределенная функция len работает

    # (4)
    print('\nDictionary:')
    print(some_users_dict)
    print('\nMapping:')
    smth(some_users_dict)

    # (5)
    print('\nФункция, получающая контейнер определенного размера:')
    print_tuple_three(('one', 'two', 'three'))  # код работает, но предупреждение от IDE / ошибка от mypy
    print_tuple_three((1, 2, 3, 4))             # код работает, но предупреждение от IDE / ошибка от mypy
    print_tuple_three((1, 2, 3))                # все Ok

    print('\nФункция, получающая контейнер любого размера:')
    print_tuple_any([1, 2, 3])                  # все Ok

    # (6)
    print(first(["one", "two"]))                # "one"
    print(first((100, 200)))                    # 100

    # (7)
    print(process_operation(mysum, 1, 5))       # 6

    # (8)
    print(user)                                 # все Ok

    obj = SomeClass()
    obj.dict_attribute["some_key"] = 123        # все Ok
    print(obj)
    obj.dict_attribute[123] = "some_key"        # код работает, но предупреждение от IDE - некорректный тип / ошибка от mypy
    print(obj)