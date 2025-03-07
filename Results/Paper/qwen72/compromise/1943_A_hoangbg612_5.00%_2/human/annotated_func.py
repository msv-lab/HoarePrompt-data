#State of the program right berfore the function call: The function `func` is expected to be called with parameters in a context where the input is provided through standard input or a similar mechanism, as it does not take any arguments directly. The input consists of multiple test cases, each with an integer n (1 ≤ n ≤ 2 · 10^5) and a list of n integers a_1, a_2, ..., a_n (0 ≤ a_i < n). The total number of test cases, t, is also provided, with 1 ≤ t ≤ 2 · 10^4, and it is guaranteed that the sum of n over all test cases does not exceed 2 · 10^5.
def func():
    T = int(input())
    for _ in range(T):
        S = int(input())
        
        N = list(map(int, input().split()))
        
        N.sort()
        
        cur = -1
        
        M = {}
        
        for num in N:
            if num > cur:
                if num > cur + 1:
                    cur += 1
                    break
                cur = num
                M[cur] = 1
            else:
                M[cur] += 1
        
        if sum([M[k] for k in M.keys()]) == S:
            cur += 1
        
        for i in range(cur):
            if M[i] <= i:
                cur = i
                break
        
        print(cur)
        
    #State: The loop will print the largest integer `cur` for each test case, such that the condition `M[i] <= i` is not violated for any `i` in the range `0` to `cur - 1`. The variable `cur` will be the final value after processing the list `N` for each test case. The dictionary `M` will contain the counts of integers that were processed, and the list `N` will be sorted. The variable `S` will be the number of unique integers in the list `N` that were processed.
#Overall this is what the function does:The function `func` reads multiple test cases from standard input, processes each test case, and prints the largest integer `cur` for each test case such that the condition `M[i] <= i` is not violated for any `i` in the range `0` to `cur - 1`. Each test case consists of an integer `S` and a list of `S` integers `N`. The function sorts the list `N` and constructs a dictionary `M` to count the occurrences of each integer in `N`. The final value of `cur` is determined based on the counts in `M` and the condition mentioned. The function does not return any value; it only prints the results.

