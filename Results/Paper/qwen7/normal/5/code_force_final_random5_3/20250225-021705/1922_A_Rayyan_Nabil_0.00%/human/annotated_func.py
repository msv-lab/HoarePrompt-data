#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 20. a, b, and c are strings consisting of exactly n lowercase Latin letters.
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
        
    #State: Output State: `i` is `n`, `n` is an input integer, `a` is the final input string after all iterations, `b` is the final input string after all iterations, `c` is the final input string after all iterations, `l` is 'YES'.
    #
    #In Natural Language: After the loop has executed all its iterations, the variable `i` will be equal to `n` (since the loop runs from `0` to `n-1` and increments `i` each time). The variable `l` will be 'YES' if for every index `i` in the range `0` to `n-1`, either `a[i]` is not equal to `c[i]` or `b[i]` is not equal to `c[i]`. If there exists any index where both conditions are false (`a[i] == c[i]` and `b[i] == c[i]`), then `l` remains 'NO'. The strings `a`, `b`, and `c` will hold their respective final values after all iterations of the loop.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `t` (1 ≤ t ≤ 1000) and a series of strings `a`, `b`, and `c` (each of length `n` where 1 ≤ n ≤ 20). For each test case, it checks if for every position `i` in the strings, either `a[i]` is not equal to `c[i]` or `b[i]` is not equal to `c[i]`. If this condition holds for all positions, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value but prints the result for each test case.

