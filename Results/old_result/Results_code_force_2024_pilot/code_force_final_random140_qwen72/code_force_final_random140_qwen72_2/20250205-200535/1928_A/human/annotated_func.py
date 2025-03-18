#State of the program right berfore the function call: t is a positive integer where 1 ≤ t ≤ 10^4, and for each test case, a and b are positive integers where 1 ≤ a, b ≤ 10^9.
def func():
    n = int(input())
    for i in range(n):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 != 0 and b % 2 != 0:
            print('NO')
        elif a / 2 == b and b % 2 != 0 or b / 2 == a and a % 2 != 0:
            print('NO')
        else:
            print('YES')
        
    #State: `t` is a positive integer where 1 ≤ t ≤ 10^4, `a` and `b` are integers provided by the user input, `n` is the input integer, and `i` is `n-1`. For each iteration, if both `a` and `b` are odd, "NO" is printed. If `a` is twice `b` and `b` is odd, or `b` is twice `a` and `a` is odd, "NO" is printed. Otherwise, "YES" is printed. After all iterations, `i` will be equal to `n-1`, and the loop will have processed `n` pairs of integers `a` and `b` from the user input.
#Overall this is what the function does:The function reads an integer `n` indicating the number of test cases. For each test case, it reads two integers `a` and `b`. It checks the following conditions for each pair `(a, b)`: if both `a` and `b` are odd, or if one is exactly twice the other and the other is odd, it prints "NO". Otherwise, it prints "YES". After processing all `n` test cases, the function completes, having printed "YES" or "NO" for each pair of integers.

