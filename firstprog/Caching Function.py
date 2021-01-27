import time
from functools import lru_cache

@lru_cache(maxsize=2)
def some_work(n):
    #Some task taking n seconds
    time.sleep(n)
    return n

def To_Call(str):
    return str

if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    some_work(1)
    some_work(1)
    some_work(1)
    print("Done... Calling again...")
    To_Call(input(""))
    some_work(4)
    print("\nCalled again But Not Reciving !")

