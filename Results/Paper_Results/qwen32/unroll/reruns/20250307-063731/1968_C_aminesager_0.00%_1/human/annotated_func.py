#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, the first line contains an integer n (2 ≤ n ≤ 500) representing the number of elements in the array a. The second line contains n-1 integers x_2, x_3, ..., x_n (1 ≤ x_i ≤ 500) representing the elements of the array x. The sum of all n values across all test cases does not exceed 2 × 10^5.
def func():
    t = int(input())
    while t:
        t = t - 1
        
        n = int(input())
        
        line = input('')
        
        T = list(map(int, line.split()))
        
        a = [1000]
        
        for i in range(1, n):
            a.append(a[i - 1] - T[i - 1])
        
        a = a[::-1]
        
        result = ' '.join(map(str, a))
        
        print(result)
        
    #State: t is 0.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list of `n-1` integers. It computes and prints an array `a` of length `n` for each test case, where each element of `a` is derived from the input integers in a specific manner.

