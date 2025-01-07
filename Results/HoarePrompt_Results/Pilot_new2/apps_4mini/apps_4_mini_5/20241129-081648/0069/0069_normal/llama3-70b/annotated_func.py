#State of the program right berfore the function call: T is a positive integer (1 <= T <= 100), n is a positive integer (1 <= n <= 10^5), x is an integer (-10^9 <= x <= 10^9), and s is a binary string of length n (s_i ∈ {0, 1}). The total sum of n across all test cases does not exceed 10^5.
def func():
    T = int(input())
    for _ in range(T):
        n, x = map(int, input().split())
        
        s = input()
        
        cnt0, cnt1 = s.count('0'), s.count('1')
        
        balance = cnt0 - cnt1
        
        if balance == x:
            print(n + 1)
        elif (x - balance) % (cnt0 - cnt1) == 0:
            print(-1)
        else:
            print((x - balance) // (cnt0 - cnt1) + 1)
        
    #State of the program after the  for loop has been executed: `T` is 0, `n` is a positive integer input, `x` is an input integer within the specified range, `s` is an input binary string of length `n`, `cnt0` is the count of '0's in `s`, `cnt1` is the count of '1's in `s`, and `balance` is equal to `cnt0 - cnt1`. The output for each iteration depends on the relationship between `balance` and `x`, with outputs being either `n + 1`, `-1`, or `(x - balance) // (cnt0 - cnt1) + 1` for each iteration of the loop.
#Overall this is what the function does:The function accepts a positive integer T representing the number of test cases. For each test case, it reads a positive integer n, an integer x, and a binary string s of length n. It counts the number of '0's and '1's in s, calculates the balance as the difference between these counts, and prints results based on the relationship between the balance and x. If the balance equals x, it prints n + 1. If (x - balance) is perfectly divisible by (cnt0 - cnt1), it prints -1. Otherwise, it prints the result of the integer division of (x - balance) by (cnt0 - cnt1), incremented by 1. If cnt0 equals cnt1, the balance will be 0, and special handling may be needed in those scenarios as division could lead to incorrect results if not addressed.

