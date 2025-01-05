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
        
    #State of the program after the  for loop has been executed: `n` is an integer greater than or equal to 2, `c` is the input list of integers, `flag` is True if there exists at least one pair of elements in the list where the previous element is greater than the next element, `pos` contains the index of the first such occurrence if `flag` is True.
    if flag :
        print('YES')
        print(pos + 1, pos + 2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an integer greater than or equal to 2, `c` is the input list of integers. If `flag` is True, then there exists at least one pair of elements in the list where the previous element is greater than the next element, and `pos` contains the index of the first such occurrence. The program prints `pos + 1, pos + 2`. If `flag` is False, there is no pair of elements in the list where the previous element is greater than the next element. The program prints 'NO' and does not affect the state of the variables.
#Overall this is what the function does:The function `func` reads an integer `n` and a list of integers `c`. It then iterates through the list `c` and checks if there exists a pair of elements where the previous element is greater than the next element. If such a pair is found, it prints 'YES' along with the indices of the first occurrence. If no such pair exists, it prints 'NO'. The function does not explicitly return a value, but it outputs the results based on the conditions met during execution.

