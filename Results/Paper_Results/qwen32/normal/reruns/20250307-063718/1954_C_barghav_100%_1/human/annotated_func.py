#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, x and y are integers consisting only of digits from 1 to 9, and 1 <= x < 10^100, 1 <= y < 10^100. Additionally, x and y have the same length in each test case.
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
        
    #State: `t` remains the same; `x` and `y` remain the same; `a` is modified based on the loop logic; `b` remains the same; `f` is 1 if any swap occurred or if `a[i] > b[i]` was encountered after the first swap.
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: The complete list `a` is printed out, and the values of `t`, `x`, `y`, `b`, and `f` remain unchanged.
    print()
    #This is printed: (an empty line)
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: The complete list `a` is printed out, `t`, `x`, `y`, `b`, and `f` remain unchanged, and all elements of the list `b` are printed in sequence.
    print()
    #This is printed: (an empty line)
#Overall this is what the function does:The function `func_1` reads two integers `x` and `y` of the same length, consisting only of digits from 1 to 9, and prints them after potentially swapping some of their corresponding digits based on a specific rule. It prints the modified version of `x` first, followed by the original `y`, each on a new line.

