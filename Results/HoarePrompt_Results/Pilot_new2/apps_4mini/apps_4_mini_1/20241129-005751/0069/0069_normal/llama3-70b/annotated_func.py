#State of the program right berfore the function call: T is a positive integer such that 1 <= T <= 100; for each test case, n is a positive integer such that 1 <= n <= 10^5, x is an integer such that -10^9 <= x <= 10^9, and s is a binary string of length n where each character is either '0' or '1'. The total sum of n across all test cases does not exceed 10^5.
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
        
    #State of the program after the  for loop has been executed: `T` is a positive integer such that `1 <= T <= 100`, for each iteration: `n` is an input integer, `x` is an input integer, `s` is an input string, `cnt0` is the count of '0' in `s`, `cnt1` is the count of '1' in `s`, and `balance` is equal to `cnt0 - cnt1`. After all iterations, the outputs depend on the comparisons made within each loop iteration: if `balance` equals `x`, the printed value is `n + 1` for those cases; if `balance` is not equal to `x` and `(x - balance) % (cnt0 - cnt1) == 0`, then -1 is printed; otherwise, the printed value is `(x - balance) // (cnt0 - cnt1) + 1`, assuming `cnt0` is not equal to `cnt1`. If `cnt0` equals `cnt1`, the output conditions may lead to no value being printed.
#Overall this is what the function does:The function accepts multiple test cases, each consisting of a positive integer `n`, an integer `x`, and a binary string `s` of length `n`. It counts the occurrences of '0's and '1's in `s`, computes a balance as the difference between these counts, and determines specific outputs based on the relationship between `balance` and `x`. If `balance` equals `x`, it prints `n + 1`. If the difference between `x` and `balance` is divisible by the difference between the counts of '0' and '1', it prints `-1`. Otherwise, it prints the formula `(x - balance) // (cnt0 - cnt1) + 1`. However, if `cnt0` equals `cnt1`, the division is undefined and may lead to no output for some cases.

