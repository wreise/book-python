import sys

sys.setrecursionlimit(5000)


# Simple Dict Cache
CACHE = {}

def factorial_cache(n: int) -> int:
    if n not in CACHE:

        if n == 0:
            CACHE[n] = 1
        else:
            CACHE[n] = n * factorial_cache(n - 1)

    return CACHE[n]


# Do not modify anything below
from timeit import timeit


def factorial_nocache(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial_nocache(n - 1)


duration_cache = timeit(
    stmt='factorial_cache(500); factorial_cache(400); factorial_cache(450); factorial_cache(350)',
    globals=globals(),
    number=10000,
)

duration_nocache = timeit(
    stmt='factorial_nocache(500); factorial_nocache(400); factorial_nocache(450); factorial_nocache(350)',
    globals=globals(),
    number=10000
)

print(f'factorial_cache time: {round(duration_cache, 4)} seconds')
print(f'factorial_nocache time: {round(duration_nocache, 3)} seconds')
print(f'Cached solution is {round(duration_nocache / duration_cache, 1)} times faster')


# Decorator
CACHE_DECORATOR = {}

def cache(func):
    def wrapper(n):
        if n not in CACHE_DECORATOR:
            CACHE_DECORATOR[n] = func(n)
        return CACHE_DECORATOR[n]
    return wrapper

@cache
def factorial_decorator(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial_decorator(n - 1)


duration_decorator = timeit(
    stmt='factorial_decorator(500); factorial_decorator(400); factorial_decorator(450); factorial_decorator(350)',
    globals=globals(),
    number=10000
)

print(f'factorial_decorator time: {round(duration_decorator, 4)} seconds')
