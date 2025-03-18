#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. Each test case consists of four integers n, f, a, and b such that 1 ≤ n ≤ 2 · 10^5, 1 ≤ f, a, b ≤ 10^9, representing the number of messages, the initial phone's charge, the charge consumption per unit of time, and the consumption when turned off and on sequentially, respectively. Each test case also includes a list of n integers m_1, m_2, ..., m_n such that 1 ≤ m_i ≤ 10^9 and m_i < m_{i + 1}, representing the moments at which messages need to be sent. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop iterates through each test case, and for each test case, it determines whether the phone can send all messages without running out of charge. If the total charge consumption (considering both continuous usage and the cost of turning the phone on and off) is less than the initial charge `f`, it prints 'Yes'. Otherwise, it prints 'No'. The variables `t` and `test_cases` remain unchanged, and the loop does not modify the input values for each test case.
#Overall this is what the function does:The function reads the number of test cases `t` and, for each test case, it reads the number of messages `n`, the initial phone charge `f`, the charge consumption per unit of time `a`, the charge consumption when the phone is turned off and on sequentially `b`, and a list of moments `messages` at which messages need to be sent. It then determines whether the phone can send all messages without running out of charge. If the total charge consumption (considering both continuous usage and the cost of turning the phone on and off) is less than the initial charge `f`, it prints 'Yes'. Otherwise, it prints 'No'. The function does not return any value. After the function concludes, the variables `t` and `test_cases` remain unchanged, and the input values for each test case are not modified.

