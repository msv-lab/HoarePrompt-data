#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and a is a list of n non-negative integers where each integer a_i satisfies 0 ≤ a_i < n. The sum of all n values across all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: Output State: After the loop executes all iterations, `cur` is an integer greater than or equal to 1, and it is the smallest index `i` such that `M[i] > i`, or it is equal to the length of `M` if no such index exists. The state of `T`, `S`, `N`, and `M` will remain unchanged from their final states after the last iteration of the loop. Specifically, `T` will still be the number of test cases, `S` will be the size of the array `N` for each test case, `N` will be the sorted list of integers for each test case, and `M` will be the dictionary where the keys are the unique integers in `N` and the values are the counts of those integers, respecting the conditions specified in the loop body.
    #
    #In simpler terms, after processing all inputs, `cur` will be the smallest number that has more occurrences in the sorted list `N` than its value itself, or the total count of unique numbers in `N` if no such number exists. All other variables (`T`, `S`, `N`, and `M`) will retain their state from the last iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer `t`, a positive integer `n`, and a list `N` of `n` non-negative integers. For each test case, it sorts the list `N` and then determines the smallest integer `i` such that the count of `i` in `N` is greater than `i` itself. If no such integer exists, it returns the total count of unique integers in `N`. The function prints and returns this value for each test case.

