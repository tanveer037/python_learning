def compact(given_list):
    return [ item for item in given_list if item ]

print( compact( [0,1,2,"",[], False, {}, None, "All done"]) ) 