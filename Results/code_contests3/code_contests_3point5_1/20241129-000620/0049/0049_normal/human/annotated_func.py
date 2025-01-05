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
        
    #State of the program after the  for loop has been executed: `n` is 2 or greater, `flag` is True if there exists at least one pair of elements in list `c` such that `c[i] > c[i + 1]`, `pos` is assigned the index of the last pair of elements where `c[i] > c[i + 1]` if `flag` is True. Otherwise, `flag` remains False and `pos` is not updated.
    if flag :
        print('YES')
        print(pos + 1, pos + 2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an integer greater than or equal to 2. If `flag` is True, `pos` is assigned the index of the last pair of elements where `c[i] > c[i + 1]`, `flag` remains True, and `pos + 1, pos + 2` are printed. If `flag` is False, `pos` remains unchanged and the code prints 'NO' to the console.
#Overall this is what the function does:The function reads input from the user, processes it to find if there exists a pair of elements in the list `c` where the element at index `i` is greater than the element at index `i+1`. If such a pair exists, it prints 'YES' followed by the indices of the last pair found. If no such pair exists, it prints 'NO'. The function does not accept any parameters.

