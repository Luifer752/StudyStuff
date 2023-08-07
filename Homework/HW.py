from time import time
from functools import wraps


def rate_limit(num=3, time_lim=10):

    def dec_1(func):
        call_time = []
        @wraps(func)
        def inner(*args, **kwargs):
            start = time()
            counter = 0

            for i in range(num):
                func(*args, **kwargs)
                counter += 1
                a.append(start)
                if start == time_lim or counter == num:
                    break

        return inner


    return dec_1

@rate_limit(4, 2)
def say_hi(name):
    print(f"Hello, {name}")

say_hi("sd")