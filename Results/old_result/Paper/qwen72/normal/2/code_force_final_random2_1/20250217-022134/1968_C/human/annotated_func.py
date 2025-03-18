#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer such that 2 ≤ n ≤ 500, and x_2, ..., x_n are integers such that 1 ≤ x_i ≤ 500. The sum of values n over all test cases does not exceed 2 · 10^5.
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
        
    #State: After the loop executes all iterations, `t` is 0, `n` remains the same as the input integer for each test case, `i` is `n-1`, `a` contains `n` elements where each element from index 1 to `n-1` is calculated as `a[i] = a[i-1] - T[i-1]`, but now `a` is reversed, and `result` is a string containing the elements of `a` separated by spaces. The variables `line` and `T` are updated with new inputs for each test case, but their final values are not retained after the loop completes.
#Overall this is what the function does:The function reads a series of test cases, where each test case consists of an integer `n` followed by a list of `n-1` integers. For each test case, it calculates a sequence of `n` integers such that each element (except the first) is derived by subtracting the corresponding element from the input list from the previous element in the sequence. The sequence is then reversed, and the function prints the reversed sequence as a space-separated string. After processing all test cases, the function terminates with no return value. The final state of the program is that all test cases have been processed, and the results have been printed.

