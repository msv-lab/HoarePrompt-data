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
        
    #State: - `t` remains unchanged.
    #- `x` remains unchanged.
    #- `y` remains unchanged.
    #- `a` is modified such that for the first half, each element is the maximum of the corresponding elements from the original `a` and `b`, and for the second half, each element is the minimum of the corresponding elements from the original `a` and `b`.
    #- `b` is modified such that for the first half, each element is the minimum of the corresponding elements from the original `a` and `b`, and for the second half, each element is the maximum of the corresponding elements from the original `a` and `b`.
    #
    #Output State:
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: 4527
    print()
    #This is printed: (an empty line)
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: 4527
    print()
    #This is printed: (newline)
#Overall this is what the function does:The function reads two integers `x` and `y` as strings, then modifies them such that for the first half of their lengths, each digit in the first integer becomes the maximum of the corresponding digits from the original integers, and each digit in the second integer becomes the minimum. For the second half, the opposite occurs. It then prints the modified integers.

