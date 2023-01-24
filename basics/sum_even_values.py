def sum_even_values(*args):
    sum = 0
    for arg in args:
        if arg %2 == 0:
            sum += arg
    return sum  

print(sum_even_values(1,2,3,4,5,6))