#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 2 <= n <= 500, and x is a list of n-1 integers where each element x_i satisfies 1 <= x_i <= 500. The sum of all n values across all test cases does not exceed 2 * 10^5.
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
        
    #State: The output state consists of the printed results for each test case, where each result is a space-separated string of integers representing the reversed list `a` for that test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list of `n-1` integers. It then calculates and prints a list of `n` integers in reverse order, where each integer is determined based on the differences between consecutive elements in the input list.

