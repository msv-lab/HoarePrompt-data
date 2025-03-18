#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 2 <= n <= 500 for each test case, and x is a list of n-1 integers where 1 <= x_i <= 500.
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
        
    #State: `t` is 0, `n` is an input integer such that 2 <= n <= 500, `x` is a list of n-1 integers where 1 <= x_i <= 500, `line` is a string input provided by the user, `T` is a list of integers obtained by splitting the string `line` and converting each element to an integer, `a` is a list containing the integers 1000, 1000 + T[0], 1000 + T[0] + T[1], ..., 1000 + T[0] + T[1] + ... + T[n-2], `i` is n-1, `result` is a string of the elements in `a` separated by spaces.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads another integer `n` and a space-separated list of `n-1` integers. It then calculates a new list `a` where each element is the cumulative sum of the input list elements starting from 1000. Finally, it prints the elements of `a` as a space-separated string. After the function concludes, `t` is 0, and the program state includes the printed results for each test case.

