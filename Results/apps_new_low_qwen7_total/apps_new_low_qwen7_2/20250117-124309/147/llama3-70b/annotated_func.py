#State of the program right berfore the function call: n and k are integers such that 2 ≤ k < n ≤ 100, and a list of n integers where each integer is either 1 or -1.
def func():
    n, k = map(int, input().split())

tabs = list(map(int, input().split()))

max_diff = 0
    for b in range(1, n + 1):
        e, s = 0, 0
        
        for i in range(1, n + 1):
            if (i - b) % k != 0:
                e += tabs[i - 1] == 1
                s += tabs[i - 1] == -1
        
        max_diff = max(max_diff, abs(e - s))
        
    #State of the program after the  for loop has been executed: `b` is `n`, `max_diff` is the maximum absolute difference between the counts of `1`s and `-1`s among the segments defined by `(i - b) % k != 0` for all `b` from `1` to `n`, `e` and `s` are not needed as they are local variables, `n` remains the same, and `k` remains unchanged.
    print(max_diff)
#Overall this is what the function does:The function accepts a list of integers where each integer is either 1 or -1, and two integers \( n \) and \( k \) such that \( 2 \leq k < n \leq 100 \). It calculates and returns the maximum absolute difference between the counts of 1s and -1s among the segments defined by \((i - b) \% k \neq 0\) for all \( b \) from 1 to \( n \). The function iterates over all possible values of \( b \) from 1 to \( n \), maintaining counters \( e \) and \( s \) for the counts of 1s and -1s respectively, within the specified segments. The maximum absolute difference found during these iterations is stored in the variable `max_diff`, which is printed at the end.

