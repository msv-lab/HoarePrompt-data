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
        
    #State: After all iterations of the loop, `t` is 0, and for each test case, `n` was an input integer, `a` was a list of integers from user input, `i` reached `n-1`, and `max` was the maximum value among all the minimum values of pairs `(a[j], a[j-1])` for `j` in the range `[1, n-1]` for each test case.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. For each test case, it reads an integer `n` and a list `a` of `n` integers. It then finds the maximum value among the minimum values of consecutive pairs in the list `a`. Finally, it prints this maximum value for each test case. The function does not return any value; it only prints the results to the standard output. After processing all test cases, the function completes its execution.

