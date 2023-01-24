def interleave(first_string, second_string):
    first_zip = zip(first_string, second_string)
    intermediate_list = [ ''.join(value) for value in first_zip ]
    final_string = ''.join(intermediate_list)
    return final_string

print(interleave('hi','ha'))