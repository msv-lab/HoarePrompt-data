#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. Each test case consists of an integer n (2 ≤ n ≤ 500) and a list of n-1 integers x_2, ..., x_n (1 ≤ x_i ≤ 500), where x_i represents the remainder when a_i is divided by a_{i-1}.
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
        
    #State: t is 0, `n` is the last input integer, `line` is the last string input by the user, `T` is a list of integers derived from splitting and converting the last `line`, `a` is a list containing the elements [1000 - (T[0] + T[1] + ... + T[n-2]), ..., (999 - T[0]) - T[1], 999 - T[0], 1000], `i` is `n-1`, `result` is a string where each element of the list `a` is converted to a string and joined with spaces.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. For each test case, it takes an integer `n` and a list of `n-1` integers. It then computes a sequence of integers based on these inputs and prints the resulting sequence as a space-separated string. After processing all test cases, the function terminates with `t` set to 0. The final state of the program includes the processed results being printed to the standard output, and the input variables `t`, `n`, `line`, `T`, `a`, and `i` holding their respective final values from the last test case.

