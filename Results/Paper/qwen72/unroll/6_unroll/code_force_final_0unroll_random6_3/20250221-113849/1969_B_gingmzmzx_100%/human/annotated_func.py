#State of the program right berfore the function call: The function should take a single argument, a list of binary strings, where each string s has a length 2 ≤ |s| ≤ 2 · 10^5 and consists only of '0's and '1's. The sum of the lengths of all strings in the list does not exceed 2 · 10^5.
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
        
    #State: The loop will execute `n` times, and for each iteration, it will read a binary string `s` from the input, convert it into a list of integers, and then compute and print the value of `ans` based on the number of '0's and '1's in the string. After all iterations, the loop will have printed `n` lines, each containing the computed value of `ans` for the corresponding binary string. The variables `s`, `zeroes`, `cnt`, and `ans` will be reset for each iteration, so their final values will be the ones from the last iteration.
#Overall this is what the function does:The function `func_1` reads an integer `n` from the input, indicating the number of binary strings to process. For each of the `n` iterations, it reads a binary string `s` from the input, converts it into a list of integers, and computes a value `ans` based on the number of '0's and '1's in the string. The function then prints the computed value of `ans` for each binary string. After processing all `n` binary strings, the function will have printed `n` lines, each containing the computed value of `ans` for the corresponding binary string. The function does not return any value.

