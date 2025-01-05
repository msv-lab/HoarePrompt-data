#State of the program right berfore the function call: **Precondition**: **n is an integer such that 2 <= n <= 3*10^5. s is a string of length n consisting only of lowercase Latin letters.**
def func():
    n = map(int, raw_input().split())
    n = n[0]
    c = raw_input()
    flag = False
    for i in range(n - 1):
        if c[i] > c[i + 1]:
            flag = True
            pos = i
        
    #State of the program after the  for loop has been executed: `c` is assigned the user input as a string, `flag` is True if there exists at least one pair of adjacent characters in `c` such that the character at index `i` is greater than the character at index `i+1`, `n` is greater than or equal to 2, `i` is the index of the last iteration, and `pos` is assigned the index of the last occurrence where the condition `c[i] > c[i + 1]` is true. If no such pair exists, `flag` remains False and `pos` is not updated.
    if flag :
        print('YES')
        print(pos + 1, pos + 2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`c` is a string containing user input, `flag` is True if there exists at least one pair of adjacent characters in `c` such that the character at index `i` is greater than the character at index `i+1`, `n` is greater than or equal to 2, `i` is the index of the last iteration, and `pos` is assigned the index of the last occurrence where the condition `c[i] > c[i + 1]` is true. If no such pair exists, `flag` remains False and `pos` is not updated. If `flag` is True, 'YES' is printed along with `pos + 1` and `pos + 2`. If `flag` is False, no additional action is taken, and `pos` remains unchanged.
#Overall this is what the function does:The function `func` reads an integer `n` and a string `c` as user input. It then iterates over the characters of the string to check if there exists at least one pair of adjacent characters where the first character is greater than the second. If such a pair is found, it sets `flag` to True and stores the index of the last occurrence in `pos`. Finally, it prints 'YES' along with the indices of the identified pair if `flag` is True, otherwise, it prints 'NO'. The function does not accept any parameters and operates within the constraints specified.

