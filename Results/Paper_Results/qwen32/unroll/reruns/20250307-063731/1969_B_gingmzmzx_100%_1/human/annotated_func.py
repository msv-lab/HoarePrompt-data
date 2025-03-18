#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each test case consists of a binary string s (2 ≤ |s| ≤ 2 · 10^5; s_i ∈ {0, 1}) that needs to be sorted. The sum of the lengths of all strings over all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` is an integer (1 ≤ t ≤ 10^4) representing the number of test cases; `n` is an input integer.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of a binary string `s`. For each binary string, it calculates and prints an integer value `ans` which represents the number of swaps needed to sort the binary string in non-decreasing order.

