#State of the program right berfore the function call: n is an even integer between 2 and 100, and the subsequent n integers represent the numbers written on the n cards, where each integer is between 1 and 100.
def func():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
        
    #State of the program after the  for loop has been executed: `n` is an even integer between 2 and 100, `i` is `n - 1`, `a` contains `n` integers entered by the user.
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
        
    #State of the program after the  for loop has been executed: `n` is an even integer between 2 and 100, `d` is a dictionary containing each unique integer from the list `a` as keys, and their corresponding counts as values. The total number of iterations equals the number of elements in `a`.
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
        
    #State of the program after the  for loop has been executed: `n` is an even integer between 2 and 100, `d` has at least 1 entry, `c` is either 0, 1, or 2, `a1` is the first key in `d` for which `d[a1]` equals `n // 2` if such a key exists; otherwise, `a1` remains -1. `a2` is the second key in `d` for which `d[a2]` equals `n // 2` if such a key exists; otherwise, `a2` remains -1. If no keys in `d` have a value of `n // 2`, then both `a1` and `a2` remain -1.
    if (a1 != -1 and a2 != -1) :
        print('YES')
        print(a1, a2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an even integer between 2 and 100, `d` has at least 1 entry, `c` is either 0, 1, or 2. If both `a1` and `a2` are valid keys in `d` for which `d[a1]` equals `n // 2`, then 'YES' has been printed along with the values of `a1` and `a2`. Otherwise, at least one of `a1` or `a2` is -1, and 'NO' has been printed.
#Overall this is what the function does:The function accepts an even integer `n` (between 2 and 100) and then reads `n` integers (each between 1 and 100) from user input. It counts the occurrences of each integer and checks if there are exactly two distinct integers that appear `n / 2` times. If such integers exist, it prints 'YES' followed by the two integers; otherwise, it prints 'NO'.

