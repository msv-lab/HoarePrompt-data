#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 1000, representing the number of test cases. For each test case, x and y are integers where 1 ≤ x, y < 10^100, and both consist only of digits from 1 to 9.
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
        
    #State: `t` is an integer where 1 ≤ t ≤ 1000, `x` and `y` are integers where 1 ≤ x, y < 10^100, and both consist only of digits from 1 to 9, `a` is a list of characters from the input string, `b` is a list of characters from the new input string, `f` is 1. After the loop has executed all iterations, the characters in `a` and `b` are such that for any index `i` where 0 ≤ i < len(a), if `a[i]` was initially greater than `b[i]`, they have been swapped, and if `a[i]` was initially less than or equal to `b[i]`, they remain unchanged. The flag `f` is set to 1, indicating that a swap has occurred or that the condition for swapping has been checked and no further swaps are necessary.
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: `t` is an integer where 1 ≤ t ≤ 1000, `x` and `y` are integers where 1 ≤ x, y < 10^100, and both consist only of digits from 1 to 9, `a` is a list of characters from the input string, `b` is a list of characters from the new input string, `f` is 1, `i` is len(a) - 1.
    print()
    #This is printed: (an empty line)
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: `t` is an integer where 1 ≤ t ≤ 1000, `x` and `y` are integers where 1 ≤ x, y < 10^100, and both consist only of digits from 1 to 9, `a` is a list of characters from the input string, `b` is a list of characters from the new input string that has been fully processed, `f` is 1, `i` is len(a) - 1.
    print()
    #This is printed: (a newline character)
#Overall this is what the function does:The function `func_1` reads two strings from the input, processes them to ensure that for any index `i`, if the character in the first string was initially greater than the character in the second string, they are swapped. It then prints the modified first string, followed by the modified second string, each on a new line. The function does not return any value. The state after the function concludes is that the input strings have been transformed and printed according to the described rules, and the flag `f` is set to 1, indicating that the processing has been completed.

