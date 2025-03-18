#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, x and y are integers such that 1 <= x < 10^100 and 1 <= y < 10^100, and both x and y consist only of digits from 1 to 9. Additionally, for each test case, x and y are of the same length.
def func_1():
    a = list(input())
    b = list(input())
    for i in range(len(a)):
        if i <= len(a) // 2 - 1:
            n = min(a[i], b[i])
            m = max(a[i], b[i])
            a[i] = m
            b[i] = n
        else:
            n = min(a[i], b[i])
            m = max(a[i], b[i])
            a[i] = n
            b[i] = m
        
    #State: - `t` remains unchanged.
    #- `x` and `y` remain unchanged.
    #- `a` and `b` are rearranged such that in the first half, `a` contains the larger digits and `b` contains the smaller digits, and in the second half, `a` contains the smaller digits and `b` contains the larger digits.
    #
    #Output State:
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: the sequence of digits in `a` after the rearrangement.
    print()
    #This is printed: (newline)
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: 12345
    print()
    #This is printed: (newline)
#Overall this is what the function does:The function `func_1` reads two integers `x` and `y` of the same length, consisting only of digits from 1 to 9. It rearranges the digits such that in the first half of the numbers, the larger digit from each position is placed in `x` and the smaller in `y`, and in the second half, the smaller digit from each position is placed in `x` and the larger in `y`. It then prints the rearranged `x` and `y` on separate lines.

