#Examples for closures
import time


def after(seconds, func):
    time.sleep(seconds)
    func()


def greeting():
    print("Hello")

def add(x, y):
    def do_add():
        print("Adding {} + {} = {}".format(x,y,x+y))

    return do_add

'''>>> after(2, add(2,3))
Adding 2 + 3 = 5
>>> after(2,greeting)
Hello
>>>
'''
