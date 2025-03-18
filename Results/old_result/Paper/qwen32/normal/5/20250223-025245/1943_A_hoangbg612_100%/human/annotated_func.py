#State of the program right berfore the function call: Each test case consists of two lines. The first line contains an integer n (1 ≤ n ≤ 2 ⋅ 10^5) representing the size of the array a. The second line contains n integers a_1, a_2, ..., a_n (0 ≤ a_i < n) representing the elements of the array a. The sum of n over all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: - `cur` is the second element in `cnt` if the length of `cnt` is at least 2, otherwise `cur` is incremented by 1 if the sum of the values in `M` is equal to `S`, otherwise `cur` remains unchanged.
    #- `M` is a dictionary with keys as numbers from `N` and values as their respective counts.
    #- `cnt` is a list of integers.
    #- `S` is the input integer.
    #- `T` remains unchanged.
    #- `N` is a sorted list of integers from the input.
    #
    #Given the pattern observed, the final output state after all iterations will be the same as the output state after the last iteration, which we can deduce from the third iteration's output state as a representative.
    #
    #Output State:
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `S` and a list of integers `N`. It then determines a value `cur` based on the sorted list `N` and the integer `S`. The final output for each test case is the value of `cur`.

