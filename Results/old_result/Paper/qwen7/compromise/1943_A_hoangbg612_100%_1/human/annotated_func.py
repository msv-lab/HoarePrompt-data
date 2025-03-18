#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. Each test case consists of n (1 ≤ n ≤ 2 ⋅ 10^5) and an array a of n integers where 0 ≤ a_i < n. The sum of all n values across all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: After all iterations of the loop have finished, the variable `cur` will be set to the highest value present in the list `N` for each iteration, and the dictionary `M` will only contain keys that are present in `N` with a count of 1. The list `N` remains a non-empty list of integers sorted in ascending order. The variable `T` is decreased by the total number of iterations the loop executed. If the sum of all values in `M` equals `S`, `cur` is increased by 1; otherwise, no changes are made to `cur` and `M`. The list `cnt` will contain all keys `k` from the dictionary `M` where `M[k]` equals 1, in the order they were added. If `len(cnt)` is greater than or equal to 2, `cur` is set to the second element in the list `cnt`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer T, an integer N, and an array of N integers. For each test case, it sorts the array, counts the occurrences of each unique integer, and determines a specific value based on certain conditions. Finally, it prints the determined value for each test case.

