#State of the program right berfore the function call: a and b are non-empty strings consisting of lowercase letters of the English alphabet, and the length of each string does not exceed 10^5 characters.
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
        
    #State of the program after the loop has been executed: Output State: a is a non-empty string, b is a non-empty string, i is equal to len(a), j is equal to len(b), ans is a list containing all characters that are common and in the same positions in both strings a and b. The loop continues executing as long as there are characters left to compare in both strings a and b. If one string ends before the other, the loop stops.
    if (len(ans) == 0) :
        print('-')
    else :
        print(''.join(ans))
    #State of the program after the if-else block has been executed: `a` is a non-empty string, `b` is a non-empty string, `i` is equal to `len(a)`, `j` is equal to `len(b)`, `ans` is a list containing all characters that are common and in the same positions in both strings `a` and `b`. If the length of `ans` is 0, the function does nothing. Otherwise, `ans` contains characters common in the same positions in both `a` and `b`.
#Overall this is what the function does:The function accepts two parameters `a` and `b`, which are non-empty strings consisting of lowercase letters, and prints a string containing all characters that are common and in the same positions in both strings `a` and `b`. If no such characters exist, it prints a hyphen ('-'). The function does not return anything; instead, it modifies the variable `ans` to contain the common characters and then prints them.

