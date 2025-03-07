#State of the program right berfore the function call: The function `func` is expected to take two parameters, `n` and `m`, which are non-negative integers such that 1 <= n, m <= 100. Additionally, the function should be able to handle multiple test cases, where the number of test cases `t` is a positive integer such that 1 <= t <= 100.
def func():
    a = int(input())
    for i in range(a):
        b, c = map(int, input().split())
        
        q = b, c
        
        if b == c:
            print('YES')
        elif b < c:
            print('NO')
        elif b % 2 == c % 2:
            print('Yes')
        else:
            print('No')
        
    #State: `a` is a positive integer, `i` is `a-1`, and `q` is the tuple `(b, c)` containing the last input integers `b` and `c`. The parities of `b` and `c` remain unchanged. If `b` is equal to `c`, the program retains this state. If `b` is less than `c`, the program retains the state where `b` is not equal to `c`. If `b` and `c` have the same parity, the program retains the state where `b` and `c` are either equal or not equal. If `b` and `c` have different parities, the program also retains the state where `b` and `c` are either equal or not equal.
#Overall this is what the function does:The function `func` reads a positive integer `a` from the input, representing the number of test cases. For each test case, it reads two integers `b` and `c` from the input. The function then prints 'YES' if `b` is equal to `c`, 'NO' if `b` is less than `c`, and 'Yes' if `b` and `c` have the same parity (both even or both odd). If `b` and `c` have different parities and `b` is greater than `c`, it prints 'No'. The function does not return any value and does not modify any external state. After the function concludes, the program has processed `a` test cases and printed the corresponding results for each.

