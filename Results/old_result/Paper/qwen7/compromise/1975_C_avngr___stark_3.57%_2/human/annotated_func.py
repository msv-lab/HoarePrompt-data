#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. Each test case consists of two lines: the first line contains a single integer n such that 2 ≤ n ≤ 10^5, and the second line contains n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 10^5.
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
        
    #State: Output State: After all iterations, `i` is equal to `n`, `max` contains the maximum value of the minimums between all consecutive elements in the list `a` for each of the `t` test cases, `t` is greater than 0, and `a` is a list of integers obtained from input for each test case.
    #
    #This means that after the loop has executed all its iterations, `max` will hold the highest value among all the minimum pairs of consecutive elements across all lists `a` provided by the input. The variable `t` will still be positive as it represents the number of test cases, and `a` will be the list of integers corresponding to each test case.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer n followed by n integers a_1, a_2, ..., a_n. For each test case, it finds the maximum value among all the minimum values of consecutive elements (min(a[i], a[i-1])) in the list a. After processing all test cases, it outputs this maximum value for each test case. The function does not return any value but prints the results directly.

