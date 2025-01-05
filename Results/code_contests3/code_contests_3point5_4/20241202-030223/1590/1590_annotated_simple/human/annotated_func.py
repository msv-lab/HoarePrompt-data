#State of the program right berfore the function call: n and s are integers such that 1 <= n <= 100 and 1 <= s <= 1000. The input details the arrival floor and time for each passenger.**
def func():
    n, s = map(int, raw_input().split())
    p = []
    for i in range(n):
        fi, ti = map(int, raw_input().split())
        
        p.append((fi, ti))
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `s` is an integer between 1 and 1000, `p` contains `n` tuples with values `(fi, ti)` where `fi` and `ti` are integers, `i` is equal to `n-1`
    p = sorted(p, key=lambda passenger: passenger[0], reverse=True)
    p.append((0, 0))
    time_passed = 0
    for i in range(n + 1):
        time_passed += s - p[i][0]
        
        s = p[i][0]
        
        if time_passed < p[i][1]:
            time_passed += p[i][1] - time_passed
        
    #State of the program after the  for loop has been executed: At the end of the loop, `time_passed` will be the total time passed based on the calculations made within the loop, `s` will be the value of the last `fi` encountered in the loop, `p` will remain the same as the initial state with `n+1` tuples with values `(fi, ti)`.
    print(time_passed)
#Overall this is what the function does:The function `func` reads input details of arrival floor and time for each passenger, processes them, and calculates the total time passed based on certain conditions. It does not accept any parameters and does not return any values. The function sorts the passengers based on their arrival floor in descending order, simulates their movement, and calculates the total time passed. The code implements the logic described in the annotations regarding time calculations and sorting passengers.

