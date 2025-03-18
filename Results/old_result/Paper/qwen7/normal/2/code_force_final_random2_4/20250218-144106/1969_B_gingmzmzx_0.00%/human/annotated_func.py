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
        
    #State: After the loop executes all iterations, `ans` will contain the sum of all instances where a '0' appears in the list `s` and there is at least one '1' in the list so far (contributing 1 to `ans` for each such instance). Additionally, `ans` will also include the difference between the total number of zeros (`zeroes`) and the count of '0's (`cnt[0]`) for each non-zero character '1' in the list `s`. The variable `n` will be decremented to 0 after all iterations, and `t` will retain its initial value as it is not affected by the loop.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `t` and a binary string `s`. For each test case, it calculates and prints a value `ans` based on the occurrences of '0' in the string `s` and the presence of '1' before each '0'. Specifically, `ans` is incremented by 1 for each '0' that has at least one '1' preceding it, and by the difference between the total number of zeros and the count of '0's seen so far for each '1'. The function does not return any value but prints the calculated `ans` for each test case.

