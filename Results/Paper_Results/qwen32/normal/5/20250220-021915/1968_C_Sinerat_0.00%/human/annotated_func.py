#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, the first line contains an integer n (2 ≤ n ≤ 500) representing the number of elements in the array a. The second line contains n-1 integers x_2, x_3, ..., x_n (1 ≤ x_i ≤ 500) representing the elements of the array x. The sum of all n over all test cases does not exceed 2 · 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 500
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: The loop will execute `t` times, where `t` is the number of test cases. For each test case, `n` is the number of elements in the array `a`, and `x` is a list of `n-1` integers. The array `a` is constructed such that `a[0]` is 500, and for each `i` from 1 to `n-1`, `a[i]` is the sum of `a[i-1]` and `x[i-1]`. After all iterations, the final output will be the printed arrays `a` for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list of `n-1` integers. For each test case, it constructs and prints an array `a` of length `n` where the first element is 500 and each subsequent element is the sum of the previous element in `a` and the corresponding element in the input list `x`.

