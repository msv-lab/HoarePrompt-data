#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer such that 1 ≤ n ≤ 2 · 10^5, f is an integer such that 1 ≤ f ≤ 10^9, a is an integer such that 1 ≤ a ≤ 10^9, b is an integer such that 1 ≤ b ≤ 10^9, and m_1, m_2, ..., m_n are integers such that 1 ≤ m_i ≤ 10^9 and m_i < m_{i + 1}. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The value of `t` and `test_cases` remains unchanged. For each test case, the values of `n`, `f`, `a`, and `b` are processed, and the list `arr` is read. The list `array2` is populated based on the conditions within the loop. After processing all test cases, the loop prints 'Yes' or 'No' for each test case based on the final conditions. The state of `feat`, `arr`, and `array2` is reset for each test case.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by integers `n`, `f`, `a`, `b`, and a sorted list of integers `m_1, m_2, ..., m_n`. For each test case, it calculates a list `array2` based on the differences between consecutive elements in the list `arr` and the values of `a` and `b`. It then checks if the sum of the elements in `array2` plus the product of the remaining elements in `arr` and `b` is less than `f`. If the condition is met, it prints 'Yes'; otherwise, it prints 'No'. The function does not return any value; it only prints the results for each test case. After processing all test cases, the function concludes, and the state of `test_cases` remains unchanged.

