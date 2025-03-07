#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 2 · 10^4) — the number of test cases. For each test case, the first line contains a single integer n (1 ≤ n ≤ 2 · 10^5) — the size of the array a. The second line contains n integers a_1, a_2, ..., a_n (0 ≤ a_i < n) representing the elements of the array a. It is guaranteed that the sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: the final value of `cur` after processing the last test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and an array `a` of `n` integers. For each test case, it determines and prints a specific integer `cur` based on the sorted elements of the array and their frequencies. The final output for each test case is the value of `cur` after all processing is complete.

