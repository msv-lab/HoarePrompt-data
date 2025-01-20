#State of the program right berfore the function call: The input consists of two lines. The first line contains an integer n where 1 ≤ n ≤ 3. The second line contains n integers a_1, a_2, ..., a_{n} where 0 ≤ a_{i} < 300.
def func():
    n = int(input())

a = list(map(int, input().split()))
    while len(a) > 1:
        if min(a) == 0:
            a.remove(0)
        else:
            x = min(a)
            a = [(i - x) for i in a]
        
    #State of the program after the loop has been executed: `n` is 2 or 3, and `a` is a list containing exactly one integer. This integer is either 0 or the difference between the maximum and minimum elements of the original list `a`.
    if a :
        print('BitLGM' if a[0] % 2 == 0 else 'BitAryo')
    else :
        print('BitAryo')
    #State of the program after the if-else block has been executed: *`n` is 2 or 3, and `a` is a list containing exactly one integer. If the list `a` contains [0], the first element remains unchanged and the console displays 'BitAryo'. Otherwise, the first element of `a` is either 0 or the difference between the maximum and minimum elements of the original list `a`, and the console displays 'BitAryo'.
#Overall this is what the function does:The function reads an integer \( n \) and \( n \) integers \( a_1, a_2, \ldots, a_n \) as input, where \( 1 \leq n \leq 3 \) and \( 0 \leq a_i < 300 \). It then repeatedly reduces the list \( a \) by subtracting the minimum non-zero element from each element until only one element remains. This remaining element is either 0 or the difference between the maximum and minimum elements of the original list. Based on whether this final element is even or not, the function prints either 'BitLGM' or 'BitAryo'. The function handles the case where the initial list might contain zeros, which are removed before performing the subtraction operation.

