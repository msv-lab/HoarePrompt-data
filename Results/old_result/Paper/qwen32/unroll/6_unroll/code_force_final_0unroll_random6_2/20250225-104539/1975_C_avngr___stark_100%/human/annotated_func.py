#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500. For each test case, n is an integer such that 2 <= n <= 10^5, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^9. The sum of n over all test cases does not exceed 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        if n == 2:
            print(min(a))
            continue
        
        max = 0
        
        for i in range(n - 2):
            temp = a[i:i + 3]
            temp.sort()
            if temp[1] > max:
                max = temp[1]
        
        print(max)
        
    #State: For each test case, the output is the maximum value among the medians of all contiguous subarrays of length 3 in the list `a`. If `n` is 2, the output is the minimum value in the list `a`. The variable `t` remains unchanged, and `n` and `a` are re-assigned for each test case but are not retained after the loop.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of an integer `n` and a list `a` of `n` integers. For each test case, if `n` is 2, it outputs the minimum value in the list `a`. Otherwise, it finds and outputs the maximum median value among all contiguous subarrays of length 3 in the list `a`.

