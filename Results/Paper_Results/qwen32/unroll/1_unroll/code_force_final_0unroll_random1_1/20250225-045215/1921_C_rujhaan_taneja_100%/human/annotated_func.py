#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, f, a, and b are integers such that 1 <= n <= 2 * 10^5, 1 <= f, a, b <= 10^9. m is a list of n integers such that 1 <= m_i <= 10^9 and m_i < m_{i+1}. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: For each test case, the code prints either 'Yes' or 'No' based on the condition that if the sum of the calculated values in `array2` plus the product of the difference between `n` and the length of `array2` and `b` is less than `f`. The variables `t`, `test_cases`, and the input values for each test case remain unchanged after the loop finishes executing.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers `n`, `f`, `a`, `b`, and a list `m` of `n` integers. For each test case, it calculates a sum based on the differences in the list `m` and compares it to `f`. It prints 'Yes' if the calculated sum plus a penalty term is less than `f`, otherwise it prints 'No'. The input values remain unchanged after processing each test case.

