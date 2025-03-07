#State of the program right berfore the function call: The function should take two parameters: a list of integers `a` and an integer `n` representing the size of the list `a`. Additionally, the function should handle multiple test cases, so it should also take an integer `t` indicating the number of test cases. For each test case, `n` is a positive integer (1 ≤ n ≤ 2 · 10^5), and `a` is a list of `n` integers where each integer `a_i` satisfies (0 ≤ a_i < n). The sum of `n` over all test cases does not exceed 2 · 10^5.
def func_1():
    N = int(input())
    a = list(map(int, input().split()))
    cnt = defaultdict(int)
    for i in range(N):
        cnt[a[i]] += 1
        
    #State: The list `a` is a list of integers input by the user, `n` is a positive integer representing the size of the list `a`, `t` is an integer indicating the number of test cases, the sum of `n` over all test cases does not exceed 2 · 10^5, each integer `a_i` in the list `a` satisfies (0 ≤ a_i < n), `cnt` is a defaultdict with default value type `int` and now contains each unique integer `a_i` from the list `a` as keys with their respective values being the count of how many times each integer appears in the list `a`, `i` is `N-1`, `N` is the size of the list `a`.
    t = 0
    for i in range(N + 1):
        if cnt[i] == 1:
            t += 1
        
        if t >= 2 or cnt[i] == 0:
            return i
        
    #State: The loop has completed all iterations. `i` is `N`. `t` is the count of unique integers in the list `a` that appear exactly once, and it is less than 2. If `t` reaches 2 or if `cnt[i]` is 0 for any `i` during the loop, the loop returns the value of `i` at that point. If the loop completes without `t` reaching 2 or encountering a `cnt[i]` that is 0, the final value of `i` is `N` and `t` is the count of unique integers that appear exactly once.
#Overall this is what the function does:The function `func_1` takes no parameters and reads input from the user. It processes a list of integers `a` of size `N`, where each integer `a_i` is in the range (0 ≤ a_i < N). The function counts the occurrences of each integer in the list using a `defaultdict`. It then iterates through the range from 0 to `N` and returns the first integer `i` that either appears exactly once in the list or is missing from the list, provided that no more than one other integer has appeared exactly once before `i`. If no such integer is found, the function returns `N`.

