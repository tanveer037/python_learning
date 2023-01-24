from functools import wraps
from time import sleep


def delay(t):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            # print(f"Waiting {t}s before running {fn.__name__}")
            print("Waiting {}s before running {}".format(t,fn.__name__))
            sleep(t)
            return fn(*args, **kwargs)
        return wrapper
    return decorator    


@delay(3)
def say_hi():
    return "hi"


print( say_hi() )