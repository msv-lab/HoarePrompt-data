#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, s is a binary string such that 2 ≤ |s| ≤ 2 \cdot 10^5 and s_i ∈ {0, 1}.
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
        
    #State: cnt is {0: 3, 1: 2, 'b': 1, 'c': 1, 'a': 1}, zeroes is 3, ans is 3.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `t` (number of binary strings) and a binary string `s`. For each binary string, it counts the number of zeroes and calculates a specific value based on the counts of zeroes and ones in the string. The function prints this calculated value for each test case.

