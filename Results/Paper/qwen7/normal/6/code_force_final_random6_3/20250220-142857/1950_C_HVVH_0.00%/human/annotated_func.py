#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1440, and for each test case, s is a string of length 5 in the format "hh:mm" representing a valid time in 24-hour format where hh is the hour from 00 to 23 and mm is the minute from 00 to 59.
def func():
    day = 'AM'
    n = int(input())
    for _ in range(n):
        h, m = map(int, input().split(':'))
        
        if h == 0:
            h = 12
            day = 'AM'
        elif h > 12:
            h = h - 12
            day = 'PM'
        else:
            day = 'PM'
            if h == 12:
                day = 'AM'
        
        print(f'{h:02d}:{m:02d}', day)
        
    #State: Output State: The final output state after the loop executes all its iterations will depend on the value of `n`, which represents the total number of times the loop runs. Here's how the variables will be affected:
    #
    #- `day`: Will be either 'AM' or 'PM' based on the last iteration of the loop.
    #- `h`: Will be an integer representing the hour after being adjusted according to the conditions inside the loop (i.e., converting 0 to 12 for AM, reducing hours over 12 by 12, and adjusting 12 to AM/PM).
    #- `m`: Will remain unchanged as it is not modified within the loop.
    #
    #In summary, after all iterations of the loop have finished, `day` will reflect the time period ('AM' or 'PM') corresponding to the last processed hour (`h`), while `m` retains its original input value, and `h` is adjusted according to the rules specified in the loop body.
#Overall this is what the function does:The function processes a series of times in the format "hh:mm" and converts them to 12-hour format with AM/PM notation. It prints out each converted time. After processing all inputs, the function does not return any value but leaves the variables `h`, `m`, and `day` in their final states reflecting the last processed time.

