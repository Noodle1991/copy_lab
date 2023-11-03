import random
import functools
import timeit
import typing
import matplotlib.pyplot as plt
import numpy as np

vec = [random.randint(1, 1000) for _ in range(0, 19 * (10 ** 5))]


def HOPE1(vec: list):
    return sum(vec)


def HOPE2(vec: list):
    return np.prod(vec)





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


N = 19
func = get_usage_time(ndigits=5, number=5)(HOPE2)
items = [i for i in range(1, len(vec), 1900)]
times = [func(vec[:i]) for i in items]

fig = plt.plot(items, times, 'bo-')
plt.title('Сумма элементов')
ax = plt.gca()
ax.set_xlabel('Число элементов')
ax.set_ylabel('Время, сек')
plt.show()



def create_matrix(n: int) -> np.array:
    result = np.array([[random.randint(0, 1000) for j in range(n)] for i in range(n)])
    return result

def matrix_multiplicathion(A, B):
    return np.dot(A, B)

N = 19
count = range(1, 250 * N, 10 * N)
times = [0.0] * 25
matrix_A = create_matrix(250*N)
matrix_B = create_matrix(250*N)
func = get_usage_time(ndigits=5)(matrix_multiplicathion)
for i in count:
    times[i // (10 * N)] = func(matrix_A[:i, :i], matrix_B[:i, :i])