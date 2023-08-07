inp = 17


def even_gen(inp):
    counter = 0
    while counter < inp:
        if counter % 3 == 0 and counter % 5 == 0:
            yield "FizzBuzz"
            counter += 1
            continue
        elif counter % 3 == 0:
            yield "Fizz"
            counter += 1
            continue
        elif counter % 5 == 0:
            yield "Buzz"
            counter += 1
            continue
        else:
            counter += 1
            yield counter

even = even_gen(inp)

for i in even:
    print(i)