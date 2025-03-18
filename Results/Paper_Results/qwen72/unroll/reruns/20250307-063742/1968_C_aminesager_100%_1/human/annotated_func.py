#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 2 <= n <= 500, and x is a list of integers such that 1 <= x_i <= 500 for all 2 <= i <= n. The sum of values n over all test cases does not exceed 2 * 10^5.
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
        
    #State: t = 0, n = an integer such that 2 <= n <= 500, x is a list of integers such that 1 <= x_i <= 500 for all 2 <= i <= n, and the results of the loop are printed for each test case.
#Overall this is what the function does:The function `func` reads an integer `t` from user input, indicating the number of test cases. For each test case, it reads another integer `n` and a line of space-separated integers. It then computes a new list `a` where each element is the cumulative sum of the elements from the input list `T` (derived from the input line). The function prints the elements of `a` as a space-separated string for each test case. After processing all test cases, `t` is reduced to 0. The function does not return any value.

