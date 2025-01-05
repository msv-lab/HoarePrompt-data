t = int(input()) 
for _ in range(t):
    string = str(input())
    
    
    hour, minute = map(int, string.split(":"))
    
    if hour == 0:
        hour_12 = 12
        period = "AM"
    elif hour < 12:
        hour_12 = hour
        period = "AM"
    elif hour == 12:
        hour_12 = 12
        period = "PM"
    else:
        hour_12 = hour - 12
        period = "PM"
    

    print(f"{hour_12:02}:{minute:02} {period}")
