#State of the program right berfore the function call: n is an even integer in the range [2, 100], and the following n integers, each in the range [1, 100], represent the numbers on the n cards.
def func():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
        
    #State of the program after the  for loop has been executed: `n` is an even integer in the range [2, 100], `i` is `n - 1`, `a` is a list containing `n` integers input by the user.
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
        
    #State of the program after the  for loop has been executed: `n` is an even integer in the range [2, 100], `d` is a dictionary mapping each integer from `a` to its count of occurrences, and `a` is a list of `n` integers input by the user.
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
        
    #State of the program after the  for loop has been executed: `n` is an even integer in the range [2, 100]; `c` is 0 or 1; `a1` is -1 or a key in `d` satisfying `d[i] == n // 2`; `a2` is -1 or a key in `d` satisfying `d[i] == n // 2`.
    if (a1 != -1 and a2 != -1) :
        print('YES')
        print(a1, a2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *n is an even integer in the range [2, 100]; c is 0 or 1. If both a1 and a2 are valid keys in d, then a1 and a2 are printed. Otherwise, at least one of a1 or a2 is -1, and "NO" is printed.
#Overall this is what the function does:The function reads an even integer `n` from user input, which specifies the number of subsequent integers to read. It then takes `n` integers as input and counts the occurrences of each integer. The function checks if there are exactly two distinct integers in the list that each appear exactly `n / 2` times. If such integers are found, it prints "YES" followed by the two integers; otherwise, it prints "NO". The function handles the case where no integers meet the criteria or where input does not conform to expected constraints, ensuring proper handling of counts and lists.

