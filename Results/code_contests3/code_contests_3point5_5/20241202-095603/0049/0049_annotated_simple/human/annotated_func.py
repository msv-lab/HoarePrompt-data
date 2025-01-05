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
        
    #State of the program after the  for loop has been executed: `n` is the first element of the original list, `i` is `n-1`, `flag` is True if there exists at least one pair of elements such that `c[i] > c[i+1]`, `pos` is the index of the last pair of elements where `c[i] > c[i+1]`
    if flag :
        print('YES')
        print(pos + 1, pos + 2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n`, `i`, `flag`, `pos` are integers. If `flag` is True, then it prints 'YES'. If `flag` is False, then it prints 'NO'.
#Overall this is what the function does:The function `func` reads input, processes it, and determines if there exists a pair of elements in the input list such that the element at the current index is greater than the next element. If such a pair exists, it prints 'YES' along with the indices of the elements. Otherwise, it prints 'NO'. The function does not accept any parameters and does not return any value.

