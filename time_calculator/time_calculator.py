"""
Enter a start time and the duration period to get the final time.
Optionally, you may enter the start day of the week.

Parameters
----------
start: str
    Start time in the 12-hour clock format (ending if AM or PM).
duration: str
    Duration time that indicates the number of hours and minutes.
day: str (optional)
    Starting day of the week.

Returns
-------
new_time: str
    Result represents the duration time added to the start time,
    showing if the result will be in the next day, someday in the
    future or in the same day as the start time.

Examples
--------
>>> add_time("3:00 PM", "3:10")
6:10 PM
"""


def add_time(start, duration, day=None):
    start_time = start.split()
    
    if start_time[1] == 'AM':
        start_time_hour = start_time[0].split(':')[0]
        start_time_hour = int(start_time_hour)
    else:
        start_time_hour = start_time[0].split(':')[0]
        start_time_hour = int(start_time_hour) + 12
    
    start_time_min = start_time[0].split(':')[1]
    start_time_min = int(start_time_min)
    
    duration_time = duration.split(':')
    duration_time_hour = duration_time[0]
    duration_time_hour = int(duration_time_hour)
    duration_time_min = duration_time[1]
    duration_time_min = int(duration_time_min)    
    
    hour: int
    min: int
    hformat = start_time[1]
    days_passed = 0
    
    hour = start_time_hour + duration_time_hour
    min = start_time_min + duration_time_min
    
    if min >= 60:
        min -= 60
        hour += 1
    
    if hour >= 24:
        while hour >= 24:
            days_passed += 1
            hour -= 24        
    
    hformat = start_time[1]
    
    if hformat == 'AM':
        if hour == 12:
            hformat = 'PM'
        elif hour > 12:
            hour -= 12
            hformat = 'PM'
    elif hformat == 'PM':
        if hour == 0:
            hour += 12
            hformat = 'AM'
        elif hour < 12:
            hformat = 'AM'
        elif hour >= 12 and hour < 24:
            hour -= 12
        elif hour == 24:
            hour -= 12
            hformat = 'AM'
    
    hour = str(hour)

    if min >= 10:    
        min = str(min)
    else:
        min = f'0{str(min)}'
    
    new_time = f'{hour}:{min} {hformat}'
    week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    control = days_passed
    
    if day is not None:
        day = day.lower()
        
        for e in week:
            if e == day:
                day_count = week.index(e)    
        
        while control > 0:
            day_count += 1
            
            if day_count > 6:
                day_count = 0
            
            day = week[day_count]
            control -= 1
           
        day = day.capitalize()
        new_time = f'{hour}:{min} {hformat}, {day}'
    
    if days_passed == 1:
        new_time += f' (next day)'
    elif days_passed > 1:
        new_time += f' ({days_passed} days later)'

    return new_time


# Tests
print('[Test 1: Same Period]')
print(add_time("3:30 PM", "2:12"))

print('\n[Test 2: Different Period]')
print(add_time("11:55 AM", "3:12"))

print('\n[Test 3: Next Day]')
print(add_time("9:15 PM", "5:30"))

print('\n[Test 4: Period Change at Twelve]')
print(add_time("11:40 AM", "0:25"))

print('\n[Test 5: Twenty Four]')
print(add_time("2:59 AM", "24:00"))

print('\n[Test 6: Two Days Later]')
print(add_time("11:59 PM", "24:05"))

print('\n[Test 7: High Duration]')
print(add_time("8:16 PM", "466:02"))

print('\n[Test 8: No Change]')
print(add_time("5:01 AM", "0:00"))

print('\n[Test 9: Same Period with Day]')
print(add_time("3:30 PM", "2:12", "Monday"))

print('\n[Test 10: Twenty Four with Day]')
print(add_time("2:59 AM", "24:00", "saturDay"))

print('\n[Test 11: Two Days Later with Day]')
print(add_time("11:59 PM", "24:05", "Wednesday"))

print('\n[Test 12: High Duration with Day]')
print(add_time("8:16 PM", "466:02", "tuesday"))
