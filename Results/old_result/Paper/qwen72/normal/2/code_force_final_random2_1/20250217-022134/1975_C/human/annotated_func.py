#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 500, representing the number of test cases. For each test case, n is an integer where 2 ≤ n ≤ 10^5, representing the length of the array a. a is a list of n integers where 1 ≤ a_i ≤ 10^9, representing the elements of the array a. The sum of n over all test cases does not exceed 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        max = 0
        
        for i in range(1, n):
            if min(a[i], a[i - 1]) > max:
                max = min(a[i], a[i - 1])
        
        print(max)
        
    #State: After all iterations of the loop, `t` is greater than 0, `n` is an input integer, `a` is a list of integers provided by the user, `i` is `n-1`, and `max` is the maximum of the minimum values found between consecutive elements in the list `a` from index 1 to `n-1` for each test case.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. It then finds the maximum value among the minimums of consecutive pairs in the list `a` and prints this value. After processing all test cases, the function has no return value, but it has printed the maximum of the minimums for each test case. The final state of the program includes the processed test cases and the printed results.

