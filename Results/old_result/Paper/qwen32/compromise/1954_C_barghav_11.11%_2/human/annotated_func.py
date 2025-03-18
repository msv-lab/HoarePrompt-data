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
        
    #State: the first half of `a` contains the larger characters and the first half of `b` contains the smaller characters from the corresponding positions in the original `a` and `b`; the second half of `a` contains the smaller characters and the second half of `b` contains the larger characters from the corresponding positions in the original `a` and `b`.
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: the first half of `a` contains the larger characters and the first half of `b` contains the smaller characters from the corresponding positions in the original `a` and `b`; the second half of `a` contains the smaller characters and the second half of `b` contains the larger characters from the corresponding positions in the original `a` and `b`.
    print()
    #This is printed: (an empty line)
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: the concatenation of all elements in `b`.
    print()
    #This is printed: (a blank line)
#Overall this is what the function does:The function `func_1` processes two integers `x` and `y` provided as input, where each integer consists only of digits from 1 to 9. It rearranges the digits of these numbers such that in the first half of each number, the larger digits from the corresponding positions of the original numbers are placed, and in the second half, the smaller digits are placed. It then prints the rearranged first number followed by the rearranged second number.

