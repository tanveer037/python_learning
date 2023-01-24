def return_day(day_number):
    week = {
        1: 'Sunday',
        2: 'Monday',
        3: 'Tuesday',
        4: 'Wednesday',
        5: 'Thursday',
        6: 'Friday',
        7: 'Saturday'
    }
    if day_number<1 or day_number>7:
        return None
    return week[day_number]

print( return_day(2) )