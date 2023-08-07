from  contextlib import contextmanager
from time import time, sleep

@contextmanager
def context_manager():
    start = time()

    yield
    sleep(1)
    end = time()
    print(end - start)

with context_manager() as manager:
    print("Printing smth for hte first time")

class ContextManager:
    runtime = []

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        start = time()
        ContextManager.runtime.append(start)
        print("Init called")

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time()
        ContextManager.runtime.append(end)
        self.file.close()
        print(f"Runtime is: {ContextManager.runtime[1] - ContextManager.runtime[0]}")

with ContextManager('example.txt', 'w') as m:
    m.write("New Line")
    print("Printing smth AGAIN")

print(m.closed)