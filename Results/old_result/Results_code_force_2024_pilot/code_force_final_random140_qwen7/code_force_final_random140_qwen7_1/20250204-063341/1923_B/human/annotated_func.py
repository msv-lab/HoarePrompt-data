#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 3 ⋅ 10^5 and 1 ≤ k ≤ 2 ⋅ 10^9; a is a list of n integers where 1 ≤ a_i ≤ 10^9; b is a list of n+1 integers initialized to 0, and for each i (0 ≤ i ≤ n), b[abs(x_i)] += a_i, where x_i is an integer such that -n ≤ x_i ≤ n and x_i ≠ 0.
def func_1():
    try:
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = [0] * (n + 1)
        for i in range(n):
            x = int(input())
            
            b[abs(x)] += a[i]
            
        #State: Output State: After the loop executes all the iterations, `i` will be equal to `n`, `n` must be greater than 0, `x` will be the last input integer provided, and `b[abs(x)]` will be increased by `a[n-1]`.
        #
        #In more detail, the loop runs from `i = 0` to `i = n-1`. After all iterations, the final value of `i` will be `n`. During each iteration, the value of `x` is taken as input and `b[abs(x)]` is incremented by the corresponding element in list `a`. Therefore, the final state of the list `b` will have its elements updated based on the absolute values of the inputs provided and the values in list `a`.
        r = 0
        for i in range(1, n + 1):
            r += k
            
            if r < b[i]:
                print('NO')
                return
            
            r -= b[i]
            
        #State: Output State: After the loop executes all its iterations, `i` will be equal to `n`, `n` must be greater than 0, `r` will be the initial value of `r` minus the sum of all elements in the list `b` from index 1 to `n`.
        #
        #Explanation: The loop runs from `i = 1` to `i = n`. In each iteration, `r` is decreased by the value of `b[i]`. Therefore, after all iterations, `r` will be the initial value of `r` minus the sum of all elements in `b` from index 1 to `n`.
        print('YES')
        #This is printed: YES
    except (ValueError):
        print('Invalid input format')
        #This is printed: Invalid input format
    #State: `n` and `k` are integers, `a` is a list of `n` integers, and `b` is a list of `n+1` integers initialized to 0. After the loop executes all its iterations, `r` will be the initial value of `r` minus the sum of all elements in the list `b` from index 1 to `n`. If the input format is invalid, the function prints 'Invalid input format' and returns.
#Overall this is what the function does:The function processes two lists, `a` and `b`, based on user inputs for `n` and `k`. It reads `n` integers into list `a` and `n+1` integers into list `b`. For each integer `x` read, it updates `b[abs(x)]` by adding the corresponding element from `a`. After processing, it calculates a running total `r` starting from `k`, subtracting the values in `b` from `r` up to `n`. If at any point `r` becomes less than the current value in `b`, it prints 'NO' and exits. Otherwise, it prints 'YES'. If the input format is invalid, it prints 'Invalid input format'. The function does not return any value.

#State of the program right berfore the function call: t is an integer representing the number of test cases; n and k are integers for each test case where 1 ≤ n ≤ 3 ⋅ 10^5 and 1 ≤ k ≤ 2 ⋅ 10^9; a_i and x_i are integers for each monster where 1 ≤ a_i ≤ 10^9 and -n ≤ x_1 < x_2 < ... < x_n ≤ n with x_i ≠ 0.
def func_2():
    try:
        t = int(input())
        for _ in range(t):
            func_1()
            
        #State: Output State: `t` must be greater than or equal to the total number of iterations.
        #
        #Natural Language Description: After the loop executes all its iterations, the variable `t` must be greater than or equal to the total number of iterations because the loop continues as long as `t` is greater than 0. Since the loop runs up to the third iteration with the given conditions, `t` must initially be at least 3 to allow for all iterations to complete.
    except (ValueError):
        print('Invalid input format')
        #This is printed: Invalid input format
    #State: `t` is an integer, and it must be greater than or equal to the total number of iterations. If the input is not a valid integer, the function prints 'Invalid input format' and returns None.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `t` (representing the number of test cases), followed by pairs of integers `n` and `k`, and lists of integers `a_i` and `x_i`. If the input is valid, it executes a series of operations defined within `func_1()` for each test case. If the input is invalid (i.e., not a valid integer), it prints 'Invalid input format' and returns `None`. The function ensures that `t` is an integer and is greater than or equal to the total number of iterations, allowing all test cases to be processed.

