#State of the program right berfore the function call: n is an integer such that 2 <= n <= 3*10^5, s is a string of length n consisting only of lowercase Latin letters.**
def func():
    n = map(int, raw_input().split())
    n = n[0]
    c = raw_input()
    flag = False
    for i in range(n - 1):
        if c[i] > c[i + 1]:
            flag = True
            pos = i
        
    #State of the program after the  for loop has been executed: `flag` is True if there exists at least one pair of elements in list `c` such that the element at the current index is greater than the next element. If no such pair exists, `flag` remains False. `pos` is the index of the last occurrence of such a pair. `i` is an integer that increments by 1 until the loop terminates. `n` remains the same, an integer greater than or equal to 2.
    if flag :
        print('YES')
        print(pos + 1, pos + 2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`flag` is a boolean. If `flag` is True, `pos` is the index of the last occurrence of a pair where the current element is greater than the next element, `i` is an integer that increments by 1 until the loop terminates, `n` remains the same, an integer greater than or equal to 2. The values `pos + 1` and `pos + 2` are printed. If `flag` is False, `pos` is the index of the last occurrence of a pair where the current element is greater than the next one, `i` is an integer that increments by 1 until the loop terminates, `n` remains the same, an integer greater than or equal to 2.
#Overall this is what the function does:The function `func` reads an integer `n` and a string `c` from the input. It then iterates through the string to find if there exists a pair of elements where the current element is greater than the next element. If such a pair is found, it prints 'YES' along with the indices of the elements forming that pair. If no such pair is found, it prints 'NO'. The function does not explicitly return a value. It operates on predefined variables `n` and `s`, with `n` being an integer between 2 and 3*10^5, and `s` being a string of lowercase letters.

