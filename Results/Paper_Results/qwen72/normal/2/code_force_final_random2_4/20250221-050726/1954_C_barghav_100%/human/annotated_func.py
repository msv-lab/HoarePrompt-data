#State of the program right berfore the function call: t is an integer where 1 <= t <= 1000, x and y are strings representing integers where 1 <= x, y < 10^100 and consist only of digits from 1 to 9.
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
        
    #State: `t` is an integer where 1 <= t <= 1000, `x` is a string representing an integer where 1 <= x < 10^100 and consists only of digits from 1 to 9, `y` is a string representing an integer where 1 <= y < 10^100 and consists only of digits from 1 to 9, `a` and `b` are lists of characters from the input strings, `f` is 1, and `i` is the length of `a` - 1. The elements of `a` and `b` are such that for each index `j` (0 <= j < len(a)), if `a[j]` was originally less than `b[j]` and `f` was 0 at that point, `a[j]` and `b[j]` have been swapped. Otherwise, if `a[j]` was greater than `b[j]` and `f` was 0 at that point, `f` is set to 1 but no swap occurs. If `f` was already 1, then any subsequent elements where `a[j]` > `b[j]` are swapped, and `f` remains 1 throughout the rest of the loop.
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: `t` is an integer where 1 <= t <= 1000, `x` is a string representing an integer where 1 <= x < 10^100 and consists only of digits from 1 to 9, `y` is a string representing an integer where 1 <= y < 10^100 and consists only of digits from 1 to 9, `a` and `b` are lists of characters from the input strings, `f` is 1, and `i` is the length of `a` - 1, where `len(a)` is the original length of the input string `x`.
    print()
    #This is printed: (an empty line)
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: `t` is an integer where 1 <= t <= 1000, `x` is a string representing an integer where 1 <= x < 10^100 and consists only of digits from 1 to 9, `y` is a string representing an integer where 1 <= y < 10^100 and consists only of digits from 1 to 9, `a` and `b` are lists of characters from the input strings, `b` has been fully printed, `f` is 1, and `i` is the length of `b` - 1.
    print()
    #This is printed: (an empty line)
#Overall this is what the function does:The function `func_1` reads two lines of input, each representing a string of digits (1 to 9), and processes them to ensure that the first string is lexicographically not smaller than the second string. It does this by swapping characters at corresponding positions if necessary. After processing, it prints the modified first string, followed by an empty line, and then the modified second string. The function does not return any value. The input parameter `t` is mentioned in the comments but is not used in the function.

