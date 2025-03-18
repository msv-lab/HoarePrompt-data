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
            a.append(a[i - 1] + T[i - 1])
        
        result = ' '.join(map(str, a))
        
        print(result)
        
    #State: Output State: The loop will continue to execute until `t` becomes 0. After all iterations of the loop have finished, `t` will be 0. For each iteration, `n` will be set to the value of an integer input, `i` will reach the value of `n`, and `a` will be a list where each element is the cumulative sum of the first `i-1` elements from the list `T`. The `result` will be a string containing the cumulative sums separated by spaces for each value of `n` processed during the loop iterations.
    #
    #Since the loop runs until `t` becomes 0, the final state will have `t` as 0, and `result` will contain the cumulative sums for all the `n` values provided by the user during the loop iterations, each separated by spaces and listed sequentially.
#Overall this is what the function does:The function processes a series of test cases defined by the variable `t`. For each test case, it reads two integers `n` and `x`, where `n` represents the number of elements in a sequence and `x` is a list of `n-1` integers. It then calculates the cumulative sum of the sequence starting from 1000 and appends each sum to a list `a`. Finally, it prints the list `a` as a space-separated string for each test case. After processing all test cases, the function outputs the cumulative sums for all provided sequences.

