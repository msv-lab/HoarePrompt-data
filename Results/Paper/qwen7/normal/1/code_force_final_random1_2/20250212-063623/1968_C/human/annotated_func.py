#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 500, and x is a list of n-1 integers where 1 ≤ x_i ≤ 500 for all 2 ≤ i ≤ n.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 1000
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: i is equal to `n-1`, `a` is a list of `n` elements where each element `a[j]` (for `j` from 0 to `n-1`) is calculated as `a[j] = 1000 + sum(x[k] for k in range(j+1))`, and `n` retains its value as it was last updated via user input.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `t` (number of test cases), an integer `n` (length of the list `x` + 1), and a list `x` of `n-1` integers. It then calculates a list `a` of length `n` where each element `a[j]` is the sum of 1000 and the first `j+1` elements of `x`. Finally, it prints the list `a` for each test case.

