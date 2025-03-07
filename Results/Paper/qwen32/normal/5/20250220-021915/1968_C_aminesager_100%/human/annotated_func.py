#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, there are two lines: the first line contains an integer n (2 ≤ n ≤ 500) representing the number of elements in the array a, and the second line contains n-1 integers x_2, x_3, ..., x_n (1 ≤ x_i ≤ 500) representing the elements of the array x. The sum of all n values across all test cases does not exceed 2 * 10^5.
def func():
    t = int(input())
    while t:
        t = t - 1
        
        n = int(input())
        
        line = input('')
        
        T = list(map(int, line.split()))
        
        a = [1000]
        
        for i in range(1, n):
            a.append(a[i - 1] + T[i - 1])
        
        result = ' '.join(map(str, a))
        
        print(result)
        
    #State: `t` is 0, `n` is the integer from the last test case input, `T` is a list of integers derived from splitting and converting the last input string `line`, `a` is a list containing the integers 1000, 1000 + T[0], 1000 + T[0] + T[1], ..., 1000 + T[0] + T[1] + ... + T[n-2] + T[n-1], `i` is `n`, `result` is a space-separated string representation of the list `a`.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and a list of `n-1` integers. It constructs an array `a` of length `n` by setting the first element to 1000 and each subsequent element to the sum of the previous element in `a` and the corresponding element in the input list. It then prints the resulting array `a` for each test case.

