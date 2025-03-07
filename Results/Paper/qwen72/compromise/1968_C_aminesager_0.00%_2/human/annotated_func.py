#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer where 2 ≤ n ≤ 500, and x is a list of n-1 integers where 1 ≤ x_i ≤ 500. The sum of values n over all test cases does not exceed 2 · 10^5.
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
        
    #State: After all iterations of the loop, `t` is `0`, `n` is the last input integer, `a` is a list of `n` elements where each element is calculated as described, `result` is a string containing the elements of `a` separated by spaces, and `line` and `T` are the last input string and its corresponding list of integers, respectively.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list of `n-1` integers. It calculates a list `a` of `n` integers based on the input list, where each element is derived from the previous element minus the corresponding element from the input list. The function then prints the elements of `a` in reverse order, separated by spaces. After processing all test cases, the function terminates with `t` set to `0`, `n` being the last input integer, `a` being the final calculated list, and `result` being the string representation of `a`.

