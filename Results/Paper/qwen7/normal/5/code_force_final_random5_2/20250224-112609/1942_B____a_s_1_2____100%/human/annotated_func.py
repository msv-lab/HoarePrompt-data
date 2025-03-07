#State of the program right berfore the function call: t is a positive integer representing the number of test cases, and for each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5, and a is a list of n integers where -n ≤ a_i ≤ n.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        p = [-1] * n
        
        mex = n
        
        for i in range(n - 1, -1, -1):
            p[i] = mex - a[i]
            mex = min(mex, p[i])
        
        print(*p)
        
    #State: Output State: After the loop executes all its iterations, `i` will be `-1`, `mex` will hold the minimum value among all elements in the list `p`, and `p` will be updated such that each element `p[i]` is equal to `mex - a[i]` for its respective index `i`.
    #
    #In simpler terms, after the loop runs through all test cases (`t` times), the final state of the variables will be:
    #- `i` will be `-1` since the loop decrements `i` from `n-1` to `0` and then stops.
    #- `mex` will be the smallest value found in the list `p` after processing all elements.
    #- The list `p` will contain values such that each `p[i]` equals `mex - a[i]` for its respective index `i`.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer n and a list of n integers a. It then updates a list p such that each element p[i] is calculated as mex - a[i], where mex is the minimum value found in the updated list p. After processing all test cases, the function prints the updated list p for each test case.

