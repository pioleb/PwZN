import functools
import time
import statistics

"""

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('executed')
        return func()

    return wrapper


@my_decorator
def my_function(x, y):
    s = 'My function'
    print(s)
    return x + y

print(my_function(3, 7))

"""

#@ functools.cache

def my_decorator(func):
    functime = []

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        functime.append(end - start)
        return result

    def get_statistics():
        return {
            'avg': statistics.mean(functime),
            'min': min(functime),
            'max': max(functime),
            'std': statistics.stdev(functime),
        }

    wrapper.get_statistics = get_statistics
    return wrapper

@my_decorator
def fibon(n):
    if n < 2:
        return n
    
    return fibon(n - 1) + fibon(n -2)

start2 = time.time()
for n in range(30):
    print(n, fibon(n))
stop2 = time.time()
print(f'{stop2 - start2 = }')

stats = fibon.get_statistics()
print("Average:", stats['avg'])
print("Minimum:", stats['min'])
print("Maximum:", stats['max'])
print("Standard deviation:", stats['std'])