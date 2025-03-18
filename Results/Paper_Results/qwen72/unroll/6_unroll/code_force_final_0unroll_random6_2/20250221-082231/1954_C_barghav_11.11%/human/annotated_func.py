#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, x and y are integers for each test case such that 1 <= x, y < 10^100, and x and y consist only of digits from 1 to 9.
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
        
    #State: The first half of the list `a` will contain the maximum values between the corresponding elements of `a` and `b`, while the second half of the list `a` will contain the minimum values between the corresponding elements of `a` and `b`. Conversely, the first half of the list `b` will contain the minimum values between the corresponding elements of `a` and `b`, while the second half of the list `b` will contain the maximum values between the corresponding elements of `a` and `b`. The variable `t`, `x`, and `y` remain unchanged.
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: The first half of the list `a` will contain the maximum values between the corresponding elements of `a` and `b`, while the second half of the list `a` will contain the minimum values between the corresponding elements of `a` and `b`. The variable `t`, `x`, and `y` remain unchanged.
    print()
    #This is printed: (a newline character)
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: The loop prints the elements of list `b` in order, without any changes to the list `a` or the variables `t`, `x`, and `y`.
    print()
    #This is printed: (a blank line)
#Overall this is what the function does:The function `func_1` takes no explicit parameters but operates on an implicit context where `t` is an integer (1 <= t <= 1000) and `x` and `y` are integers for each test case (1 <= x, y < 10^100) consisting only of digits from 1 to 9. It reads two strings of digits from the input, swaps the digits in the first half of the strings such that the first half of the first string contains the maximum values and the first half of the second string contains the minimum values, and swaps the digits in the second half of the strings such that the second half of the first string contains the minimum values and the second half of the second string contains the maximum values. The function then prints the modified first string followed by the modified second string, each on a new line. The variables `t`, `x`, and `y` remain unchanged.

