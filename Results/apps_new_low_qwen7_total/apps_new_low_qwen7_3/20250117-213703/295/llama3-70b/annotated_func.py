#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 24, and a is a list of n integers where each integer a_i satisfies 28 ≤ a_i ≤ 31.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(1 \leq n \leq 24\), `a` is a list of \(n\) integers where each integer \(a_i\) satisfies \(28 \leq a_i \leq 31\), `b` is a list \([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]\), and `f` is `True` if any of the conditions within the loop evaluate to `True`. Otherwise, `f` remains `False`. The variable `i` is `12`.
    if f :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an integer such that \(1 \leq n \leq 24\), `a` is a list of \(n\) integers where each integer \(a_i\) satisfies \(28 \leq a_i \leq 31\), `b` is a list \([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]\), `f` is `True` if any of the conditions within the loop evaluate to `True` when `f` is initially `True`, and `f` remains `False` when `f` is initially `False`, and the value of `i` is `12`. Additionally, if `f` is `True`, the print statement outputs 'YES'.
#Overall this is what the function does:The function `func` accepts a list `a` of integers, where each integer is between 28 and 31, inclusive, and has a length between 1 and 24. It checks if the elements of the list `a` match any of the following patterns based on a predefined list `b` containing the number of days in each month: either all elements are equal to 31, or the elements follow the pattern of the days in a non-leap year. If any of these conditions are met, the function prints 'YES'. Otherwise, it prints 'NO'.

