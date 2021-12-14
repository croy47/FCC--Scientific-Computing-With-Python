def add_time(start, duration,day=False):
    # 
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    meridium = ['AM', 'PM']
    # 
    start_list = start.replace(':', " ").split()
    duration_list = duration.split(':')
    # 
    minute = int(start_list[1]) + int(duration_list[1])
    hour = int(start_list[0]) + int(duration_list[0])
    curr_meridium = start_list[2]
    days_lapsed = 0
    
    # if minute > 60: increase an hour and rest becomes minute. if less than 10, add a leading zero to it.
    if minute > 60:
        hour += 1
        # MINUTE HAS TO BE NORMALIZED NOW.
    minute = (minute % 60) if (minute % 60) > 9 else f'0{minute % 60}'
        
    # meridium changes every time hour crosses 12.
    if hour >= 12:
        # DAY CHANGE LOGIC. Day changes every time meridium hits AM. 
        days_lapsed = (hour // 12 + meridium.index(curr_meridium)) // 2 
        
        curr_meridium = meridium[(hour // 12 + meridium.index(curr_meridium)) % 2]
    #    when it's 12 or 12x, it should be 12 else hour % 12
        hour = hour % 12 if hour % 12 > 0 else 12

        
# results based on various conditions
    new_time = f'{hour}:{minute} {curr_meridium}'
#  
    if day:
        day = day.capitalize()
        day_index = weekdays.index(day)
        new_day = weekdays[(day_index + days_lapsed) % 7]
        new_time += f', {new_day}'
    # 
    if days_lapsed:
        if days_lapsed > 1:          
            new_time += f' ({days_lapsed} days later)'
        elif days_lapsed == 1:
            new_time += f' (next day)'
    # print(new_time)    
    return new_time
         


# add_time('5:1 AM', '0:00')
        
# add_time("8:16 PM", "466:02", "tuesday")    

# add_time("3:00 PM", "3:10")
# # # # Returns: 6:10 PM

# add_time("11:30 AM", "2:32", "Monday")
# # # # Returns: 2:02 PM, Monday

# add_time("11:43 AM", "00:20")
# # # Returns: 12:03 PM

# add_time("10:10 PM", "3:30")
# # # # Returns: 1:40 AM (next day)

# add_time("11:43 PM", "24:20", "tueSday")
# # # Returns: 12:03 AM, Thursday (2 days later)

# add_time("6:30 PM", "205:12")
# # # Returns: 7:42 AM (9 days later)