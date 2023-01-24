def max_magnitude(iterable_list):
    return max([ abs(item) for item in iterable_list ])

print(max_magnitude([300, 20, -900]))