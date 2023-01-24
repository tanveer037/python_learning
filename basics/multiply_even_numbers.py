def multiply_even_numbers(given_list):
    total = 1
    for num in given_list:
        if num%2==0:
            total = total*num
    return total