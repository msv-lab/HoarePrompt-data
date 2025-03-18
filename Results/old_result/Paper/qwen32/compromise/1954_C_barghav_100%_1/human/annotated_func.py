#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, x and y are integers such that 1 <= x < 10^100 and 1 <= y < 10^100, and both x and y consist only of digits from 1 to 9. Additionally, the length of x and y is the same for each test case.
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
        
    #State: `a` and `b` are modified such that the first position where `a` was less than `b` has its digits swapped, and any subsequent positions where `a` is greater than `b` also have their digits swapped. The values of `t`, `x`, `y`, and the lengths of `a` and `b` remain unchanged.
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: The output of the loop will be the sequence of elements in `a` as they are after the initial state modifications. Since the loop only prints the elements of `a` and does not change them, the output state is simply the state of `a` after the initial modifications.
    #
    #Output State:
    print()
    #This is printed: (nothing)
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: Hello
    print()
    #This is printed: (newline)
#Overall this is what the function does:The function `func_1` reads two integers `x` and `y` of the same length, each consisting only of digits from 1 to 9, and prints them after performing a specific transformation. The transformation involves swapping the digits at the first position where `x` is less than `y` and any subsequent positions where `x` is greater than `y`. The function processes one test case at a time and outputs the modified `x` and `y` separately.

