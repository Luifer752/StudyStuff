from time import time
from functools import wraps


def rate_limit(num=3, time_lim=10):
    call_time = []
    def dec_1(func):
        call_time1 = [i for i in call_time if i <= time_lim]
        @wraps(func)
        def inner(*args, **kwargs):

            start = time()
            counter = 0

            for i in range(num):
                func(*args, **kwargs)
                if len(call_time1) > time_lim:
                    print("Call limit reached")
                    break
                else:
                    call_time1.append(start)

        return inner


    return dec_1

@rate_limit(7, 2)
def say_hi(name):
    print(f"Hello, {name}")

say_hi("sd")