#State of the program right berfore the function call: Each test case contains an integer n (1 ≤ n ≤ 2 · 10^5) representing the size of the array a. The array a contains n integers a_1, a_2, ..., a_n (0 ≤ a_i < n). The sum of n over all test cases does not exceed 2 · 10^5.
def func_1():
    N = int(input())
    a = list(map(int, input().split()))
    cnt = defaultdict(int)
    for i in range(N):
        cnt[a[i]] += 1
        
    #State: `N` is an integer (1 ≤ `N` ≤ 2 · 10^5), `a` is a list of `N` integers (0 ≤ `a_i` < `N`), `cnt` is a defaultdict with default integer value `0` and contains the frequency of each integer in the list `a`.
    t = 0
    for i in range(N + 1):
        if cnt[i] == 1:
            t += 1
        
        if t >= 2 or cnt[i] == 0:
            return i
        
    #State: the smallest integer `i` where either `cnt[i]` is 0 or `t` becomes 2.
#Overall this is what the function does:The function `func_1` reads an integer `N` and a list of `N` integers from the input. It then determines and returns the smallest integer `i` such that either the integer `i` does not appear in the list, or `i` appears exactly once in the list and there are already at least two other integers that each appear exactly once.

