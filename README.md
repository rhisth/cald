# cald

Скрипт для работы с особенными днями

(P.S. главный файл - `script.py`, `main.py` это тест работы)

## Скрипт

Использование: `script.py <ID дня/флаг> <год>`

Первый аргумент - это ID дня, который есть в папке
`inf`, либо спец. флаг (о них дальше)

Второй аргумент - это год (от 1 до 9999)

## Флаги

Есть несколько флагов, которые влияют на результат вывода:
- `all` — выводит все особенные дни и их дату в году;
- `today` — выводит все сегодняшние особенные дни и их дату в этом году.

## Особенные дни

В программу по умолчанию встроено несколько особенных дней:
- `prog` — День программиста.

Со временем количество будет увеличиваться.

## Формат дней, как их добавлять

У дня есть ID.

День - это папка.

В папке 2 файла:
- `<ID>.inf` — файл с информацией об дне;
- `<ID>.py` — python-файл с функцией, которая возвращает дату.

Чтобы добавить особенный день в программу,
нужно в папке `inf` создать папку с любым
названием. Название этой папки и будет ID.

Дальше создаём файл с информацией.
Например, напишите туда название дня.

После чего делаем python-файл. Вот пример файла, на примере Дня программиста:
```py
from datetime import date

def value(year: int):
    if year % 4 == 0: return date(year, 9, 12)
    return date(year, 9, 13)
```

В файле обязательно должна присутствовать функция `value`,
которая принимает один целочисленный аргумент. Далее в эту
функцию передаётся год, после чего она должна возвратить
объект `datetime.date` (дату).

## Зачем нужно?

Можно использовать для мониторинга сегодняшних праздников
или дней рождений знакомых/друзей.

А вообще фиг знает, постепенно будут добавляться
новые фичи.
