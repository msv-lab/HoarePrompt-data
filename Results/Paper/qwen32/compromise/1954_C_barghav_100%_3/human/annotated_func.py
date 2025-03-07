#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, x and y are integers such that 1 <= x < 10^100 and 1 <= y < 10^100, and both x and y consist only of digits from 1 to 9. Additionally, x and y have the same number of digits in each test case.
def func_1():
    a = list(input())
    b = list(input())
    f = 0
    for i in range(len(a)):
        if f == 0:
            if a[i] < b[i]:
                a[i], b[i] = b[i], a[i]
                f = 1
            elif a[i] > b[i]:
                f = 1
        elif a[i] > b[i]:
            a[i], b[i] = b[i], a[i]
        
    #State: `a` is lexicographically greater than or equal to `b`, and `f` is 1 if a swap occurred at any point, otherwise `f` remains 0. The values of `x`, `y`, and `t` remain unchanged.
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: `a` is printed in one line, and `f` remains 1 if a swap occurred at any point, otherwise `f` remains 0. The values of `x`, `y`, and `t` remain unchanged.
    print()
    #This is printed: (an empty line)
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: a is printed in one line, and `f` remains 1 if a swap occurred at any point, otherwise `f` remains 0. The values of `x`, `y`, and `t` remain unchanged. Additionally, the elements of list `b` are printed in one line without any spaces between them.
    print()
    #This is printed: (newline)
#Overall this is what the function does:The function `func_1` reads two integers `x` and `y` (each with the same number of digits and consisting only of digits from 1 to 9) for each of `t` test cases. It ensures that the first integer `x` is lexicographically greater than or equal to the second integer `y` by swapping corresponding digits if necessary. The function then prints the modified `x` and the original `y` on separate lines for each test case.

