#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2 ⋅ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and a is a list of n integers where each element a_i satisfies 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: the final value of `cur` after the last iteration of the outer loop.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it takes an integer `n` and a list `a` of `n` integers where each element is between 0 and `n-1`. It then computes and prints a value based on the sorted list and the given integer `n`. The printed value represents the smallest integer `cur` such that the number of elements in the list less than or equal to `cur` is at least `cur + 1`.

