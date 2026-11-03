# geometric_lib

## Общее описание решения

**Технологии:** Python3 (модуль `math`), bash, unittest

***Структура проекта:***
```text
.
├── circle.py
├── docs
│   └── README.md
├── rectangle.py
├── square.py
├── tests
│   ├── __init__.py
│   ├── test_circle.py
│   ├── test_rectangle.py
│   ├── test_square.py
│   └── test_triangle.py
├── triangle.py
├── u1.txt
├── u2.txt
└── u3.txt
```

**Использование:** импортируйте нужные функции в свой скрипт:
```python 
from circle import area as circle_area, perimeter as circle_perimeter
from square import area as square_area, perimeter as square_perimeter
from rectangle import area as rectangle_area, perimetr as rectangle_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter
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

- **Параметры:** `a` (int) — длина стороны квадрата (число > 0)
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

### rectangle.py

#### `area(a, b)`
Вычисляет площадь прямоугольника. Формула: `S = a · b`.

- **Параметры:** `a`, `b` (int) — длины сторон прямоугольника
- **Возвращает (int):** площадь прямоугольника
- **Пример вызова:**
```python
from rectangle import area
area(3, 4)  # 12
```

#### `perimetr(a, b)`
Вычисляет периметр прямоугольника. Формула: `P = 2 · (a + b)`. 

- **Параметры:** `a`, `b` (int) — длины сторон прямоугольника
- **Возвращает (int):** периметр прямоугольника
- **Пример вызова:**
```python
from rectangle import perimetr
perimetr(3, 4)  # 14
```

### triangle.py

#### `area(a, b, c)`
Вычисляет площадь треугольника. 

- **Параметры:** `a`, `b`, `c` (int) — длины сторон треугольника
- **Возвращает (float):** площадь треугольника
- **Пример вызова:**
```python
from triangle import area
area(3, 4, 5)  # 6.0
```

#### `perimeter(a, b, c)`
Вычисляет периметр треугольника. Формула: `P = a + b + c`.

- **Параметры:** `a`, `b`, `c` (int) — длины сторон треугольника
- **Возвращает (int):** периметр треугольника
- **Пример вызова:**
```python
from triangle import perimeter
perimeter(3, 4, 5)  # 12
```

---

## История изменения проекта

| Хэш коммита | Описание изменения |
| ----------- | ------------------ |
| edc847f     | Add files and tests, change README.md |
| 7e410e4     | Updated README.md |
| 3e8f1d0     | Change circle.py square.py files |
| d1048cd     | add u1.txt u3.txt |
| d078c8d     | L-03: Docs added |
| 8ba9aeb     | L-03: Circle and square added |

---

## Запуск тестов

В проекте написаны unit-тесты с использованием стандартной библиотеки `unittest`. Тесты покрывают все 4 фигуры (круг, квадрат, прямоугольник, треугольник), включая проверки граничных значений и поиск дефектов.

Для запуска всех тестов из корневой папки проекта выполните:

```bash
python -m unittest discover -v
```


