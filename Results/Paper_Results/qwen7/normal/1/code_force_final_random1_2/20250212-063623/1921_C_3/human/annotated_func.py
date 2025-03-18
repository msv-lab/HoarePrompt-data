#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, f, a, and b are integers such that 1 ≤ n ≤ 2 ⋅ 10^5, 1 ≤ f, a, b ≤ 10^9. Additionally, m_1, m_2, ..., m_n are integers such that 1 ≤ m_i ≤ 10^9 and m_i < m_{i+1}.
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
        
    #State: Output State: After the loop executes all the iterations, `i` will be equal to `test_cases`, `array2` will contain the product `(arr[i] - arr[i - 1]) * a` for every index `i` in the range from 1 to `n-1` where the difference `arr[i] - arr[i - 1]` is less than the ratio `b / a`. The final output will be 'Yes' if the sum of the elements in `array2` plus `(n - len(array2)) * b` is less than `f`, otherwise it will be 'No'.
    #
    #This means that after all iterations of the loop, the variable `i` will have reached the value of `test_cases`, indicating that the loop has completed all its iterations. The list `array2` will hold the calculated values based on the condition specified within the inner loop. Finally, the program will print 'Yes' or 'No' based on the comparison between the sum of `array2` and the adjusted value of `f`.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads integers n, f, a, b, and a list of n integers. It then calculates the difference between consecutive elements in the list and checks if this difference is less than the ratio b/a. If the difference is less, it multiplies the difference by a and adds the result to a new list. Finally, it compares the sum of the new list with the adjusted value of f (which is f minus the number of elements in the new list times b). If the sum is less than f, it prints 'Yes'; otherwise, it prints 'No'.

