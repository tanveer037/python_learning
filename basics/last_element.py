def last_element(given_list):
    if given_list == []:
        return None
    return given_list.pop()

final_element = last_element( [] )
print(final_element)