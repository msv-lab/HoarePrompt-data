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
        
    #State: x and y are strings representing integers of the same length, with their characters swapped in the first half and then swapped back in the second half. a is a list of characters from x (or y), and b is a list of characters from the input provided by the user, with the same transformations applied.
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: a list of characters from string x printed in sequence.
    print()
    #This is printed: an empty line
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: the characters of string b printed in sequence without any spaces.
    print()
    #This is printed: newline
#Overall this is what the function does:The function accepts no parameters and processes two strings `x` and `y`, swapping their characters in the first half of each string and then swapping them back in the second half. It then prints the modified strings `a` and `b` without any spaces between characters.

