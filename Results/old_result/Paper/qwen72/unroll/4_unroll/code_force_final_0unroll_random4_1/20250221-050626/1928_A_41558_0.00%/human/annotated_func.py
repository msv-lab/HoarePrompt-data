#State of the program right berfore the function call: The function `func` is expected to take two parameters, `a` and `b`, which are integers such that 1 <= a, b <= 10^9, representing the dimensions of Bob's rectangle. The function should be able to handle multiple test cases, where the number of test cases, `t`, is an integer such that 1 <= t <= 10^4.
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
        
    #State: The loop has executed `n` times, and for each iteration, it has read two integers `a` and `b` from the input. Depending on the values of `a` and `b`, it has printed either 'NO' if both `a` and `b` are odd or if one of them is exactly half of the other, or 'YES' otherwise. The values of `a` and `b` are updated in each iteration, but their final values are not retained after the loop completes. The variable `n` is unchanged.
#Overall this is what the function does:The function `func` reads an integer `n` from the input, which represents the number of test cases. For each of the `n` test cases, it reads two integers `a` and `b` from the input, representing the dimensions of a rectangle. It then prints 'NO' if both `a` and `b` are odd or if one of them is exactly half of the other. Otherwise, it prints 'YES'. The function does not return any value. After the function concludes, the variable `n` remains unchanged, and the values of `a` and `b` are not retained.

