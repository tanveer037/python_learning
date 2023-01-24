def contains_purple(*args):
    for arg in args:
        if 'purple' in args:
            state = True
        else: state = False
    return state

print( contains_purple("a", 99, "blah blah blah", 1, True, False, "purple") )