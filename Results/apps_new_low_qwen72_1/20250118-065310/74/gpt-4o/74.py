def main():
    # Reading input values
    c, v_0, v_1, a, l = map(int, input().split())
    
    days = 0
    pages_read = 0
    current_speed = v_0
    
    while pages_read < c:
        days += 1
        if days == 1:
            # First day reading
            pages_read += v_0
        else:
            # Subsequent days reading: considering reread pages
            pages_read += min(current_speed, v_1) - l
            current_speed += a
        
        # Ensure the reading speed does not exceed v_1
        current_speed = min(current_speed, v_1)
        
        # If the reread pages are more than the pages read, reset the pages_read to zero
        if pages_read < 0:
            pages_read = 0
    
    print(days)

if __name__ == "__main__":
    main()
