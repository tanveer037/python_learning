def intersection(first_list, second_list):
    new_list = [ 
        item for item in set(first_list).intersection(set(second_list))
    ]
    return new_list

print(intersection([1,2,3], [2,3,4]))
print(intersection(['a','b','z'], ['x','y','z']))