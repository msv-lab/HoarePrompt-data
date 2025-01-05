#State of the program right berfore the function call: n is an integer (1 ≤ n ≤ 100) representing the number of passengers, s is an integer (1 ≤ s ≤ 1000) representing the number of the top floor, and for each passenger, fi is an integer (1 ≤ fi ≤ s) representing the floor number, and ti is an integer (1 ≤ ti ≤ 1000) representing the time of arrival in seconds.
def func():
    n, s = map(int, raw_input().split())
    p = []
    for i in range(n):
        fi, ti = map(int, raw_input().split())
        
        p.append((fi, ti))
        
    #State of the program after the  for loop has been executed: `n` is an integer (1 ≤ n ≤ 100), `i` is equal to `n`, `p` is a list containing `n` tuples of integers (fi, ti).
    p = sorted(p, key=lambda passenger: passenger[0], reverse=True)
    p.append((0, 0))
    time_passed = 0
    for i in range(n + 1):
        time_passed += s - p[i][0]
        
        s = p[i][0]
        
        if time_passed < p[i][1]:
            time_passed += p[i][1] - time_passed
        
    #State of the program after the  for loop has been executed: `n` is an integer (1 ≤ n ≤ 100), `i` is `n`, `p` is sorted in descending order by the first element of each tuple and includes the tuple (0, 0), `s` is `p[n][0]`, and `time_passed` is calculated based on all iterations of the loop.
    print(time_passed)
#Overall this is what the function does:The function accepts an integer `n` representing the number of passengers and an integer `s` representing the top floor. It then collects each passenger's floor number `fi` and their arrival time `ti`. After sorting the passengers based on their floor numbers in descending order, the function calculates the total time taken to accommodate all passengers, considering their arrival times, and prints this total time. The function does not handle cases where the input may not conform to the specified ranges, nor does it handle invalid input types.

