#State of the program right berfore the function call: The function is expected to handle multiple test cases, where each test case consists of two integers a and b (1 ≤ a, b ≤ 10^9) representing the dimensions of Bob's rectangle. The number of test cases, t, is a positive integer (1 ≤ t ≤ 10^4).
def func():
    n = int(input())
    for i in range(n):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 != 0 and b % 2 != 0:
            print('NO')
        elif a / 2 == b or b / 2 == a:
            print('NO')
        else:
            print('YES')
        
    #State: The values of `a` and `b` for each test case are processed, and the loop prints 'NO' if both `a` and `b` are odd or if one is exactly half of the other. Otherwise, it prints 'YES'. The variables `n` and `t` remain unchanged.
#Overall this is what the function does:The function `func` reads a positive integer `n` from the input, representing the number of test cases. For each test case, it reads two integers `a` and `b` (1 ≤ a, b ≤ 10^9) from the input, representing the dimensions of a rectangle. The function then prints 'NO' if both `a` and `b` are odd, or if one dimension is exactly half of the other. Otherwise, it prints 'YES'. The function does not return any value, and the variables `n` and the test case inputs `a` and `b` are not retained after the function concludes.

