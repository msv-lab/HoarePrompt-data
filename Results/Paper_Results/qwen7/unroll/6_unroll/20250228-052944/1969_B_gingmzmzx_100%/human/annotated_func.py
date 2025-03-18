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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an input integer, and after executing the loop, `ans` is the sum of counts calculated based on the conditions provided within the loop for each input list `s`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a binary string `s`. For each string, it calculates a value `ans` based on the count of zeros and ones in the string. Specifically, for each zero in the string, it adds 1 to `ans` if there has been at least one one before it; otherwise, it adds the total number of zeros minus the count of ones seen so far. The function prints the calculated value `ans` for each test case.

