def divide(first_input,second_input):
    try:
        return first_input / second_input
    except ZeroDivisionError:
        if second_input == 0:
           return "Please do not divide by zero"
    except TypeError:
        if (first_input is not int or float) or (second_input is not int or float):
            return "Please provide two integers or floats"
        
print( divide('a',5) )