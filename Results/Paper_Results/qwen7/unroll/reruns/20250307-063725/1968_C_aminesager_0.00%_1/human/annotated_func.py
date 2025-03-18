#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 500, and x is a list of n-1 integers where 1 ≤ x_i ≤ 500 for all 2 ≤ i ≤ n.
def func():
    t = int(input())
    while t:
        t = t - 1
        
        n = int(input())
        
        line = input('')
        
        T = list(map(int, line.split()))
        
        a = [1000]
        
        for i in range(1, n):
            a.append(a[i - 1] - T[i - 1])
        
        a = a[::-1]
        
        result = ' '.join(map(str, a))
        
        print(result)
        
    #State: The output state will be a series of lists, each representing the reversed cumulative subtraction of the input sequence T for each test case.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer `n`, a list `T` of `n-1` integers, and an integer `t`. For each test case, it calculates the reversed cumulative subtraction of the input sequence `T` and prints the result. After processing all test cases, the function concludes without returning any specific value.

