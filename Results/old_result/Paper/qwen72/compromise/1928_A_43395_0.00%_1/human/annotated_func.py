#State of the program right berfore the function call: The function should take two integers a and b as input, where 1 ≤ a, b ≤ 10^9, representing the dimensions of the rectangle.
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
        
    #State: The function will print 'yes' or 'no' for each iteration based on the conditions provided, but the values of `a` and `b` will remain unchanged after the loop finishes.
#Overall this is what the function does:The function `func` reads an integer from the input, which represents the number of test cases. For each test case, it reads two integers `a` and `b` from the input, representing the dimensions of a rectangle. The function then prints 'yes' or 'no' for each test case based on the following conditions: if both `a` and `b` are even, it prints 'yes'; if the difference between `a` and `b` is odd, it prints 'yes'; otherwise, it prints 'no'. The function does not modify the values of `a` and `b` after processing each test case.

