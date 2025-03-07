#State of the program right berfore the function call: n is an integer such that 1 <= n <= 20, a, b, and c are strings of length n consisting of lowercase Latin letters.
def func_1(n, a, b, c):
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            return 'YES'
        
    #State: Output State: The value returned by the function is either 'YES' or 'NO', depending on whether there exists at least one index `i` where `a[i]` is not equal to `c[i]` and `b[i]` is also not equal to `c[i]`. If such an index exists, the function returns 'YES'; otherwise, it continues all iterations without finding any such index and implicitly returns 'NO'.
    return 'NO'
    #The program returns 'NO'
#Overall this is what the function does:The function accepts three parameters: an integer `n` (with 1 <= n <= 20), and two strings `a` and `b` each of length `n` consisting of lowercase Latin letters, along with another string `c` of the same length. It checks if there is at least one index `i` where both `a[i]` and `b[i]` are different from `c[i]`. If such an index exists, the function returns 'YES'; otherwise, it returns 'NO'. The final state of the program after the function concludes is that it returns either 'YES' or 'NO' based on the condition checked.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 20. a, b, and c are strings consisting of exactly n lowercase Latin letters.
def func_2():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        
        a = input().strip()
        
        b = input().strip()
        
        c = input().strip()
        
        results.append(func_1(n, a, b, c))
        
    #State: Output State: `t` is an integer such that 1 ≤ `t` ≤ 1000, and it is the number of iterations the loop executed; `results` is a list containing `t` elements, where each element is the result of calling `func_1(n, a, b, c)` with the respective inputs `n`, `a`, `b`, and `c` for each iteration.
    for result in results:
        print(result)
        
    #State: `results` is a list containing `t` elements, where each element is printed on a new line.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `t` (number of iterations), an integer `n` (length of strings), and three strings `a`, `b`, and `c` (each of length `n`). For each test case, it calls `func_1(n, a, b, c)` to perform some unspecified operations and collects the results in a list. Finally, it prints each result on a new line.

