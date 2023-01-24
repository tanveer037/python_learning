def number_compare(first_value,second_value):
    if first_value > second_value:
        return "First is greater"
    if second_value > first_value:
        return "Second is greater"
    return "Numbers are equal"

print(number_compare(4,4))