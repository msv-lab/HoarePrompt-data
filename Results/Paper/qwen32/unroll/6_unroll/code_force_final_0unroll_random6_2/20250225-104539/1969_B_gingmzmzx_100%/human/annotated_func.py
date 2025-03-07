#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each of the next t lines contains a binary string s (2 ≤ |s| ≤ 2 · 10^5; s_i ∈ {0, 1}) which needs to be sorted in non-descending order. The sum of the lengths of all strings s over all test cases does not exceed 2 · 10^5.
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
        
    #State: a series of integers, each representing the number of inversions for each binary string in the input.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads a binary string `s`. It calculates and prints the number of inversions in each binary string, where an inversion is defined as a pair of indices (i, j) such that i < j and s[i] > s[j].

