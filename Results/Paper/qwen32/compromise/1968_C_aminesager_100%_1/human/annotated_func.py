#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each test case consists of an integer n (2 <= n <= 500) and a list of n-1 integers x_2, x_3, ..., x_n (1 <= x_i <= 500). The sum of all n values across test cases does not exceed 2 * 10^5.
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
        
    #State: `t` is 0, `n` is the integer value provided by user input in the last iteration (2 <= n <= 500), `T` is the list of integers derived from splitting the string `line` in the last iteration, `a` is `[1000, 1000 + T[0], (1000 + T[0]) + T[1], ..., 1000 + sum(T[0] to T[n-2])]`, and `result` is the space-separated string of the elements in `a` from the last iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list of `n-1` integers. For each test case, it calculates a new list where each element is the cumulative sum starting from 1000, adding each integer from the input list sequentially. It then prints this new list as a space-separated string for each test case.

