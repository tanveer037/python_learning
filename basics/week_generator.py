def week():
    days_in_week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    count = 0
    while count < len(days_in_week):
        yield days_in_week[count]
        count += 1


days = week()
print( next(days) )
print( next(days) )
print( next(days) )
print( next(days) )
print( next(days) )
print( next(days) )
print( next(days) )