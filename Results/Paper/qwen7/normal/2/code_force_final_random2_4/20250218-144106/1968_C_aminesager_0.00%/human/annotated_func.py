#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 500, and x is a list of n-1 integers such that 1 ≤ x_i ≤ 500 for all 2 ≤ i ≤ n.
def func():
    t = int(input())
    while t:
        t = t - 1
        
        n = int(input())
        
        line = input('')
        
        T = list(map(int, line.split()))
        
        a = [1000]
        
        for i in range(1, n):
            a.append(a[i - 1] - T[i - 1])
        
        a = a[::-1]
        
        result = ' '.join(map(str, a))
        
        print(result)
        
    #State: Output State: The loop will continue to decrement `t` until `t` reaches 0. After all iterations, `t` will be 0, and the variable `n` will be the value it had in the last iteration of the loop. The list `a` will contain the final computed values based on the cumulative subtraction of elements in `T`. Specifically, `a` will be constructed such that each element `a[j]` (for `j` from 0 to `n-2`) represents the difference between `T[j]` and the accumulated value from previous elements in `a`.
    #
    #The `result` will be a string representation of the list `a` with elements separated by spaces. The `line` variable will hold the input string from the last iteration, and `T` will be an empty list since it gets reassigned to an empty list at the end of each iteration.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `t` (number of test cases), an integer `n` (length of the list `x` + 1), and a list `x` of `n-1` integers. It then constructs a list `a` where each element is derived from the cumulative subtraction of elements in `x`. Finally, it prints a string representation of the list `a` with elements separated by spaces. After processing all test cases, the function ends.

