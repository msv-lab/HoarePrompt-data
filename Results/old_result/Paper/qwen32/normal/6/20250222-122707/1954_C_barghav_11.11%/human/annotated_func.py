#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, x and y are integers such that 1 <= x < 10^100 and 1 <= y < 10^100, and both x and y consist only of digits from 1 to 9.
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
        
    #State: `t` is an integer such that 1 <= t <= 1000; `x` and `y` are integers such that 1 <= x < 10^100 and 1 <= y < 10^100, and both consist only of digits from 1 to 9; `a` is a list of characters where the first half of `a` contains the maximum values between the corresponding elements of the original `a` and `b`, and the second half contains the minimum values; `b` is a list of characters where the first half contains the minimum values between the corresponding elements of the original `a` and `b`, and the second half contains the maximum values.
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: The complete list `a` is printed out, and `i` equals the length of `a`.
    print()
    #This is printed: (an empty line)
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: `a` is printed out, `i` equals `len(b) - 1`, and all elements of `b` are printed concatenated together.
    print()
    #This is printed: (newline)
#Overall this is what the function does:The function `func_1` reads two integers `x` and `y` as strings, processes them by rearranging their digits such that the first half of the first number consists of the maximum digits and the second half consists of the minimum digits compared to the corresponding digits of the second number, and vice versa for the second number. It then prints the modified versions of both numbers.

