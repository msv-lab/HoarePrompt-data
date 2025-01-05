#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, s is an integer such that 1 ≤ s ≤ 1000, and each passenger's floor fi and arrival time ti are integers such that 1 ≤ fi ≤ s and 1 ≤ ti ≤ 1000.
def func():
    n, s = map(int, raw_input().split())
    p = []
    for i in range(n):
        fi, ti = map(int, raw_input().split())
        
        p.append((fi, ti))
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100, `s` is an integer such that 1 ≤ `s` ≤ 1000, `p` contains `n` tuples of the form `(fi, ti)` collected from user input, `i` is `n`.
    p = sorted(p, key=lambda passenger: passenger[0], reverse=True)
    p.append((0, 0))
    time_passed = 0
    for i in range(n + 1):
        time_passed += s - p[i][0]
        
        s = p[i][0]
        
        if time_passed < p[i][1]:
            time_passed += p[i][1] - time_passed
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100, `s` is equal to `p[n][0]`, `time_passed` is either the final calculated time or equal to `p[n][1]`, `p` is sorted based on the first element of each tuple in descending order, and `i` is `n`.
    print(time_passed)
#Overall this is what the function does:The function accepts two integers, `n` (number of passengers) and `s` (number of floors), and a list of tuples containing each passenger's floor `fi` and arrival time `ti`. It calculates the total time passed based on the passengers' floors and their respective arrival times, returning the final calculated time. The function also ensures that the time passed does not fall short of any passenger's arrival time.

