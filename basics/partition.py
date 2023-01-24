def isEven(num):
    return num % 2 == 0

def partition(given_list,given_function):
    return [ 
        [ num for num in given_list if given_function(num) ], 
        [ num for num in given_list if not given_function(num) ]
    ]

print(partition([1,2,3,4], isEven))