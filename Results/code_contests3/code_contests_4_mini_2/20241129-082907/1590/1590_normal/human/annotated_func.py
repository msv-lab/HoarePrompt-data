#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 100, s is a positive integer such that 1 ≤ s ≤ 1000, and each of the next n lines contains two integers fi and ti where 1 ≤ fi ≤ s and 1 ≤ ti ≤ 1000.
def func():
    n, s = map(int, raw_input().split())
    p = []
    for i in range(n):
        fi, ti = map(int, raw_input().split())
        
        p.append((fi, ti))
        
    #State of the program after the  for loop has been executed: `n` is a positive integer within the range of 1 to 100; `s` is a positive integer within the range of 1 to 1000; `p` contains `n` tuples of the form (fi, ti); `i` is `n`.
    p = sorted(p, key=lambda passenger: passenger[0], reverse=True)
    p.append((0, 0))
    time_passed = 0
    for i in range(n + 1):
        time_passed += s - p[i][0]
        
        s = p[i][0]
        
        if time_passed < p[i][1]:
            time_passed += p[i][1] - time_passed
        
    #State of the program after the  for loop has been executed: `n` is a positive integer within the range of 1 to 100; `s` is the value of `p[n][0]`; `p` is sorted based on the first element of the tuples in descending order and includes the tuple (0, 0); `i` is `n`; `time_passed` is the total accumulated value after all iterations, which is at least `p[n][1]` or more depending on the conditions met during the loop.
    print(time_passed)
#Overall this is what the function does:The function reads a positive integer `n` and a positive integer `s`, followed by `n` pairs of integers (`fi`, `ti`). It calculates the total time passed based on the sorted order of `fi` values in descending order and the conditions set by `ti`. The function then prints the total time passed, which is derived from the values of `s` and the conditions in the loop. It implicitly handles the case where no passengers are provided by including a tuple (0, 0) to ensure the calculation proceeds without error.

