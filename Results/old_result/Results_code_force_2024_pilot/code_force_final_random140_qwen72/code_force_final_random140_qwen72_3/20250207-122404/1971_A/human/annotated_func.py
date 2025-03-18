#State of the program right berfore the function call: t is an integer where 1 <= t <= 100, and for each of the t test cases, x and y are integers where 0 <= x, y <= 9.
def func():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        print(max(a, b), min(a, b))
        
    #State: `t` is 0, and all pairs of integers (a, b) have been processed, printing the maximum and minimum of each pair.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 <= t <= 100`, representing the number of test cases. For each test case, it reads two integers `a` and `b` (where `0 <= a, b <= 9`) from the input, and prints the maximum and minimum of these two integers. After processing all `t` test cases, the function completes without returning any value. The state of the program after the function concludes is that all input pairs `(a, b)` have been processed and their maximum and minimum values have been printed.

