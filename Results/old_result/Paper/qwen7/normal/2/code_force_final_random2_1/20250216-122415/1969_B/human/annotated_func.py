#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, s is a binary string such that 2 ≤ |s| ≤ 2 ⋅ 10^5 and s_i ∈ {0, 1}.
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
        
    #State: `ans` will be the total count of zeros in the list `s` plus the count of ones multiplied by the initial number of zeros minus the count of ones encountered so far, `n` will be the length of the list `s`, `zeroes` will be the count of zeros in the list `s` after processing all elements, and `cnt` will contain the final counts of zeros and ones in the list `s`.
#Overall this is what the function does:The function processes multiple test cases where each test case consists of an integer `t` and a binary string `s`. For each test case, it calculates and prints a value based on the counts of zeros and ones in the string `s`. Specifically, it computes the sum of the counts of zeros and the product of the count of ones and the initial count of zeros, adjusted as it iterates through the string.

