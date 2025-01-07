#State of the program right berfore the function call: n is an even integer between 2 and 100 (inclusive), and the next n lines contain integers a_i (1 ≤ a_i ≤ 100) representing the numbers written on the n cards. Each number a_i may appear multiple times.
def func():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
        
    #State of the program after the  for loop has been executed: `n` is an even integer between 2 and 100, `i` is `n - 1`, `a` contains `n` integers received as inputs.
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
        
    #State of the program after the  for loop has been executed: `n` is an even integer between 2 and 100, `a` contains `n` integers, and `d` is a dictionary where each key is a unique integer from `a` and each value is the count of occurrences of that integer in `a`.
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
        
    #State of the program after the  for loop has been executed: `n` is an even integer between 2 and 100, `a` contains `n` integers, `d` is a dictionary containing key-value pairs where the keys are the integers from `a` and the values are their counts; `c` is either 0, 1, or 2, indicating how many elements with a count equal to `n // 2` have been found, `a1` contains the first integer found with a count of `n // 2` (if any), `a2` contains the second integer found with a count of `n // 2` (if any), and if no such integers were found `a1` and `a2` remain -1.
    if (a1 != -1 and a2 != -1) :
        print('YES')
        print(a1, a2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an even integer between 2 and 100, `a` contains `n` integers, `d` is a dictionary containing key-value pairs where the keys are the integers from `a` and the values are their counts, and `c` is either 0, 1, or 2. If `a1` and `a2` are both not -1, then 'YES' has been printed along with the values of `a1` and `a2`. If either `a1` or `a2` is -1, then 'NO' has been printed, indicating that either no integers with a count of `n // 2` were found or that they do not correspond to valid integers with that count.
#Overall this is what the function does:The function reads an even integer `n` between 2 and 100, and then reads `n` integers that represent the values on `n` cards. It counts the occurrences of each integer and checks if there are exactly two distinct integers that each appear `n / 2` times. If such integers are found, it prints 'YES' followed by the two integers; otherwise, it prints 'NO'. The function does not handle cases where fewer or more than two integers have the required count, and it does not validate the input bounds for the integers beyond ensuring they are between 1 and 100.

