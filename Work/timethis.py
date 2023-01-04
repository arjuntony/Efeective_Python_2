import time

def timethis(func):
    def wrapper(*args , **kwargs):
        print(" Function Started")
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(" Function Ended")
        print("Time taken to execute this function is : ",end-start)
        return res

    return wrapper

@timethis
def countdown(n):
    while n >0:
        n -= 1
