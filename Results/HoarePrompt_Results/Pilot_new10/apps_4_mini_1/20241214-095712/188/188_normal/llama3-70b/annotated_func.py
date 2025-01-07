#State of the program right berfore the function call: n is an even integer in the range 2 to 100, and the input consists of n integers each in the range 1 to 100 representing the numbers on the cards.
def func():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
        
    #State of the program after the  for loop has been executed: `n` is an even integer in the range 2 to 100, `i` is `n-1`, `a` is a list containing `n` integers from input.
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
        
    #State of the program after the  for loop has been executed: `n` is an even integer in the range 2 to 100, `d` is a dictionary that contains the count of each unique integer from the list `a`, and `a` is a list containing `n` integers.
    c = 0
    a1, a2 = -1, -1
    for i in d:
        if d[i] == n // 2:
            if c == 0:
                a1 = i
                c += 1
            else:
                a2 = i
                break
        
    #State of the program after the  for loop has been executed: `n` is an even integer in the range 2 to 100, `d` contains all unique integers from the list `a`, `c` indicates the number of integers in `d` that have a count equal to `n // 2` (0, 1, or 2), `a1` is the first key in `d` for which the count equals `n // 2` (or remains -1 if none), `a2` is the second key in `d` for which the count equals `n // 2` (or remains -1 if fewer than two exist). If `c` is 0, then neither `a1` nor `a2` is set to any key in `d`; if `c` is 1, then `a1` has a value from `d` while `a2` remains -1; if `c` is 2, then both `a1` and `a2` contain keys from `d`.
    if (a1 != -1 and a2 != -1) :
        print('YES')
        print(a1, a2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an even integer in the range 2 to 100. If both `a1` and `a2` are not -1, the values of `a1` and `a2` have been printed. Otherwise, if either `a1` or `a2` is -1 (or both), 'NO' has been printed.
#Overall this is what the function does:The function accepts an even integer `n` (ranging from 2 to 100) which indicates the number of card values to be read. It then reads `n` integers (each in the range from 1 to 100), counts the occurrences of each unique integer, and looks for exactly two distinct numbers that appear `n // 2` times. If such two numbers are found, it prints 'YES' followed by the two numbers. Otherwise, it prints 'NO'. If fewer than two numbers meet the requirement, the function does not return or display any information about those numbers.

