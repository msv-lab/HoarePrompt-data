#State of the program right berfore the function call: The function `func` is expected to handle multiple test cases. Each test case includes an integer `n` (2 ≤ n ≤ 500) representing the number of elements in the array `a`, and a list of integers `x` (1 ≤ x_i ≤ 500) of length `n-1` representing the remainders. The total number of test cases `t` is a positive integer (1 ≤ t ≤ 10^4), and the sum of all `n` values across test cases does not exceed 2 · 10^5.
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
        
    #State: `t` is 0, `n` is an input integer greater than 1, `T` is a list of integers derived from the input string `line` by splitting it and converting each element to an integer, `a` is a list containing the integers 1000 and the cumulative sums of the first `n-1` elements of `T`, `i` is `n - 1`, `result` is a string containing the elements of `a` separated by spaces.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads an integer `n` and a list of integers `x` of length `n-1`. It then constructs a list `a` starting with the integer 1000, followed by the cumulative sums of the elements in `x`. The function prints the elements of `a` as a space-separated string. After processing all test cases, the function terminates with `t` being 0.

