#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, f, a, and b are integers such that 1 ≤ n ≤ 2⋅10^5, 1 ≤ f, a, b ≤ 10^9. Additionally, m_1, m_2, ..., m_n are integers such that 1 ≤ m_i ≤ 10^9 and m_i < m_{i+1}.
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
        
    #State: Output State: The output state consists of "Yes" or "No" printed for each test case based on the conditions inside the loop. For each test case, a list `array2` is created where elements are appended based on certain conditions involving the input arrays `arr`. If the sum of the elements in `array2` plus the product of the remaining elements with `b` is less than `f`, it prints "Yes"; otherwise, it prints "No".
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `t`, followed by `n`, `f`, `a`, and `b`, and a list of `n` integers. For each test case, it creates a new list `array2` based on certain conditions involving the input arrays. It then checks if the sum of the elements in `array2` plus the product of the remaining elements with `b` is less than `f`. If true, it prints "Yes"; otherwise, it prints "No". The function does not return any value but prints "Yes" or "No" for each test case.

