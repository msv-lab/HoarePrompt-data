#State of the program right berfore the function call: **
def func():
    n = map(int, raw_input().split())
    n = n[0]
    c = raw_input()
    flag = False
    for i in range(n - 1):
        if c[i] > c[i + 1]:
            flag = True
            pos = i
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to 2, `c` is a string input, `flag` is True if there exists at least one pair of elements in `c` such that the element at the previous index is greater than the element at the current index, `pos` is the index of the last occurrence where this condition is met, otherwise `flag` is False
    if flag :
        print('YES')
        print(pos + 1, pos + 2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is greater than or equal to 2, `c` is a string input. If `flag` is True, then the function prints 'YES' and outputs the values of `pos + 1` and `pos + 2`. If `flag` is False, then the function does not print anything and `pos` is either the index of the last occurrence where the condition is met or None.
#Overall this is what the function does:The function reads an integer `n` and a string `c` as inputs. It then iterates through the elements of `c` to check if there exists a pair of elements where the previous element is greater than the current element. If such a pair is found, it prints 'YES' along with the indices of those elements. If no such pair is found, it prints 'NO'. The function does not accept any parameters and always outputs either 'YES' with indices or 'NO' based on the conditions met in the loop.

