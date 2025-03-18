#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2 · 10^5, f, a, and b are integers such that 1 ≤ f, a, b ≤ 10^9, and m_1, m_2, ..., m_n are integers such that 1 ≤ m_i ≤ 10^9 and m_i < m_{i + 1}. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The values of `t`, `n`, `f`, `a`, `b`, and `m_1`, `m_2`, ..., `m_n` remain unchanged. The loop has executed `test_cases` times, and for each test case, it has either printed 'Yes' or 'No' based on the conditions specified in the loop.
#Overall this is what the function does:The function reads multiple test cases from the input, where each test case consists of an integer `n`, an integer `f`, two integers `a` and `b`, and a list of `n` integers `arr`. For each test case, the function checks if the sum of certain calculated values (based on the elements of `arr` and the constants `a` and `b`) plus a fixed cost is less than `f`. If the condition is met, it prints 'Yes'; otherwise, it prints 'No'. The function does not return any value. After processing all test cases, the values of `t`, `n`, `f`, `a`, `b`, and the elements of `arr` remain unchanged.

