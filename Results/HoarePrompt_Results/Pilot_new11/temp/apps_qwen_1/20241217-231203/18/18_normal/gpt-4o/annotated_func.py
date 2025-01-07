#State of the program right berfore the function call: n, k, and t are integers such that 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k.
def func():
    n, k, t = map(int, input().split())
    if (t <= k) :
        print(t)
    else :
        if (t <= n) :
            print(k)
        else :
            print(n + k - t)
        #State of the program after the if-else block has been executed: *`n`, `k`, and `t` are input integers, where 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k with t being larger than k. If `t` is less than or equal to `n`, then `k` is printed. Otherwise, `n + k - t` is computed and printed.
    #State of the program after the if-else block has been executed: *`n`, `k`, and `t` are input integers with 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k. If `t` is less than or equal to `k`, then `k` is printed. Otherwise, `n + k - t` is computed and printed.
#Overall this is what the function does:The function processes three integers \( n \), \( k \), and \( t \) where \( 1 \leq n \leq 10^9 \), \( 1 \leq k \leq n \), and \( 1 \leq t < n + k \). It prints one of three possible values based on the relationship between these variables:

1. If \( t \leq k \), it prints \( t \).
2. If \( k < t \leq n \), it prints \( k \).
3. If \( t > n \), it prints \( n + k - t \).

The function accepts no direct parameters but operates internally with the given constraints on \( n \), \( k \), and \( t \). After executing, the program state will have one of these three values printed. The function handles all edge cases within the specified ranges.

