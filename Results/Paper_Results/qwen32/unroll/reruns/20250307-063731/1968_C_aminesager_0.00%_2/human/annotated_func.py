#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (2 ≤ n ≤ 500) representing the number of elements in array a. The next line contains n-1 integers x_2, x_3, ..., x_n (1 ≤ x_i ≤ 500) representing the elements of array x. The total number of elements across all test cases does not exceed 2 * 10^5.
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
        
    #State: `t` is `0`, and the printed results for each test case are the arrays `a` in reverse order.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and `n-1` integers. It calculates and prints an array `a` of length `n` such that the difference between consecutive elements matches the given `n-1` integers in reverse order, starting with the initial element of `a` set to 1000.

