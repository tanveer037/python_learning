def list_manipulation(given_list,command,location,value = None):
    if command == 'remove' and location == 'end':
        return given_list.pop()
    
    if command == 'remove' and location == 'beginning':
        return given_list.pop(0)
    
    if command == 'add' and location == 'beginning':
        given_list.insert(0,value)
        return given_list

    if command == 'add' and location == 'end':
        given_list.append(value)
        return given_list    
# print(list_manipulation( [1,2,3,4],'remove','end'))