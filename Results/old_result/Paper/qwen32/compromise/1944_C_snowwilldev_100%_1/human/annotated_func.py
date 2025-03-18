#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2 · 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 · 10^5.
def func_1():
    N = int(input())
    a = list(map(int, input().split()))
    cnt = defaultdict(int)
    for i in range(N):
        cnt[a[i]] += 1
        
    #State: `t` is an integer such that 1 ≤ t ≤ 2 · 10^4; `N` is an input integer; `a` is a list of integers obtained by splitting the input string and converting each part to an integer; `cnt` is a defaultdict of type int where each key is an integer from the list `a` and the corresponding value is the count of occurrences of that integer in the list `a`.
    t = 0
    for i in range(N + 1):
        if cnt[i] == 1:
            t += 1
        
        if t >= 2 or cnt[i] == 0:
            return i
        
    #State: the first integer `i` in the range `[0, N]` such that either `t` becomes `2` or `cnt[i]` is `0`.
#Overall this is what the function does:The function reads an integer `N` and a list `a` of `N` integers. It then determines and returns the first integer `i` in the range `[0, N]` such that either at least two integers in `a` appear exactly once, or `i` does not appear in `a`.

