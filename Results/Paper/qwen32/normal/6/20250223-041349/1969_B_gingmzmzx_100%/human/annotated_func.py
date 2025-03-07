#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each of the following t lines contains a binary string s (2 ≤ |s| ≤ 2 · 10^5; s_i ∈ {0, 1}) that needs to be sorted. The sum of the lengths of all strings over all test cases does not exceed 2 · 10^5.
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
        
    #State: The output state after all iterations is a series of `t` integers, each representing the number of inversions in the corresponding binary string from the input.
#Overall this is what the function does:The function `func_1` processes `t` binary strings, each consisting of '0's and '1's, and for each string, it calculates and outputs the number of inversions required to sort the string in non-decreasing order. An inversion is defined as a pair of indices (i, j) such that i < j and s[i] > s[j].

