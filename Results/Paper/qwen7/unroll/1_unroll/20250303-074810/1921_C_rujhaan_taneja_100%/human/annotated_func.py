#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, f, a, and b are integers such that 1 ≤ n ≤ 2 ⋅ 10^5, 1 ≤ f, a, b ≤ 10^9. The list m consists of n integers such that 1 ≤ m_i ≤ 10^9 and m_i < m_{i+1}.
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
        
    #State: Output State: The output state consists of a series of 'Yes' or 'No' printed for each test case based on the conditions specified in the loop. For each test case, if the sum of the adjusted values in `array2` plus the cost of the remaining elements is less than `f`, it prints 'Yes', otherwise it prints 'No'.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers \( n \), \( f \), \( a \), \( b \), and a list \( m \) of length \( n \). For each test case, it calculates whether the sum of certain adjusted values in \( m \) plus the cost of the remaining elements is less than \( f \). If true, it prints 'Yes'; otherwise, it prints 'No'. The function does not return any value explicitly but outputs 'Yes' or 'No' for each test case.

