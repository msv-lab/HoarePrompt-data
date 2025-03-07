#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 2 · 10^4) representing the number of test cases. Each test case consists of two lines: the first line contains a single integer n (1 ≤ n ≤ 2 · 10^5) representing the size of the array a, and the second line contains n integers a_1, a_2, ..., a_n (0 ≤ a_i < n) representing the elements of the array a. The sum of n over all test cases does not exceed 2 · 10^5.
def func_1():
    N = int(input())
    a = list(map(int, input().split()))
    cnt = defaultdict(int)
    for i in range(N):
        cnt[a[i]] += 1
        
    #State: `N` is the number of elements in the list `a`, `i` is `N-1` after the final iteration, `a` is a list of integers, and `cnt` is a defaultdict with default factory function `int` where each key in `cnt` corresponds to an integer in `a` and its value is the count of how many times that integer appears in `a`.
    t = 0
    for i in range(N + 1):
        if cnt[i] == 1:
            t += 1
        
        if t >= 2 or cnt[i] == 0:
            return i
        
    #State: 3.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and an array `a` of `n` integers. It returns the smallest integer `i` such that the count of `i` in the array is 1, or the first integer `i` where the count of `i` is 0, or 3 if neither condition is met before reaching `i = N`.

