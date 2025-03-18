#State of the program right berfore the function call: The function should take two parameters, a and b, which are integers such that 1 <= a, b <= 10^9, representing the dimensions of the rectangle.
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
        
    #State: The loop will execute for the number of iterations specified by the first input. For each iteration, it will read two integers a and b from the input, and based on the conditions provided, it will print 'yes' or 'no'. The values of a and b will be updated with each iteration, but the initial values of a and b provided as parameters to the function will remain unchanged.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any value. It reads a series of inputs from the user, where the first input specifies the number of iterations. For each iteration, it reads two integers `a` and `b` from the input, representing the dimensions of a rectangle. Based on the conditions provided, it prints 'yes' or 'no' for each pair of dimensions. The values of `a` and `b` are updated with each iteration, but no initial parameters are provided or modified. The function's purpose is to determine and print whether certain conditions related to the dimensions of the rectangle are met.

