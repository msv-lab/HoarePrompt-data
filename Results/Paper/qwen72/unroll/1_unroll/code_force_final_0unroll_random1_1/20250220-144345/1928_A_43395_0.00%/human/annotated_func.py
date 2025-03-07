#State of the program right berfore the function call: The function `func` is intended to process multiple test cases, each with two integers a and b representing the dimensions of a rectangle. The inputs a and b for each test case satisfy 1 ≤ a, b ≤ 10^9. The function should be able to handle up to 10^4 test cases.
def func():
    for i in range(int(input())):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 == 0 and b % 2 == 0:
            print('yes')
        elif (a - b == -a, a) or (b - a == -b, b):
            print('no')
        elif (a - b) % 2 > 0 or (a - b) % 2 < 0:
            print('yes')
        else:
            print('no')
        
    #State: The function `func` processes all test cases, printing 'yes' for rectangles where both dimensions are even, and 'no' for all other cases. The variables `a` and `b` are updated for each test case, but their final values are not retained after the loop completes.
#Overall this is what the function does:The function `func` processes multiple test cases, each with two integers `a` and `b` representing the dimensions of a rectangle. It prints 'yes' if both dimensions are even, and 'no' for all other cases. The function does not return any values. The variables `a` and `b` are updated for each test case but their final values are not retained after the loop completes.

