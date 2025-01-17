# Read input values
d, k, a, b, t = map(int, input().split())

# If the distance to the post office is less than or equal to the distance the car can travel without breaking
if d <= k:
    # Calculate the time taken to drive the entire distance
    print(d * a)
else:
    # Calculate the time taken to drive the first k kilometers
    initial_drive_time = k * a
    # Calculate the remaining distance after the first k kilometers
    remaining_distance = d - k
    
    # Calculate the number of full k kilometers Vasiliy can drive after the first k kilometers
    full_drives = remaining_distance // k
    # Calculate the remaining distance after the full k kilometers drives
    remaining_after_full_drives = remaining_distance % k
    
    # Calculate the time taken for the full k kilometers drives including the repair times
    full_drive_time = full_drives * (k * a + t)
    
    # Calculate the minimal time for the remaining distance after full k kilometers drives
    if remaining_after_full_drives > 0:
        # Option 1: Drive the remaining distance and repair the car (if needed)
        drive_remaining_time = remaining_after_full_drives * a + t if remaining_distance > k else remaining_after_full_drives * a
        # Option 2: Walk the remaining distance
        walk_remaining_time = remaining_after_full_drives * b
        
        # Choose the minimal time option for the remaining distance
        remaining_time = min(drive_remaining_time, walk_remaining_time)
    else:
        # No remaining distance, no additional time needed
        remaining_time = 0
    
    # Calculate the total minimal time
    total_time = initial_drive_time + full_drive_time + remaining_time
    
    # Output the result
    print(total_time)
