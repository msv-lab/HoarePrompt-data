#State of the program right berfore the function call: t is an integer where 1 <= t <= 1000, representing the number of test cases. For each test case, x and y are integers where 1 <= x, y < 10^100, and both consist only of digits from 1 to 9.
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
        
    #State: `t` is an integer where 1 <= t <= 1000, `x` and `y` are integers where 1 <= x, y < 10^100, `a` is a list of characters from the input string that has been modified such that no character in `a` is less than the corresponding character in `b` (if `f` was set to 1 during the loop), or `a` and `b` remain unchanged if no such condition was met. `b` is a list of characters from the new input string that may have been swapped with characters in `a`. `f` is 1 if any character in `a` was found to be less than the corresponding character in `b` and a swap occurred, otherwise `f` remains 0. The loop iterates through all characters in `a` and `b` up to the length of `a`.
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: `i` is `len(a) - 1`, `a` is a list of characters with no elements remaining to be processed.
    print()
    #This is printed: (an empty line)
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: `i` is `len(b) - 1`, `a` is a list of characters with no elements remaining to be processed, `b` has been fully iterated over, and all its elements have been printed.
    print()
    #This is printed: (a blank line)
#Overall this is what the function does:The function `func_1` processes two input strings, `a` and `b`, which represent large integers consisting only of digits from 1 to 9. It ensures that no character in `a` is less than the corresponding character in `b` by swapping them if necessary. After processing, it prints the modified `a` and `b` strings, each followed by a newline. The function does not return any value but modifies and prints the input strings according to the specified conditions.

