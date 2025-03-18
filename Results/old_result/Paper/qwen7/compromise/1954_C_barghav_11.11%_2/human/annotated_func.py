#State of the program right berfore the function call: x and y are strings representing integers of the same length, consisting of digits from 1 to 9.
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
        
    #State: Output State: `x` and `y` are strings where each character in `x` is the maximum of the corresponding characters in the original `x` and `y`, and each character in `y` is the minimum of the corresponding characters in the original `x` and `y`, but only for the first half of the strings. For the second half, each character in `x` is the minimum of the corresponding characters in the original `x` and `y`, and each character in `y` is the maximum of the corresponding characters in the original `x` and `y`.
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: x and y are strings where each character in x is the maximum of the corresponding characters in the original x and y, and each character in y is the minimum of the corresponding characters in the original x and y, but only for the first half of the strings. For the second half, each character in x is the minimum of the corresponding characters in the original x and y, and each character in y is the maximum of the corresponding characters in the original x and y.
    print()
    #This is printed: ''
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: b
    print()
    #This is printed: ''
#Overall this is what the function does:The function takes two strings `x` and `y` as input, where both strings consist of digits from 1 to 9 and have the same length. It modifies these strings such that for the first half of the string, each character in `x` becomes the maximum of the corresponding characters in the original `x` and `y`, and each character in `y` becomes the minimum of the corresponding characters in the original `x` and `y`. For the second half of the string, this process is reversed: each character in `x` becomes the minimum of the corresponding characters in the original `x` and `y`, and each character in `y` becomes the maximum of the corresponding characters in the original `x` and `y`. After modifying the strings, the function prints the modified `x` and `y` strings. The function does not return any value.

