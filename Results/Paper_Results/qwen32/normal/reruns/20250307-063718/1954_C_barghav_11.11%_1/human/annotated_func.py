#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, for each test case, x and y are integers such that 1 <= x < 10^100 and 1 <= y < 10^100, and both x and y consist only of digits from 1 to 9.
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
        
    #State: 
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: the concatenation of all elements in the list `a`.
    print()
    #This is printed: (an empty line)
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: the concatenation of all elements in the list `b`.
    print()
    #This is printed: (newline)
#Overall this is what the function does:The function `func_1` reads two strings `a` and `b` as input, where each string consists of digits from 1 to 9. It then rearranges the digits in each string such that for the first half of the strings, the larger digit is placed in `a` and the smaller in `b`, and for the second half, the smaller digit is placed in `a` and the larger in `b`. Finally, it prints the modified strings `a` and `b` on separate lines.

