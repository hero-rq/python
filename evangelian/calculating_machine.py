def calculate_remaining_time():
    # Get the current and start times as input
    hours_current, minutes_current, seconds_current = map(int, input().split(':'))
    hours_start, minutes_start, seconds_start = map(int, input().split(':'))
    
    # Convert times to seconds and calculate the difference
    total_seconds_current = hours_current*3600 + minutes_current*60 + seconds_current
    total_seconds_start = hours_start*3600 + minutes_start*60 + seconds_start
    time_difference = total_seconds_start - total_seconds_current
    
    # If the task started before the current time, calculate the remaining time till the task ends on the next day
    if time_difference < 0:
        time_difference += 24*60*60
    
    # Convert the time difference back to hours, minutes, and seconds
    hours_remaining = time_difference // 3600
    time_difference %= 3600
    minutes_remaining = time_difference // 60
    seconds_remaining = time_difference % 60

    # Print the remaining time
    print("%02d:%02d:%02d" % (hours_remaining, minutes_remaining, seconds_remaining))

# Run the function 
calculate_remaining_time()
