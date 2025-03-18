#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 500, and x is a list of n-1 integers where 1 ≤ x_i ≤ 500 for all 2 ≤ i ≤ n.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 500
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: After the loop executes all its iterations, the variable `i` will be equal to `n`, the list `a` will contain `n` elements where each element `a[i]` (for `i` from 0 to `n-1`) will be the cumulative sum of the first `i+1` elements of the list `x`, starting with `a[0] = 500`. The variable `n` will remain unchanged, and the list `x` will also remain unchanged.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `n` and a list `x` of `n-1` integers. It then calculates a new list `a` where each element `a[i]` (for `i` from 0 to `n-1`) is the cumulative sum of the first `i+1` elements of `x`, starting with `a[0] = 500`. Finally, it prints the list `a` for each test case. The function does not return any value but modifies and prints the cumulative sums based on the input lists.

