#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. Each test case contains four integers n, f, a, b such that 1 ≤ n ≤ 2 · 10^5, 1 ≤ f, a, b ≤ 10^9, where n is the number of messages, f is the initial phone's charge, a is the charge consumption per unit of time, and b is the consumption when turned off and on sequentially. Each test case also contains n integers m_1, m_2, ..., m_n such that 1 ≤ m_i ≤ 10^9 and m_i < m_{i + 1}, representing the moments at which messages need to be sent. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
        for i in range(0, n):
            if i == 0:
                if arr[0] < b / a:
                    array2.append(arr[0] * a)
            elif arr[i] - arr[i - 1] < b / a:
                array2.append((arr[i] - arr[i - 1]) * a)
        
        if sum(array2) + (n - len(array2)) * b < f:
            print('Yes')
        else:
            print('No')
        
    #State: The loop iterates through each test case, and for each test case, it processes the input values `n`, `f`, `a`, `b`, and the array `arr`. It then calculates the cost of sending messages based on the conditions provided and prints 'Yes' if the total cost is less than `f`, otherwise it prints 'No'. The variables `t` and `test_cases` remain unchanged, as they are not modified within the loop. The variables `feat`, `n`, `f`, `a`, `b`, `arr`, and `array2` are reinitialized for each test case.
#Overall this is what the function does:The function processes multiple test cases, each containing four integers `n`, `f`, `a`, and `b`, and a list of `n` integers `m_1, m_2, ..., m_n`. For each test case, it calculates the total charge consumption required to send all messages, considering the charge consumption per unit of time `a` and the charge consumption when the phone is turned off and on sequentially `b`. It prints 'Yes' if the total charge consumption is less than or equal to the initial charge `f`, otherwise it prints 'No'. The function does not return any values; it only prints the results for each test case.

