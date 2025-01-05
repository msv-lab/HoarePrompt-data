#State of the program right berfore the function call: n is an integer (1 ≤ n ≤ 100) representing the number of passengers, s is an integer (1 ≤ s ≤ 1000) representing the top floor, and each passenger is described by two integers fi and ti (1 ≤ fi ≤ s, 1 ≤ ti ≤ 1000) indicating the floor and arrival time of the passenger.
def func():
    n, s = map(int, raw_input().split())
    p = []
    for i in range(n):
        fi, ti = map(int, raw_input().split())
        
        p.append((fi, ti))
        
    #State of the program after the  for loop has been executed: `n` is an integer (1 ≤ n ≤ 100), `s` is an integer (1 ≤ s ≤ 1000), `i` is `n - 1`, `p` is a list containing `n` tuples of integers (fi, ti) from input.
    p = sorted(p, key=lambda passenger: passenger[0], reverse=True)
    p.append((0, 0))
    time_passed = 0
    for i in range(n + 1):
        time_passed += s - p[i][0]
        
        s = p[i][0]
        
        if time_passed < p[i][1]:
            time_passed += p[i][1] - time_passed
        
    #State of the program after the  for loop has been executed: `n` is an integer (1 ≤ n ≤ 100), `s` is the last value of `p[n][0]`, `i` is `n`, `p` contains `n + 1` tuples, and `time_passed` is the maximum value among `p[i][1]` for all `i` from 0 to `n` if `time_passed` was less than that maximum during the loop execution, otherwise it remains the accumulated value from the loop.
    print(time_passed)
#Overall this is what the function does:The function accepts an integer `n` (number of passengers) and an integer `s` (top floor) as inputs, then processes a list of `n` passengers characterized by their respective floor `fi` and arrival time `ti`. It calculates the total time taken for the elevator to serve all passengers and prints this time. The function handles cases where the time spent may need to be adjusted based on the passengers' arrival times. It ensures that the elevator waits if it arrives before a passenger's specified arrival time.

