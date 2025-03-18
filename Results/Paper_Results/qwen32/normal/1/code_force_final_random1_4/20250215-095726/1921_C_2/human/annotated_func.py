#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of two lines: the first line contains four integers n, f, a, and b such that 1 ≤ n ≤ 2 · 10^5, 1 ≤ f, a, b ≤ 10^9. The second line contains n integers m_1, m_2, ..., m_n such that 1 ≤ m_i ≤ 10^9 and m_i < m_{i+1}. The sum of n across all test cases does not exceed 2 · 10^5.
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
        
    #State: After all iterations, `test_cases` remains unchanged, `t` remains unchanged, and for each test case, the program has evaluated whether the sum of `array2` plus `(n - len(array2)) * b` is less than `f`. If true, it prints "Yes"; otherwise, it prints "No".
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers and several parameters. For each test case, it calculates a value based on the differences between consecutive integers in the list and compares this value to a threshold. It prints "Yes" if the calculated value is below the threshold, otherwise it prints "No".

