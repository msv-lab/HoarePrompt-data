#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. Each test case consists of four integers n, f, a, and b where 1 ≤ n ≤ 2 × 10^5, 1 ≤ f, a, b ≤ 10^9, representing the number of messages, the initial phone's charge, the charge consumption per unit of time, and the consumption when turned off and on sequentially, respectively. Additionally, there is a list of n integers m_1, m_2, ..., m_n where 1 ≤ m_i ≤ 10^9 and m_i < m_{i+1}, representing the moments at which messages need to be sent. The sum of n over all test cases does not exceed 2 × 10^5.
def func():
    test_cases = int(input())
    for i in range(test_cases):
        feat = [int(i) for i in input().split(' ')]
        
        n = feat[0]
        
        f = feat[1]
        
        a = feat[2]
        
        b = feat[-1]
        
        arr = [int(i) for i in input().split(' ')]
        
        array2 = []
        
        for i in range(1, n):
            if arr[i] - arr[i - 1] < b / a:
                array2.append((arr[i] - arr[i - 1]) * a)
        
        if sum(array2) + (n - len(array2)) * b < f:
            print('Yes')
        else:
            print('No')
        
    #State: After the loop executes all its iterations, `i` will have iterated through all values from 0 to `test_cases - 1`. For each iteration, `feat` will be updated with the new input values, and `n`, `f`, `a`, and `b` will be set based on the current `feat`. The list `arr` will be populated with the new input values for each test case. The list `array2` will be recalculated for each test case, containing the values `(arr[j] - arr[j-1]) * a` for all `j` in the range `[1, n-1]` where the condition `(arr[j] - arr[j-1]) < b / a` is true. The final output for each test case will be 'Yes' if the sum of the elements in `array2` plus the product of `(n - len(array2))` and `b` is less than `f`, otherwise 'No'. The variable `t` remains unchanged and still satisfies 1 ≤ t ≤ 10^4.
#Overall this is what the function does:The function `func` reads multiple test cases, each consisting of the number of messages `n`, the initial phone's charge `f`, the charge consumption per unit of time `a`, the charge consumption when turning the phone off and on `b`, and a list of moments `m_1, m_2, ..., m_n` when messages need to be sent. For each test case, it calculates whether the phone can send all messages without running out of charge. If the total charge required to send all messages (considering both continuous usage and turning the phone off and on) is less than the initial charge `f`, it prints 'Yes'; otherwise, it prints 'No'. The function processes all test cases and prints the result for each one. The variable `t` (number of test cases) remains unchanged throughout the function's execution.

