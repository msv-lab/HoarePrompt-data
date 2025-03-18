#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 20, and a, b, and c are strings consisting of exactly n lowercase Latin letters.
def func():
    t = int(input())
    l = 'YES'
    for i in range(t):
        n = int(input())
        
        a = input()
        
        b = input()
        
        c = input()
        
        for i in range(n):
            if a[i] != c[i] and b[i] != c[i]:
                l = 'YES'
        else:
            l = 'NO'
        
        print(l)
        
    #State: Output State: After the loop executes all iterations, `i` will be equal to `n`, `l` will be 'YES', `c` will be the last input string, `n` must be a positive integer, and the condition `a[i] != c[i] and b[i] != c[i]` must be true for every `i` from `0` to `n-1`.
    #
    #This means that after all iterations of the loop have completed, the value of `i` will match the final value of `n`, `l` will be set to 'YES' if the specified condition holds for all characters in the strings `a`, `b`, and `c` for each index `i` from `0` to `n-1`. The strings `a`, `b`, and `c` will retain their last input values, and `n` will hold the last value it was assigned during the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t (number of test cases), an integer n (length of strings), and three strings a, b, and c (each of length n). For each test case, it checks if for every index i from 0 to n-1, either a[i] ≠ c[i] or b[i] ≠ c[i]. If this condition holds for all indices, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value but prints the result for each test case.

