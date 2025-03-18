#State of the program right berfore the function call: The function should accept two parameters, a and b, which are integers such that 1 <= a, b <= 10^9, representing the dimensions of the rectangle. The function should be called multiple times with different values of a and b, as specified by the number of test cases t (1 <= t <= 10^4).
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
        
    #State: The loop will execute `n` times, reading pairs of integers `a` and `b` from the input. For each pair, it will check if both `a` and `b` are odd, or if one is exactly half of the other. If either condition is true, it will print 'NO'. Otherwise, it will print 'YES'. The values of `a` and `b` will be updated with each iteration, but their final values after the loop will be the last pair read from the input. The value of `n` will remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `n` from the input, representing the number of test cases. For each test case, it reads two integers `a` and `b` from the input, representing the dimensions of a rectangle. It then checks if both `a` and `b` are odd, or if one is exactly half of the other. If either condition is true, it prints 'NO'. Otherwise, it prints 'YES'. The function does not return any value; it only prints the results for each test case. After the function concludes, the value of `n` remains unchanged, and the last values of `a` and `b` will be the dimensions read in the final test case.

