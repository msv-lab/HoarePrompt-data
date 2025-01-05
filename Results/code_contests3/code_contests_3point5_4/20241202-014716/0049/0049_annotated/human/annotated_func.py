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
        
    #State of the program after the  for loop has been executed: `flag` is True if there exists at least one pair of adjacent elements in the list `c` such that the element at the current index is greater than the element at the next index. If no such pair exists, `flag` remains False. `i` is the index of the last element in the list `c`, `n` is equal to the length of the list `c`, `c` is a list of integers, and `pos` is the index of the last pair of adjacent elements where the element at the current index is greater than the element at the next index.
    if flag :
        print('YES')
        print(pos + 1, pos + 2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`flag` is a boolean, `i`, `n`, `pos` are integers, `c` is a list of integers. If `flag` is True, it means there exists at least one pair of adjacent elements in the list `c` such that the element at the current index is greater than the element at the next index. In this case, the program maintains the same state as described in the precondition. If `flag` is False, the program prints 'NO' and the state of the program changes to reflect this output, but the values of `i`, `n`, `c`, and `pos` remain the same.
#Overall this is what the function does:The function `func` reads input from the user, processes the input list `c` to check if there exists at least one pair of adjacent elements where the current element is greater than the next element. If such a pair exists, it prints 'YES' followed by the index positions of that pair. If no such pair exists, it prints 'NO'. The function does not accept any parameters and does not return any value.

