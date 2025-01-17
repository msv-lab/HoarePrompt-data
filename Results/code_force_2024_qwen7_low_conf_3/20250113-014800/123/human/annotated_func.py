#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500. For each test case, n is an integer such that 4 <= n <= 100, and a is a list of n integers where -10^6 <= a_i <= 10^6.
def func_1():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    idx = 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        
        idx += 1
        
        a = list(map(int, data[idx:idx + n]))
        
        idx += n
        
        min_val = float('inf')
        
        max_val = float('-inf')
        
        for num in a:
            if num < min_val:
                min_val = num
            if num > max_val:
                max_val = num
        
        max_expression_value = 4 * (max_val - min_val)
        
        results.append(max_expression_value)
        
    #State of the program after the  for loop has been executed: `t` is an integer equal to `data[0]` and must be greater than 0, `n` is the last value of `n` set within the loop and must be between 4 and 100, `a` is a list of integers with length `0`, `idx` is the final value of `idx` which is `3 + n * t`, `results` is a list containing `max_expression_value` for each iteration, `min_val` is undefined, `max_val` is undefined, `max_expression_value` is the maximum value of `4 * (max_val - min_val)` for each iteration.
    print('\n'.join(map(str, results)))
#Overall this is what the function does:- The function assumes that the input is correctly formatted, meaning that for each test case, the integer `n` is followed by exactly `n` integers. If there are any discrepancies in the input format, the function may fail to process the input correctly.
- There is no explicit handling for the case where `n` is less than 4 or greater than 100. While the loop in the code will still execute, it is not specified what should happen if the constraints are violated.
- The function does not handle negative values of `t`. If `t` is less than 1 or greater than 500, the function will still process the input, but this might not be the intended behavior.

