#State of the program right berfore the function call: t is an integer where 1 <= t <= 1000, x and y are integers for each test case such that 1 <= x, y < 10^100, and x and y consist only of digits from 1 to 9.
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
        
    #State: `t` is an integer where 1 <= t <= 1000, `x` and `y` are integers for each test case such that 1 <= x, y < 10^100, and `x` and `y` consist only of digits from 1 to 9; `a` is a list of characters from the input string, and `b` is a list of characters from the new input string. After the loop, for the first half of the list (up to `len(a) // 2 - 1`), each character in `a` is the maximum of the corresponding characters from the initial `a` and `b`, and each character in `b` is the minimum of the corresponding characters from the initial `a` and `b`. For the second half of the list (from `len(a) // 2` to the end), each character in `a` is the minimum of the corresponding characters from the initial `a` and `b`, and each character in `b` is the maximum of the corresponding characters from the initial `a` and `b`.
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: `t` is an integer where 1 <= t <= 1000, `x` and `y` are integers for each test case such that 1 <= x, y < 10^100, and `x` and `y` consist only of digits from 1 to 9; `a` is a list of characters from the input string, and `b` is a list of characters from the new input string. For the first half of the list (up to `len(a) // 2 - 1`), each character in `a` is the maximum of the corresponding characters from the initial `a` and `b`, and each character in `b` is the minimum of the corresponding characters from the initial `a` and `b`. For the second half of the list (from `len(a) // 2` to the end), each character in `a` is the minimum of the corresponding characters from the initial `a` and `b`, and each character in `b` is the maximum of the corresponding characters from the initial `a` and `b`. `i` is `len(a) - 1`.
    print()
    #This is printed: (a newline character)
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: `t` is an integer where 1 <= t <= 1000, `x` and `y` are integers for each test case such that 1 <= x, y < 10^100, and `x` and `y` consist only of digits from 1 to 9; `a` is a list of characters from the input string, and `b` is a list of characters from the new input string that must have at least `len(a)` elements; `i` is `len(a) - 1`
    print()
    #This is printed: (an empty line)
#Overall this is what the function does:The function `func_1` takes no parameters and returns no values. It reads two lines of input, each representing a string of digits from 1 to 9. The function then modifies these strings such that for the first half of the strings, each character in the first string is the maximum of the corresponding characters from the original strings, and each character in the second string is the minimum. For the second half of the strings, the opposite occurs: each character in the first string is the minimum, and each character in the second string is the maximum. Finally, the function prints the modified first string, followed by a newline, then the modified second string, and another newline. The input variables `t`, `x`, and `y` are not directly affected by the function.

