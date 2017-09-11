# custom decorators

from threading import Thread

# generic thread wrapper
def async(func):
    def wrapper(*args, **kwargs):
        th = Thread(target = func, args = args, kwargs = kwargs)
        th.start()
    return wrapper
