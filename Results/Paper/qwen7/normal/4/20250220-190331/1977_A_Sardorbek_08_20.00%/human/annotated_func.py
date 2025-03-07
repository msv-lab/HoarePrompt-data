#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 100.
def func():
    a = int(input())
    for i in range(a):
        b, c = map(int, input().split())
        
        q = b, c
        
        if b == c:
            print('YES')
        elif b < c:
            print('NO')
        elif a % 2 == b % 2:
            print('Yes')
        else:
            print('No')
        
    #State: `t` is a positive integer such that \(1 \leq t \leq 100\), `a` is the final value of `a` after all iterations of the loop, `b` is an integer from the input, `c` is an integer from the input, `q` is a tuple containing `b` and `c`, `i` is the total number of iterations which equals `a`
#Overall this is what the function does:The function processes multiple test cases, each consisting of two positive integers \(n\) and \(m\). For each test case, it prints 'YES' if \(n\) equals \(m\), 'NO' if \(n\) is less than \(m\), 'Yes' if both \(n\) and \(m\) have the same parity (both even or both odd), and 'No' otherwise. The function does not return any value but prints the results for each test case.

