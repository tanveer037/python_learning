def sum_floats(*args):
    sum = 0
    for arg in args:
        if type(arg) == float:
            sum += arg
    return sum 

print(sum_floats(1.5, 2.4, 'awesome', [], 1))