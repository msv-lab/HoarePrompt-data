#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and a is a list of n non-negative integers where 0 ≤ a_i < n. Additionally, the sum of all n values across all test cases does not exceed 2 ⋅ 10^5.
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
        
        cnt = []
        
        for k in M.keys():
            if M[k] == 1:
                cnt.append(k)
        
        if len(cnt) >= 2:
            cur = cnt[1]
        
        print(cur)
        
    #State: Output State: After all iterations of the loop have finished, the dictionary `M` will be empty, as all entries with a value of 1 will have been processed. The list `cnt` will contain all unique keys from the original dictionary `M` that had a value of 1 during the loop's execution. The variable `cur` will be set to the second smallest key in the list `cnt` if the list has at least two elements; otherwise, `cur` will be -1 (or undefined, depending on how the code handles an empty `cnt` list). The variable `T` will be 0, indicating that all input integers have been processed.
    #
    #In simpler terms, after running the loop through all iterations, `M` will be empty because all its entries with a count of 1 will have been removed. `cnt` will hold all the unique keys that appeared exactly once in any of the input lists `N`. `cur` will be the second smallest number in `cnt` if `cnt` has more than one element; otherwise, `cur` will be undefined or -1. Also, `T` will be 0, showing that there are no more inputs to process.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `t`, another positive integer `n`, and a list `a` of `n` non-negative integers. For each test case, it sorts the list `a`, counts the occurrences of each unique number, and identifies numbers that appear exactly once. If there are at least two such numbers, it selects the second smallest one; otherwise, it selects -1. Finally, it prints the selected number for each test case and sets the variable `T` to 0, indicating that all test cases have been processed.

