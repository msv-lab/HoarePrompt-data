#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (1 ≤ n ≤ 2 · 10^5) representing the size of the array a. The next line contains n integers a_1, a_2, ..., a_n (0 ≤ a_i < n) representing the elements of the array a. The sum of n over all test cases does not exceed 2 · 10^5.
def func_1():
    N = int(input())
    a = list(map(int, input().split()))
    cnt = defaultdict(int)
    for i in range(N):
        cnt[a[i]] += 1
        
    #State: - After the loop finishes, `cnt` will contain the frequency of each integer in the list `a`. Each key in `cnt` corresponds to a unique integer from the list `a`, and the value associated with each key is the number of times that integer appears in the list.
    #
    #Given this understanding, the output state can be described as follows:
    #
    #Output State:
    t = 0
    for i in range(N + 1):
        if cnt[i] == 1:
            t += 1
        
        if t >= 2 or cnt[i] == 0:
            return i
        
    #State: the loop returns `N`.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list of `n` integers. For each test case, it returns the smallest integer from `0` to `n` that either appears exactly once in the list or does not appear at all.

