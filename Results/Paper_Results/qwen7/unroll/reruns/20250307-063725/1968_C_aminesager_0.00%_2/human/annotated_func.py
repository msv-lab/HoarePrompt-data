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
        
    #State: The output state will be a list of integers, each calculated based on the initial value of `t`, which ranges from 1 to 10^4. The list will start with 1000 and decrease by the corresponding values from the input list `T` in reverse order.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `t` (1 ≤ t ≤ 10^4), an integer `n` (2 ≤ n ≤ 500), and a list `x` of `n-1` integers (1 ≤ x_i ≤ 500 for all 2 ≤ i ≤ n). For each test case, it calculates a list starting with 1000 and decreases by the corresponding values from the input list `x` in reverse order. Finally, it prints the resulting list as a space-separated string.

