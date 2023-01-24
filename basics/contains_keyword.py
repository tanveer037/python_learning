# def contains_keyword(*args):
#     from keyword import iskeyword
#     new_list = list(args)
#     another_list = [ iskeyword(item) for item in new_list ]
#     if True in another_list:
#         return True
#     return False

def contains_keyword(*args):
    from keyword import iskeyword
    for arg in args:
        return iskeyword(arg)
    return False

print(contains_keyword("def", "haha", "lol", "chicken", "alaska"))
print( contains_keyword("blah", "doggo", "crab", "anchor") )