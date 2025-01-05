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
        
    #State of the program after the  for loop has been executed: `flag` is a boolean, `n` is greater than or equal to 2, `i` is equal to n-2, and `pos` is either the index of the last occurrence where `c[i]` is greater than `c[i + 1]` or 0 if no such occurrence exists.
    if flag :
        print('YES')
        print(pos + 1, pos + 2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`flag` is a boolean, `n` is greater than or equal to 2, `i` is equal to n-2, `pos` is either the index of the last occurrence where `c[i]` is greater than `c[i + 1]` or 0 if no such occurrence exists. If `flag` is true, 'YES' is printed on the console along with pos + 1 and pos + 2. If `flag` is false, 'NO' is printed on the console.
#Overall this is what the function does:The function `func` reads input from the user, processes it to find if there is a decreasing sequence in a given string, and prints 'YES' followed by the positions if such a sequence exists, otherwise it prints 'NO'. The function does not accept any parameters and does not return anything. However, the current implementation only checks for a decreasing sequence and does not handle cases where the sequence is non-decreasing or where multiple decreasing sequences exist.

