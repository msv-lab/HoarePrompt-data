#State of the program right berfore the function call: The function should take two integers a and b as input, where 1 ≤ a, b ≤ 10^9, representing the dimensions of the rectangle.
def func():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        if a % 2 == 0 or b % 2 == 0:
            print('Yes')
        else:
            print('No')
        
    #State: The values of `a` and `b` are updated to the last input values provided in the loop, and `t` remains unchanged. The loop prints 'Yes' if either `a` or `b` is even, and 'No' if both are odd for each iteration.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads two integers `a` and `b` from the input, representing the dimensions of a rectangle. It then checks if either `a` or `b` is even. If at least one of them is even, it prints 'Yes'; otherwise, it prints 'No'. After processing all test cases, the function does not return any value, and the final state of the program includes the last input values of `a` and `b` from the last test case, and `t` remains unchanged.

