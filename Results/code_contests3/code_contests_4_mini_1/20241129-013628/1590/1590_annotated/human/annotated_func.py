#State of the program right berfore the function call: n is an integer (1 ≤ n ≤ 100) representing the number of passengers, s is an integer (1 ≤ s ≤ 1000) representing the number of the top floor, and for each passenger, fi is an integer (1 ≤ fi ≤ s) indicating the floor number where the passenger arrives, and ti is an integer (1 ≤ ti ≤ 1000) indicating the time of arrival in seconds.
def func():
    n, s = map(int, raw_input().split())
    p = []
    for i in range(n):
        fi, ti = map(int, raw_input().split())
        
        p.append((fi, ti))
        
    #State of the program after the  for loop has been executed: `n` is an integer (1 ≤ n ≤ 100), `s` is an integer (1 ≤ s ≤ 1000), `p` contains `n` tuples of integers (fi, ti) where each tuple is from input and `i` is equal to `n`.
    p = sorted(p, key=lambda passenger: passenger[0], reverse=True)
    p.append((0, 0))
    time_passed = 0
    for i in range(n + 1):
        time_passed += s - p[i][0]
        
        s = p[i][0]
        
        if time_passed < p[i][1]:
            time_passed += p[i][1] - time_passed
        
    #State of the program after the  for loop has been executed: `n` is an integer (1 ≤ n ≤ 100), `s` is the value of `p[n][0]`, `time_passed` is the maximum value of `p[i][1]` for `i` in the range [0, n].
    print(time_passed)
#Overall this is what the function does:The function accepts an integer `n` representing the number of passengers and an integer `s` representing the top floor. It reads `n` pairs of integers (floor number and time of arrival) for each passenger. The function calculates the total time required to serve all passengers, considering the time taken to travel to each passenger's specified floor and waiting times. It returns the total time passed.

