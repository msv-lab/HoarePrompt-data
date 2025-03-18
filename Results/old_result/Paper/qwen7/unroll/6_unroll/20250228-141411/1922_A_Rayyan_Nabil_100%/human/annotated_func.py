#State of the program right berfore the function call: n is an integer such that 1 <= n <= 20, a, b, and c are strings consisting of exactly n lowercase Latin letters.
def func_1(n, a, b, c):
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            return 'YES'
        
    #State: Output State: The string `c` is either equal to `a` or `b`, or for every index `i` from 0 to `n-1`, if `c[i]` is different from `a[i]`, then `b[i]` must be equal to `c[i]`.
    return 'NO'
    #The program returns 'NO'
#Overall this is what the function does:The function accepts three parameters: an integer `n` (between 1 and 20), and two strings `a` and `b` each consisting of exactly `n` lowercase Latin letters, along with a third string `c` also consisting of exactly `n` lowercase Latin letters. It checks whether `c` is either equal to `a` or `b`, or for every index `i` from 0 to `n-1`, if `c[i]` is different from `a[i]`, then `b[i]` must be equal to `c[i]`. If any index `i` violates this condition, the function returns 'YES'. Otherwise, it returns 'NO'.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 20, and a, b, c are strings consisting of exactly n lowercase Latin letters.
def func_2():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        
        a = input().strip()
        
        b = input().strip()
        
        c = input().strip()
        
        results.append(func_1(n, a, b, c))
        
    #State: Output State: `t` integers within the range 1 ≤ t ≤ 1000, stored in the `results` list, where each integer is the result of calling `func_1(n, a, b, c)` for corresponding inputs `n`, `a`, `b`, and `c`.
    for result in results:
        print(result)
        
    #State: 1000 integers, each identical to the corresponding integer in the `results` list, printed on separate lines.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `t` (1 ≤ t ≤ 1000), an integer `n` (1 ≤ n ≤ 20), and three strings `a`, `b`, and `c` (each consisting of exactly `n` lowercase Latin letters). It then calls another function `func_1` with these inputs and stores the result. Finally, it prints the results for all test cases, one per line.

