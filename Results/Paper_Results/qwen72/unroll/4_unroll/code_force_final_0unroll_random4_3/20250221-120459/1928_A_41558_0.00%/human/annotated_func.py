#State of the program right berfore the function call: The function should take two arguments, a and b, which are integers such that 1 <= a, b <= 10^9, representing the dimensions of the rectangle.
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
        
    #State: The loop will execute `n` times, and for each iteration, it will read two integers `a` and `b` from the input. If both `a` and `b` are odd, or if one is exactly half of the other, it will print 'NO'. Otherwise, it will print 'YES'. The values of `a` and `b` will be updated with each iteration, but the value of `n` will remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `n` from the input, representing the number of test cases. For each of the `n` test cases, it reads two integers `a` and `b` from the input, which represent the dimensions of a rectangle. It then checks if both `a` and `b` are odd, or if one is exactly half of the other. If either condition is true, it prints 'NO'. Otherwise, it prints 'YES'. The function does not return any value. After the function concludes, the input values `a` and `b` for each test case are processed, and the program state is unchanged except for the output printed.

