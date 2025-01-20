#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 24, and the list a contains n integers where each integer a_i is an integer such that 28 ≤ a_i ≤ 31.
def func():
    n = int(input())

a = list(map(int, input().split()))

b = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

f = False
    for i in range(12):
        if all(a[j] == b[(i + j) % 12] for j in range(n)):
            f = True
        
        if i == 11 and not f:
            break
        
        if all(a[j] == b[(i + j) % 12 + 12] for j in range(n)):
            f = True
        
        if i == 11 and not f:
            break
        
    #State of the program after the  for loop has been executed: - `i` is 12 (since the loop always runs up to 11 and then exits).
    #- `n` is an integer such that \(1 \leq n \leq 24\).
    #- `f` is `True` if any of the conditions in the loop were satisfied before `i` reached 11; otherwise, `f` is `False`.
    #
    #Thus, the final output state is:
    #Output State:
    if f :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: `i` is 12, `n` is an integer such that \(1 \leq n \leq 24\), and the printed output is 'YES' if `f` is `True`; otherwise, `f` remains `False`.
#Overall this is what the function does:The function takes no explicit parameters but reads an integer \( n \) and a list \( a \) of \( n \) integers, where each integer in \( a \) is between 28 and 31 inclusive. It then checks if the elements of \( a \) match any of two possible sequences of 12 integers, which represent the number of days in months (either January to December or February to January of the next year). If any of these sequences match a cyclic shift of the elements in \( a \), it prints 'YES'; otherwise, it prints 'NO'.

