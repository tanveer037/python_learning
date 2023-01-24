from functools import wraps


def only_ints(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if all(isinstance(x,int) for x in args or kwargs):
            return fn(*args, **kwargs)
        return "Please only invoke with integers."
    return wrapper


@only_ints
def add(x,y):
    return x + y


print(add(y=7, x = 'sds'))
print(add(1,4))
print(add("1", "2"))