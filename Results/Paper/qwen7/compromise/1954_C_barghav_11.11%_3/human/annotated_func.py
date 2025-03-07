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
        
    #State: Output State: `x` is a string where the first half of its characters are swapped with the corresponding characters from `y` in ascending order, and `y` is a string where the second half of its characters are swapped with the corresponding characters from `x` in descending order.
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: The value of `a` is printed out character by character in the same order it was initially.
    print()
    #This is printed: the characters of `a` (where `a` is the initial value that is printed character by character)
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: the value of `b` printed out character by character in the same order it was initially.
    print()
    #This is printed: b (where b is the initial string whose characters are printed)
#Overall this is what the function does:The function takes two strings `x` and `y` as input, where both strings consist of digits from 1 to 9 and have the same length. It swaps the first half of the characters in `x` with the corresponding characters in `y` in ascending order, and swaps the second half of the characters in `y` with the corresponding characters in `x` in descending order. The function then prints the modified strings `a` and `b`, which are the initial values of `x` and `y` respectively.

