#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500; for each test case, n is an integer such that 4 <= n <= 100; the second line of each test case contains n integers a_1, a_2, ..., a_n such that -10^6 <= a_i <= 10^6.
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
        
    #State of the program after the  for loop has been executed: `t` is the number of iterations the loop has executed, `results` is a list containing the values `4 * (max_val - min_val)` for each iteration, `idx` is equal to its original value plus `t` times `(1 + n)`, `n` is the `n` value from the last iteration, `a` is a list of integers derived from `data[idx + (t-1)*n:idx + t*n]` and contains at least one element, `min_val` is the minimum value in the list `a`, `max_val` is the maximum value in the list `a`, and `max_expression_value` is `4 * (max_val - min_val)`.
    print('\n'.join(map(str, results)))
#Overall this is what the function does:The function processes `t` test cases, each consisting of an integer `n` followed by `n` integers `a_1, a_2, ..., a_n`. For each test case, it calculates the expression `4 * (max_val - min_val)`, where `max_val` is the maximum value and `min_val` is the minimum value in the list `a`. The function collects these calculated values in a list `results`. After processing all test cases, it prints each value in `results` on a new line. Potential edge cases include scenarios where `t` is 1 or where `n` is the minimum allowed value (i.e., 4). If the input does not follow the specified format, the function may behave unpredictably due to the assumptions made about the structure of `data`. The function does not handle missing or invalid input values explicitly.

