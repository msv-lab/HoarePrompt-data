#State of the program right berfore the function call: n and s are positive integers such that 1 <= n <= 100 and 1 <= s <= 1000. Each passenger arrival floor fi and time ti are positive integers such that 1 <= fi <= s and 1 <= ti <= 1000.**
def func():
    n, s = map(int, raw_input().split())
    p = []
    for i in range(n):
        fi, ti = map(int, raw_input().split())
        
        p.append((fi, ti))
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `s` is a positive integer such that 1 <= s <= 1000, each passenger arrival floor `fi` and time `ti` are positive integers such that 1 <= `fi` <= s and 1 <= `ti` <= 1000, `p` contains the appended tuple with values assigned from the input split for each passenger, `i` is equal to n
    p = sorted(p, key=lambda passenger: passenger[0], reverse=True)
    p.append((0, 0))
    time_passed = 0
    for i in range(n + 1):
        time_passed += s - p[i][0]
        
        s = p[i][0]
        
        if time_passed < p[i][1]:
            time_passed += p[i][1] - time_passed
        
    #State of the program after the  for loop has been executed: At the end of the loop, `time_passed` will be updated based on the calculations in the loop body, `s` will be the arrival floor of the last passenger in the sorted list `p`, `i` will be 0, and all other variables will retain their initial values as described in the initial state.
    print(time_passed)
#Overall this is what the function does:The function `func` reads input values for the number of passengers, building size, arrival floors, and arrival times. It then calculates the total time passed based on the given conditions. However, the function does not return any value, it only prints the total time passed.

