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
        
    #State: The output state after the loop executes all the iterations is a string containing the elements of the list `a` separated by spaces, where `a` is calculated based on the input values of `n` and the list `T`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a positive integer `t` (number of test cases), an integer `n` (number of elements in the list `x` + 1), and a list `x` of `n-1` integers. For each test case, it calculates a new list `a` based on the input values and prints a string containing the elements of `a` separated by spaces.

