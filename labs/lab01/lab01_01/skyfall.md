---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.15.1
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

```python
import random
import functools
import timeit
import typing
import matplotlib.pyplot as plt
import numpy as np
```

```python
vec = [random.randint(1, 1000) for _ in range(0, 19 * (10 ** 5))]


def HOPE1(vec: list):
    return sum(vec)

def HOPE2(vec: list):
    return np.prod(vec)

def HOPE3(vec: list, x: float = 14 * 1.5):
    result = 0
    for i in range(len(vec), 0, -1):
        result = result * x + vec[i - 1]
    return result

def HOPE4(vec: list):
    max = vec[0]
    for item in vec[1:]:
        if item > max:
            max = item
    return max

def HOPE5(vec: list[int]) -> float:
    return sum(vec) / len(vec)


def get_usage_time(
        *, number: int = 1, setup: str = 'pass', ndigits: int = 3
) -> typing.Callable:
    def decorator(func: typing.Callable) -> typing.Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> float:
            usage_time = timeit.timeit(
                lambda: func(*args, **kwargs),
                setup=setup,
                number=number,
            )
            return round(usage_time / number, ndigits)

        return wrapper

    return decorator


```

```python
N = 19
func = get_usage_time(ndigits=5, number=5)(HOPE1)
items = [i for i in range(1, len(vec), 1900)]
times = [func(vec[:i]) for i in items]

fig = plt.plot(items, times, 'bo-')
plt.title('Сумма элементов')
ax = plt.gca()
ax.set_xlabel('Число элементов')
ax.set_ylabel('Время, сек')
plt.show()
```

```python
N = 19
func = get_usage_time(ndigits=5, number=5)(HOPE2)
items = [i for i in range(1, len(vec), 1900)]
times = [func(vec[:i]) for i in items]

fig = plt.plot(items, times, 'bo-')
plt.title('Произведение элементов')
ax = plt.gca()
ax.set_xlabel('Число элементов')
ax.set_ylabel('Время, сек')
plt.show()
```

```python
N = 19
func = get_usage_time(ndigits=5, number=5)(HOPE4)
items = [i for i in range(1, len(vec), 1900)]
times = [func(vec[:i]) for i in items]

fig = plt.plot(items, times, 'bo-')
plt.title('Получение максимума простым перебором')
ax = plt.gca()
ax.set_xlabel('Число элементов')
ax.set_ylabel('Время, сек')
plt.show()
```

```python
N = 19
func = get_usage_time(ndigits=5, number=5)(HOPE5)
items = [i for i in range(1, len(vec), 1900)]
times = [func(vec[:i]) for i in items]

fig = plt.plot(items, times, 'bo-')
plt.title('Среднее арифметическое')
ax = plt.gca()
ax.set_xlabel('Число элементов')
ax.set_ylabel('Время, сек')
plt.show()
```

```python
def create_matrix(n: int) -> np.array:
    result = np.array([[random.randint(0, 1000) for j in range(n)] for i in range(n)])
    return result

def matrix_multiplicathion(A, B):
    return np.dot(A, B)

N = 19
count = range(1, 250 * N, 10 * N)
matrix_A = create_matrix(250*N)
matrix_B = create_matrix(250*N)
func = get_usage_time(ndigits=5)(matrix_multiplicathion)
items = [i for i in count]
times = [func(matrix_A[:i, :i], matrix_B[:i, :i]) for i in items]

fig = plt.plot(items, times, 'bo-')
plt.title('Сумма элементов')
ax = plt.gca()
ax.set_xlabel('Число элементов')
ax.set_ylabel('Время, сек')
plt.show()
```

```python
fig = plt.plot(items, times, 'bo-')
plt.title('Произведение матриц')
ax = plt.gca()
ax.set_xlabel('Число элементов')
ax.set_ylabel('Время, сек')
plt.show()
```

```python

```
