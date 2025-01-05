#State of the program right berfore the function call: n is an integer representing the number of passengers (1 ≤ n ≤ 100), s is an integer representing the top floor number (1 ≤ s ≤ 1000), and each passenger's data consists of two integers fi and ti (1 ≤ fi ≤ s, 1 ≤ ti ≤ 1000), where fi is the floor number of the passenger and ti is the time of arrival in seconds.
def func():
    n, s = map(int, raw_input().split())
    p = []
    for i in range(n):
        fi, ti = map(int, raw_input().split())
        
        p.append((fi, ti))
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `p` is a list containing `n` tuples of (fi, ti) representing the starting and target floors for each passenger.
    p = sorted(p, key=lambda passenger: passenger[0], reverse=True)
    p.append((0, 0))
    time_passed = 0
    for i in range(n + 1):
        time_passed += s - p[i][0]
        
        s = p[i][0]
        
        if time_passed < p[i][1]:
            time_passed += p[i][1] - time_passed
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `i` is `n`, `s` is `p[n][0]`, `time_passed` is the final computed value after all iterations.
    print(time_passed)
#Overall this is what the function does:The function accepts an integer `n` representing the number of passengers and an integer `s` representing the top floor number. It reads data for each passenger, consisting of their starting floor `fi` and their time of arrival `ti`. The function calculates the total time taken for an elevator to serve all passengers by moving between floors, considering their arrival times. It outputs the total time passed, which includes any delays if the elevator arrives before a passenger's scheduled time. The function assumes valid input based on the constraints provided.

