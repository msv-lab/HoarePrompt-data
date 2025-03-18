#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 500, and x is a list of n-1 integers such that 1 ≤ x_i ≤ 500 for all 2 ≤ i ≤ n.
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
        
    #State: Output State: The loop has completed all its iterations, so `t` is now 0. The variable `n` must be greater than 0, and `x` remains unchanged from its initial state. The variable `line` remains as the input string from the last iteration, and `T` remains as the list of integers obtained from splitting `line` by spaces and converting each element to an integer. The list `a` is a reversed list starting with the value 1000 followed by `n-1` elements, each being the difference between the previous element in `a` and the corresponding element in `T`. The variable `result` is a string obtained by joining the elements of the list `a` converted to strings with a space as the separator.
    #
    #In simpler terms, after all iterations of the loop, `t` is 0, `n` is some positive integer, `x` is unchanged, `line` is the input from the last iteration, `T` is the list of integers from the last input, `a` is the reversed list calculated from `T`, and `result` is the space-separated string of the elements in `a`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a positive integer `t`, an integer `n`, and a list `x` of `n-1` integers. For each test case, it calculates a reversed list `a` starting with 1000, where each subsequent element is the difference between the previous element and the corresponding element in `x`. It then prints a space-separated string of the elements in `a`. After processing all test cases, the function outputs the results for each case.

