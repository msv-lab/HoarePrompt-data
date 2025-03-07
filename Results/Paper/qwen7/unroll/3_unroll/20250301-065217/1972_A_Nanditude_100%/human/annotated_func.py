#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100. For each test case, n is a positive integer such that 1 ≤ n ≤ 100. a and b are lists of integers of length n, where a and b are sorted in non-decreasing order. Each element in a and b is a positive integer such that 1 ≤ a_i, b_i ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        b = list(map(int, input().split()))
        
        cnt = 0
        
        i = 0
        
        for j in range(n):
            if b[j] < a[i]:
                cnt += 1
            else:
                i += 1
        
        print(cnt)
        
    #State: Output State: t is an integer between 1 and 100 inclusive. For each iteration of the outer loop, n is an integer, a is a list of integers, and b is a list of integers. After all iterations, cnt is the sum of counts where elements in list b are less than the corresponding elements in list a, across all iterations.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads two lists of integers, `a` and `b`, both of length `n` and sorted in non-decreasing order. It then counts how many times an element in list `b` is less than the corresponding element in list `a`. Finally, it prints the count for each test case.

