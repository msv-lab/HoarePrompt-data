#State of the program right berfore the function call: a and b are non-negative integers such that 1 <= a, b <= 10^9.
def func():
    t = int(input())
    for _rep in range(t):
        n, k = list(map(int, input().split()))
        
        if n > k:
            print('Bob')
        elif n < k:
            print('Alice')
        else:
            print('Bob')
        
    #State: Output State: `a` is a non-negative integer such that \(1 \leq a \leq 10^9\), `b` is a non-negative integer such that \(1 \leq b \leq 10^9\), `t` is an input integer that was initially set but is now exhausted after the loop runs `t` times, `_rep` is equal to `t` (the number of times the loop has executed), `n` and `k` are integers input from the user split by space and converted to an integer. After each iteration, if `n` is greater than `k`, `n` and `k` retain their values; otherwise, they also retain their values. The variables `a` and `b` remain unchanged throughout the loop's execution.
#Overall this is what the function does:The function reads multiple pairs of integers \(n\) and \(k\) from the user, compares each pair, and prints 'Bob' if \(n > k\), 'Alice' if \(n < k\), and 'Bob' again if \(n = k\). After processing all pairs, the function does not return any value.

