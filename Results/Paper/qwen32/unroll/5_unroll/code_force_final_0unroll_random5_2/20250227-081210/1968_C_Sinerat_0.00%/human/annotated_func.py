#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, the input includes an integer n (2 ≤ n ≤ 500) representing the number of elements in array a, followed by n-1 integers x_2, x_3, ..., x_n (1 ≤ x_i ≤ 500) representing the elements of array x. The sum of all n values across all test cases does not exceed 2 * 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 500
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: For each test case, the output is an array `a` of size `n` where `a[0] = 500` and `a[i] = a[i-1] + x[i-1]` for `i` from 1 to `n-1`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and `n-1` integers. For each test case, it constructs and prints an array `a` of size `n` where the first element is 500, and each subsequent element is the sum of the previous element in `a` and the corresponding element in the input array `x`.

