#State of the program right berfore the function call: The function receives an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, it receives two integers a and b (1 ≤ a, b ≤ 10^9) representing the dimensions of Bob's rectangle.
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
        
    #State: A series of 'yes' or 'no' based on the input test cases.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `a` and `b` representing the dimensions of a rectangle. It then prints 'yes' if the rectangle can be divided into smaller rectangles of equal size where each smaller rectangle has both dimensions as even numbers, or if the difference between `a` and `b` is odd. Otherwise, it prints 'no'.

