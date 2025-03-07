#State of the program right berfore the function call: The function is expected to handle multiple test cases, where each test case includes a binary string s. The input to the function should be a list of binary strings, where each string s has a length 2 ≤ |s| ≤ 2 · 10^5, and the sum of lengths of all strings does not exceed 2 · 10^5.
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
        
    #State: The loop iterates `n` times, and for each iteration, it reads a binary string `s`, converts it to a list of integers, and calculates the value of `ans` based on the counts of 0s and 1s in the string. After each iteration, `ans` is printed, and the variables `s`, `zeroes`, `cnt`, and `ans` are reset for the next iteration. The final state of these variables is undefined as they are reset in each iteration. The only variable that remains unchanged is `n`.
#Overall this is what the function does:The function `func_1` reads an integer `n` from the input, which represents the number of test cases. For each test case, it reads a binary string `s` from the input, processes the string to calculate a value `ans`, and prints this value. The value `ans` is computed based on the counts of 0s and 1s in the string `s`. The function does not return any value; it only prints the results for each test case. After processing all test cases, the function concludes, and the only variable that remains unchanged is `n`.

