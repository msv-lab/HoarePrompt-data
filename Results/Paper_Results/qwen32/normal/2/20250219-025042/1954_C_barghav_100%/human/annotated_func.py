#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, x and y are integers such that 1 ≤ x < 10^100 and 1 ≤ y < 10^100, and both x and y consist only of digits from 1 to 9. Additionally, x and y have the same number of digits.
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
        
    #State: After the loop finishes, `a` and `b` will be modified such that the first position where `a[i] < b[i]` results in a swap, and any subsequent positions where `a[i] > b[i]` also result in swaps. All other positions remain unchanged.
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: All elements of list `a` are printed sequentially without any modifications to `a` or `b`.
    print()
    #This is printed: (newline)
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: All elements of list `a` are printed sequentially without any modifications to `a` or `b`, followed by all elements of list `b` printed sequentially without any modifications to `a` or `b`.
    print()
    #This is printed: (newline)
#Overall this is what the function does:The function reads two integers `x` and `y` as strings, modifies them according to specific rules, and prints the modified versions of both integers. The modification involves swapping digits in `x` and `y` starting from the first position where `x` has a smaller digit than `y`, and continues swapping any subsequent positions where `x` has a larger digit than `y`. After processing, it prints the modified `x` followed by the modified `y`, each on a new line.

