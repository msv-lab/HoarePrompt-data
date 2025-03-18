#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^9.
def func():
    n = int(input())
    ans = 0
    for i in range(1, n // 2 + 1):
        if (i + (n - i)) % 10 ** (len(str(i + (n - i))) - 1) == 0:
            ans += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer within the range \([2, 10^9]\), `ans` is the count of integers `i` from 1 to `n // 2` such that `(i + (n - i)) % 10
    print(ans)
#Overall this is what the function does:The function takes an integer `n` as input, where \(2 \leq n \leq 10^9\). It iterates over all integers `i` from 1 to \(n//2\) and checks if the sum of `i` and `n-i` is divisible by the last non-zero digit of the sum. If the condition is met, it increments the counter `ans`. Finally, it prints the value of `ans`, which represents the count of such integers `i`. The function does not handle any edge cases explicitly; however, the input `n` is assumed to be within the specified range.

