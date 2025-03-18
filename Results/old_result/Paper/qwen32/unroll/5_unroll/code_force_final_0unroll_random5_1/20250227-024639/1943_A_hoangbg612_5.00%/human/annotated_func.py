#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 2 · 10^4) representing the number of test cases. For each test case, the first line contains a single integer n (1 ≤ n ≤ 2 · 10^5) representing the size of the array a. The second line contains n integers a_1, a_2, ..., a_n (0 ≤ a_i < n) representing the elements of the array a. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: a series of integers, each representing the final value of `cur` for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and an array `a` of `n` integers. For each test case, it calculates and prints a value `cur` which represents the smallest integer such that the number of elements in the array less than or equal to `cur` is at least `cur+1`.

