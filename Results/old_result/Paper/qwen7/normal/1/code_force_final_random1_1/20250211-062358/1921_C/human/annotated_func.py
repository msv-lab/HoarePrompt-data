#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, f, a, and b are integers such that 1 ≤ n ≤ 2·10^5, 1 ≤ f, a, b ≤ 10^9. The list m contains n integers such that 1 ≤ m_i ≤ 10^9 and m_i < m_{i+1}.
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
        
    #State: Output State: After the loop executes all the iterations, `i` will be equal to `test_cases`, which is the total number of test cases. The variable `n` will be the value of `feat[0]` for the last test case, and it must be an integer within the range `1` to `10^4`. The variable `f` will be the value of `feat[1]` for the last test case, `a` will be the value of `feat[2]` for the last test case, and `b` will be the value of `feat[-1]` for the last test case. `arr` will be a list of integers obtained from the input for the last test case, split by spaces and converted to integers. `array2` will be a list containing elements where each element is `(arr[j] - arr[j - 1]) * a` for every `j` in the range from `3` to `n-1` inclusive, provided that `arr[j] - arr[j - 1] < b / a`. The final output will be 'Yes' if the sum of `array2` plus `(n - len(array2)) * b` is less than `f` for the last test case; otherwise, the output will be 'No'.
    #
    #This means that after processing all the test cases, the loop will have iterated through all the inputs, and the final decision ('Yes' or 'No') will be based on the conditions evaluated for the last test case.
#Overall this is what the function does:The function processes a series of test cases, each consisting of integers \( n \), \( f \), \( a \), and \( b \), along with a list of \( n \) integers. For each test case, it calculates whether the sum of certain adjusted differences between consecutive elements in the list, plus a linear term, is less than \( f \). If true for the last test case, it prints 'Yes'; otherwise, it prints 'No'.

