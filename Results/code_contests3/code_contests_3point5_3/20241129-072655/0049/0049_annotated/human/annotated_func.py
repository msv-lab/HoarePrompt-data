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
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to 2, `c` is assigned the value of `n`, `flag` is True if there exists at least one pair of elements in `c` such that the element at index `i` is greater than the element at index `i + 1`, `pos` is assigned the index of the last occurrence where `c[i] > c[i + 1]` if `flag` is True, otherwise `pos` is not assigned a value.
    if flag :
        print('YES')
        print(pos + 1, pos + 2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is greater than or equal to 2, `c` is assigned the value of `n`. If `flag` is True, `pos` is assigned the index of the last occurrence where `c[i] > c[i + 1]`, and `print(pos + 1, pos + 2)` has been executed. If `flag` is False, `pos` is not assigned a value, and the program prints 'NO'.
#Overall this is what the function does:The function `func()` reads an integer `n` and a string `c` from the user input. It then iterates through the elements of `c` and checks if there exists a pair of elements where the element at index `i` is greater than the element at index `i + 1`. If such a pair is found, it sets `flag` to True and stores the index of the last occurrence where this condition is met in `pos`. After the loop, if `flag` is True, it prints 'YES' along with the indices `pos + 1` and `pos + 2`. If `flag` is False, it prints 'NO'. The function does not have any specified parameters and does not return any value. There might be an issue with the loop logic as it only considers elements up to `n - 2`.

