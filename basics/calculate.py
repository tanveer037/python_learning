def make_float(arg):
    if arg is float:
        return True
    return False

def operation(a,b,*args):
    if 'add' in args:
        return a + b
    elif 'subtract' in args:
        return a - b
    elif 'multiply' in args:
        return a * b
    elif 'divide' in args:
        return a / b
    return "Unspecified request"

def calculate( message = 'The result is', **kwargs):
    result = operation( kwargs['a'],kwargs['b'],kwargs['action'] )
    make_float(result)
    return f"{message} {result}"

data = dict(a = 8, b = 2, action = 'add')

print( calculate(**data) )