from  contextlib import contextmanager
from time import time, sleep

@contextmanager
def context_manager(sym):
    print(10 * f"{sym}")

    yield

    print(10 * f"{sym}")

with context_manager("-") as manager:
    print("Printing smth for hte first time")

class ContextManager:
    runtime = []

    def __init__(self, filename, mode, sym):
        self.filename = filename
        self.mode = mode
        self.sym = sym

        print(10 * f"{self.sym}")

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time()
        ContextManager.runtime.append(end)
        self.file.close()
        print(10 * f"{self.sym}")

with ContextManager('example.txt', 'w', "*") as m:
    m.write("New Line")
    print("Printing smth AGAIN")

print(m.closed)