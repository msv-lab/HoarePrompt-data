#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 500, and x is a list of n-1 integers where 1 ≤ x_i ≤ 500 for all 2 ≤ i ≤ n.
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
        
    #State: Output State: The loop will continue to execute until `t` becomes 0. After all iterations, `t` will be `0`. For each iteration, `n` will be set to a new input value, and `a` will be updated based on the new `n` and the input list `T`. The final `result` will be a string containing the cumulative sums starting from 1000 for each `n` in the form of space-separated integers. Each `result` string corresponds to one iteration and will be printed during that iteration.
    #
    #Since the loop runs until `t` becomes 0, the final output state will be determined by the last value of `n` and the corresponding list `T`. The `result` will be the cumulative sums starting from 1000 for the last `n`, and this will be the last string printed. All previous `result` strings will also be part of the output, each corresponding to the respective `n` and `T` values from earlier iterations.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a positive integer `t` (indicating the number of test cases), an integer `n` (the size of the subsequent list), and a list `T` of `n-1` integers. For each test case, it calculates a list `a` where each element is the cumulative sum starting from 1000. It then prints a string of these cumulative sums in space-separated format for each test case. The function does not return any value but prints the results for each test case.

