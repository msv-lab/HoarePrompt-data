#State of the program right berfore the function call: a and b are non-empty strings consisting of lowercase letters of the English alphabet, with lengths no bigger than 10^5.
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
        
    #State of the program after the loop has been executed: a is a non-empty string consisting of lowercase letters, b is a non-empty string consisting of lowercase letters, i is equal to len(a), j is equal to len(b), and ans is a list containing characters from a that match corresponding characters in b, maintaining their order.
    if (len(ans) == 0) :
        print('-')
    else :
        print(''.join(ans))
    #State of the program after the if-else block has been executed: *`a` is a non-empty string consisting of lowercase letters, `b` is a non-empty string consisting of lowercase letters, `i` is equal to `len(a)`, `j` is equal to `len(b)`, and `ans` is a list containing characters from `a` that match corresponding characters in `b`, maintaining their order. If no such characters exist, `ans` is an empty list. Otherwise, `ans` contains at least one character from `a` that matches corresponding characters in `b`, maintaining their order.
#Overall this is what the function does:The function accepts two parameters `a` and `b`, which are non-empty strings consisting of lowercase letters of the English alphabet with lengths no bigger than \(10^5\). It then iterates through both strings simultaneously, comparing each character. If a character in `a` matches the corresponding character in `b`, it is added to the list `ans`. After the loop, if `ans` is empty, it prints `-`; otherwise, it prints the concatenation of the characters in `ans`. The final state of the program is such that `a` and `b` remain unchanged, `i` is set to `len(a)`, `j` is set to `len(b)`, and `ans` is a list of matching characters from `a` that also appear in `b` in the same order, or an empty list if no such characters exist. The function does not modify the contents of `a` or `b` beyond the comparison process.

