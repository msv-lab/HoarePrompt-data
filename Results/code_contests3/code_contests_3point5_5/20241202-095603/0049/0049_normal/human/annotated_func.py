#State of the program right berfore the function call: # Precondition

**n is an integer such that 2 <= n <= 3*10^5. s is a string of length n consisting only of lowercase Latin letters.**
def func():
    n = map(int, raw_input().split())
    n = n[0]
    c = raw_input()
    flag = False
    for i in range(n - 1):
        if c[i] > c[i + 1]:
            flag = True
            pos = i
        
    #State of the program after the  for loop has been executed: `flag` is True if there exists at least one pair of elements in list `c` such that the element at the current index is greater than the next element, `pos` is the index of the last occurrence of this condition, `n` is greater than or equal to 2
    if flag :
        print('YES')
        print(pos + 1, pos + 2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`flag` is True if there exists at least one pair of elements in list `c` such that the element at the current index is greater than the next element, `pos` is the index of the last occurrence of this condition, and `n` is greater than or equal to 2. If `flag` is True, the function maintains the same state with the previous values of `flag`, `pos`, and `n`. If `flag` is False, the function prints 'NO' and does not change the values of `pos` and `n`.
#Overall this is what the function does:The function `func` reads an integer `n` and a string `c` from the input. It then iterates through the string and checks if there exists a pair of elements where the element at the current index is greater than the next element. If such a pair exists, it sets `flag` to True and stores the index of the last occurrence of this condition in `pos`. Finally, if `flag` is True, it prints 'YES' along with the indices of the pair; otherwise, it prints 'NO'. The function does not return any value. It works under the assumption that `n` is an integer such that 2 <= n <= 3*10^5 and `c` is a string of length `n` consisting only of lowercase Latin letters.

