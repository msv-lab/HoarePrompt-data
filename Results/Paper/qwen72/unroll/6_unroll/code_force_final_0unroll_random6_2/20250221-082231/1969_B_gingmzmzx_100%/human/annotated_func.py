#State of the program right berfore the function call: The function should take a binary string `s` as input, where `2 <= len(s) <= 2 * 10^5` and each character in `s` is either '0' or '1'. The function should also handle multiple test cases, where the number of test cases `t` is an integer such that `1 <= t <= 10^4`. The sum of the lengths of all strings across all test cases does not exceed `2 * 10^5`.
def func_1():
    n = int(input())
    for _ in range(n):
        s = list(map(int, input().strip()))
        
        zeroes = s.count(0)
        
        cnt = [0, 0]
        
        ans = 0
        
        for c in s:
            cnt[c] += 1
            if c == 0:
                ans += 1 if cnt[1] > 0 else 0
            else:
                ans += zeroes - cnt[0]
        
        print(ans)
        
    #State: The loop will execute `n` times, and for each execution, it will read a new binary string `s` from the input, convert it to a list of integers, count the number of zeroes in `s`, and then compute and print the value of `ans` which represents the sum of the number of '1's before each '0' and the number of '0's after each '1' in the string `s`. After `n` iterations, the loop will terminate, and the final state will be that `n` will be 0, and the values of `s`, `zeroes`, `cnt`, and `ans` will be undefined or reset for each iteration.
#Overall this is what the function does:The function `func_1` reads an integer `n` from the input, representing the number of test cases. For each test case, it reads a binary string `s` from the input, processes it to compute a value `ans`, and prints `ans`. The value `ans` represents the sum of the number of '1's before each '0' and the number of '0's after each '1' in the string `s`. After processing all `n` test cases, the function terminates, and the final state is that `n` test cases have been processed, and the results for each test case have been printed. The variables `s`, `zeroes`, `cnt`, and `ans` are reset for each test case.

