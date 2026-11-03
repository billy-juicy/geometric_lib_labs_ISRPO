# geometric_lib

## Общее описание решения

**Технологии:** Python3 (модуль `math`), bash

***Структура проекта:***
```
.
├── circle.py
├── docs
│   └── README.md
├── square.py
├── u1.txt
├── u2.txt
└── u3.txt
```

**Использование:** импортируйте нужные функции в свой скрипт:
```python 
from circle import area as circle_area, perimeter as circle_perimeter
from square import area as square_area, perimeter as square_perimeter
```

## Описание функций

### circle.py

#### `area(r)`
Вычисляет площадь круга по его радиусу. Формула: `S = π · r²`.

- **Параметры:** `r` (int) — радиус круга (число > 0)
- **Возвращает (float):** площадь круга
- **Пример вызова:**
```python
from circle import area
area(5)  # 78.53981633974483
```

#### `perimeter(r)`
Вычисляет длину окружности (периметр круга) по его радиусу. Формула: `P = 2 · π · r`.

- **Параметры:** `r` (int) — радиус круга (число > 0)
- **Возвращает (float):** длину окружности
- **Пример вызова:**
```python
from circle import perimeter
perimeter(5)  # 31.41592653589793
```

### square.py

#### `area(a)`
Вычисляет площадь квадрата по длине его стороны. Формула: `S = a²`.

- **Параметры:** `a int` — длина стороны квадрата (число > 0)
- **Возвращает (int):** площадь квадрата (int/float)
- **Пример вызова:**
```python
from square import area
area(4)  # 16
```

#### `perimeter(a)`
Вычисляет периметр квадрата по длине его стороны. Формула: `P = 4 · a`.

- **Параметры:** `a` (int) — длина стороны квадрата (число > 0)
- **Возвращает (int):** периметр квадрата (int/float)
- **Пример вызова:**
```python
from square import perimeter
perimeter(4)  # 16
```

---

## История изменения проекта


| Хэш коммита | Описание изменения            |
| ----------- | ----------------------------- |
| 8ba9aeb     | L-03: Circle and square added |
| d078c8d     | L-03: Docs added              |
| d1048cd     | add u1.txt u3.txt             |


## Запуск тестов

Для запуска unit-тестов из корневой папки проекта выполните:

```bash
python -m unittest discover -v
