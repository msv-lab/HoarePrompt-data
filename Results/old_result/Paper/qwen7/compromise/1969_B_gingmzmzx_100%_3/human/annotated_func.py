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
        
    #State: `cnt` is [total_count_of_1s, total_count_of_2s], `zeroes` is the total count of 0s in the entire list `s`, `ans` is the final value calculated based on the conditions given in the loop, `s` is an empty list since all elements have been processed, and `c` is undefined.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a binary string `s`. For each test case, it calculates and prints a value `ans` based on the counts of '0's and '1's in the string. Specifically, `ans` is determined by counting the number of positions where a '0' is followed by a '1' and subtracting the number of positions where a '1' is followed by a '0', considering the current counts of '0's and '1's in the string.

