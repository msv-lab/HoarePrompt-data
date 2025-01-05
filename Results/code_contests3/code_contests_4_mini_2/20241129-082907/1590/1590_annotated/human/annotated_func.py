#State of the program right berfore the function call: n is an integer (1 ≤ n ≤ 100) representing the number of passengers, s is an integer (1 ≤ s ≤ 1000) representing the top floor number, and for each passenger i, fi is an integer (1 ≤ fi ≤ s) representing the floor number where the passenger arrives, and ti is an integer (1 ≤ ti ≤ 1000) representing the time of arrival in seconds.
def func():
    n, s = map(int, raw_input().split())
    p = []
    for i in range(n):
        fi, ti = map(int, raw_input().split())
        
        p.append((fi, ti))
        
    #State of the program after the  for loop has been executed: `n` is an integer (1 ≤ n ≤ 100), `i` is `n - 1`, `p` is a list containing `n` tuples where each tuple is of the form `(fi, ti)` obtained from input.
    p = sorted(p, key=lambda passenger: passenger[0], reverse=True)
    p.append((0, 0))
    time_passed = 0
    for i in range(n + 1):
        time_passed += s - p[i][0]
        
        s = p[i][0]
        
        if time_passed < p[i][1]:
            time_passed += p[i][1] - time_passed
        
    #State of the program after the  for loop has been executed: `time_passed` is equal to the last value of `p[i][1]`, `s` is equal to `p[n][0]`, `i` is `n`, and `p` is a list of tuples sorted based on the first element in descending order with the last tuple being (0, 0).
    print(time_passed)
#Overall this is what the function does:The function accepts an integer `n` representing the number of passengers and an integer `s` representing the top floor number. It then collects the arrival floor `fi` and time `ti` for each passenger, sorts them by arrival floor in descending order, and calculates the total time taken to transport all passengers to their respective floors, including any waiting time if the elevator arrives before the passenger's scheduled time. Finally, it prints the total time taken. The function does not return any value.

