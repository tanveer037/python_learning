from functools import wraps


def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        l1 = [x for x in args]
        if len(l1) > 2:
            return 'Too many arguments'
        return fn(*args, **kwargs)
    return wrapper


@ensure_fewer_than_three_args
def add_all(*nums):
    return sum(nums)


print(add_all(1,2))
print(add_all(1,2,3))
