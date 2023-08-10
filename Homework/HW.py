def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fibonacci_gen = fibonacci_generator()

for i in range(100):
    print(next(fibonacci_gen))

