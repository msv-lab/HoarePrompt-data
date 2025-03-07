#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, x and y are integers such that 1 <= x < 10^100 and 1 <= y < 10^100, and both x and y consist only of digits from 1 to 9. The lengths of x and y are the same for each test case.
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
        
    #State: `a` is lexicographically not less than `b`, `f` is 1 if any swap occurred, otherwise 0, `t`, `x`, `y` remain unchanged.
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: `a` is lexicographically not less than `b`, `f` is 1 if any swap occurred, otherwise 0, `t`, `x`, `y` remain unchanged. The string `a` is printed.
    print()
    #This is printed: (an empty line)
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: `a` is lexicographically not less than `b`, `f` is 1 if any swap occurred, otherwise 0, `t`, `x`, `y` remain unchanged. The string `b` is printed.
    print()
    #This is printed: (an empty line)
#Overall this is what the function does:The function `func_1` reads two strings `a` and `b` of the same length, consisting of digits from 1 to 9. It ensures that `a` is not lexicographically less than `b` by potentially swapping digits between `a` and `b` under certain conditions. After processing, it prints the modified string `a` followed by the modified string `b`, each on a new line. The input values `t`, `x`, and `y` remain unchanged throughout the execution.

