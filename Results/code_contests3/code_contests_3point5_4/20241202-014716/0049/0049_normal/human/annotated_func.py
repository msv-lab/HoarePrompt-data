#State of the program right berfore the function call: n is an integer such that 2 <= n <= 3*10^5, and s is a string of length n consisting only of lowercase Latin letters.**
def func():
    n = map(int, raw_input().split())
    n = n[0]
    c = raw_input()
    flag = False
    for i in range(n - 1):
        if c[i] > c[i + 1]:
            flag = True
            pos = i
        
    #State of the program after the  for loop has been executed: `n` is an ASCII value of the first character in the string `s`, `c` is the input value, `flag` is True if there exists any pair of elements in `c` such that the element at the current index is greater than the next element, `pos` is the index of the first occurrence where this condition is met. If no such pair exists, `flag` remains False.
    if flag :
        print('YES')
        print(pos + 1, pos + 2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an ASCII value of the first character in the string `s`, `c` is the input value. If there exists any pair of elements in `c` such that the element at the current index is greater than the next element, `flag` is True and `pos` is the index of the first occurrence where this condition is met. In this case, the values of `pos + 1` and `pos + 2` are printed. If no such pair exists, `flag` remains False, and the output is 'NO'.
#Overall this is what the function does:The function `func` reads an integer `n` and a string `c` as input. It then iterates through the string `c` to check if there exists any pair of elements where the current element is greater than the next element. If such a pair is found, it prints 'YES' along with the indices of the first occurrence of this condition. If no such pair exists, it prints 'NO'. The function does not accept any parameters and does not return any value.

