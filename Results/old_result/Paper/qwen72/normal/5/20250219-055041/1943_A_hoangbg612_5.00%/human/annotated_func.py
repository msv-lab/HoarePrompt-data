#State of the program right berfore the function call: The function `func` is expected to be called within a context where it processes multiple test cases. Each test case includes an integer n (1 ≤ n ≤ 2 · 10^5) and a list of n integers a_1, a_2, ..., a_n (0 ≤ a_i < n). The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: `T` is 0, `_` is `T-1`, `S` is an input integer, `N` is a sorted list of integers provided by the user, `M` is a dictionary where each key is an integer from `N` that is exactly one more than the previous integer in the list, and the value for each key is the count of consecutive integers in `N` that are equal to the key. `cur` is the smallest index `i` in the range `[0, cur-1]` such that `M[i]` is less than or equal to `i`. If no such index exists, `cur` remains unchanged and is equal to its initial value.
#Overall this is what the function does:The function `func` processes multiple test cases, each containing an integer `S` and a list of `S` integers. It sorts the list and then constructs a dictionary `M` where each key is an integer from the list that is exactly one more than the previous integer, and the value is the count of consecutive integers equal to the key. The function then determines the smallest index `cur` such that the count of integers up to `cur` in `M` is less than or equal to `cur`. If no such index exists, `cur` is the largest integer in the list plus one. The function prints `cur` for each test case. After processing all test cases, the function terminates.

