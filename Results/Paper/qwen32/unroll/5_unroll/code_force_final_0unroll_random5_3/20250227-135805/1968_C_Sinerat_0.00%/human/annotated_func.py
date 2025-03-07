#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (2 ≤ n ≤ 500) representing the number of elements in the array a. The next line contains n-1 integers x_2, x_3, ..., x_n (1 ≤ x_i ≤ 500) which are the elements of the array x. The total number of elements in all test cases combined does not exceed 2 * 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 500
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: The output state consists of the printed arrays `a` for each test case, with no retained state of variables `n`, `x`, and `a` after the loop finishes.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it constructs and prints an array `a` of length `n` where the first element is 500 and each subsequent element is the sum of the previous element in `a` and the corresponding element in the input array `x`.

