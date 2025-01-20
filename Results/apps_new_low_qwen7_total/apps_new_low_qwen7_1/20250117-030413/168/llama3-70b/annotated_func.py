#State of the program right berfore the function call: a and b are strings consisting of lowercase letters of the English alphabet, with lengths no bigger than 10^5.
def func():
    a = input()

b = input()

i = 0

j = 0

ans = []
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            ans.append(a[i])
            i += 1
            j += 1
        else:
            i += 1
        
    #State of the program after the loop has been executed: `a` is a string, `b` is a string, `i` is equal to `len(a)`, `j` is equal to `len(b)`, and `ans` is a list containing all characters of `a` that also appear in `b` in order.
    if (len(ans) == 0) :
        print('-')
    else :
        print(''.join(ans))
    #State of the program after the if-else block has been executed: *`a` is a string, `b` is a string, `i` is equal to `len(a)`, `j` is equal to `len(b)`, and `ans` is a list containing all characters of `a` that also appear in `b` in order. If `ans` is an empty list, no action is taken. Otherwise, the list `ans` is printed.
#Overall this is what the function does:The function `func()` takes two strings `a` and `b` as input, both consisting of lowercase letters of the English alphabet with lengths no greater than \(10^5\). It then iterates through both strings, comparing each character of `a` with each character of `b`. If a character from `a` matches a character from `b`, it appends that character to the list `ans`. After the loop, if `ans` is empty, it prints a hyphen (`-`). Otherwise, it prints the concatenated string formed by joining all elements of `ans`. The function does not return anything.

Potential edge cases and missing functionality:
- If either `a` or `b` is an empty string, the loop will not execute, and `ans` will remain an empty list. Therefore, a hyphen (`-`) will be printed in this case.
- The function does not handle non-alphabetical characters or special characters in the input strings. It assumes that both `a` and `b` contain only lowercase letters of the English alphabet.
- The function does not account for the possibility that the same character might appear multiple times in both strings; it only checks for matching characters once per position in `a` and `b`.

