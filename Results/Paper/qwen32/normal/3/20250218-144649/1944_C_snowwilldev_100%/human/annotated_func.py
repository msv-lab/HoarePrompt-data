#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 2 · 10^4) representing the number of test cases. For each test case, the first line contains a single integer n (1 ≤ n ≤ 2 · 10^5) representing the size of the array a. The second line contains n integers a_1, a_2, ..., a_n (0 ≤ a_i < n) representing the elements of the array a. The sum of n over all test cases does not exceed 2 · 10^5.
def func_1():
    N = int(input())
    a = list(map(int, input().split()))
    cnt = defaultdict(int)
    for i in range(N):
        cnt[a[i]] += 1
        
    #State: `N` iterations have completed, `i` is `N-1`, `cnt` contains the frequency of each element in the array `a`.
    t = 0
    for i in range(N + 1):
        if cnt[i] == 1:
            t += 1
        
        if t >= 2 or cnt[i] == 0:
            return i
        
    #State: N.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and an array `a` of size `n`. It calculates the frequency of each element in the array and returns the smallest integer `i` such that the frequency of `i` in the array is either 1 or 0, or it returns 2 if there are at least two unique elements with a frequency of 1.

