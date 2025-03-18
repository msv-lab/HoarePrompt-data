#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each test case starts with an integer n (2 ≤ n ≤ 500) representing the number of elements in the array a. The next line contains n-1 integers x_2, x_3, ..., x_n (1 ≤ x_i ≤ 500) representing the elements of the array x. The sum of all n over all test cases does not exceed 2 * 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 1000
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: For each test case, the output is a list of n integers where the first integer is 1000 and each subsequent integer is the sum of the previous integer in the list and the corresponding element from the input list x.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it generates and prints an array `a` of length `n`. The first element of `a` is set to 1000, and each subsequent element is the sum of the previous element in `a` and the corresponding element from the input list `x`.

