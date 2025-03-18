#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, x and y are integers consisting only of digits from 1 to 9, where 1 ≤ x < 10^100 and 1 ≤ y < 10^100.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 1000, `x` and `y` are integers consisting only of digits from 1 to 9, where 1 ≤ x < 10^100 and 1 ≤ y < 10^100; `a` is a list of digits from the input string `s` such that no element in `a` is less than the corresponding element in `b`; `b` is a list of characters from the new input string; `f` is 1 if any swap occurred during the loop, otherwise, it remains 0.
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: The loop prints all elements of `a` concatenated together, and the values of `t`, `x`, `y`, `a`, `b`, and `f` remain unchanged.
    print()
    #This is printed: (newline)
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: All elements of `b` are printed concatenated together, and `t`, `x`, `y`, `a`, `f` remain unchanged, `i` is `len(b) - 1`.
    print()
    #This is printed: (an empty line)
#Overall this is what the function does:The function reads two integers `x` and `y` consisting only of digits from 1 to 9, compares them digit by digit, and ensures that the resulting number from `x` is not less than the corresponding number from `y` by swapping digits when necessary. It then prints the modified `x` followed by the modified `y`, each on a new line.

