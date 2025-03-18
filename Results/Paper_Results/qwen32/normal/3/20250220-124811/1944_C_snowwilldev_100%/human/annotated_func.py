#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2 · 10^4, each test case consists of an integer n such that 1 ≤ n ≤ 2 · 10^5, and a list of n integers a where 0 ≤ a_i < n, with the sum of n over all test cases not exceeding 2 · 10^5.
def func_1():
    N = int(input())
    a = list(map(int, input().split()))
    cnt = defaultdict(int)
    for i in range(N):
        cnt[a[i]] += 1
        
    #State: `t` is an integer such that 1 ≤ t ≤ 2 · 10^4, `N` is an integer read from input where 1 ≤ N ≤ 2 · 10^5, `a` is a list of `N` integers where 0 ≤ a_i < N, `cnt` is a defaultdict with default integer values where `cnt[a[i]]` is incremented by 1 for each occurrence of `a[i]` in `a`, and `i` is equal to `N`.
    t = 0
    for i in range(N + 1):
        if cnt[i] == 1:
            t += 1
        
        if t >= 2 or cnt[i] == 0:
            return i
        
    #State: the value of `i` at which the loop terminates.
#Overall this is what the function does:The function reads an integer `N` and a list of `N` integers `a`. It then counts the occurrences of each integer in the list. The function returns the smallest integer `i` such that `i` either has zero occurrences or at least two integers in the list have exactly one occurrence each.

