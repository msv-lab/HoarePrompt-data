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
        
    #State of the program after the loop has been executed: a is a list with a single element, which is the minimum value of the original list `a`. n is 1.
    if a :
        print('BitLGM' if a[0] % 2 == 0 else 'BitAryo')
    else :
        print('BitAryo')
    #State of the program after the if-else block has been executed: *`a` is a list with a single element, which is the minimum value of the original list `a`. `n` remains 1 regardless of whether the if condition is met or not.
#Overall this is what the function does:The function reads an integer \( n \) followed by \( n \) integers. It then removes all zeros from the list and subtracts the minimum non-zero value from each element in the list until only one element remains. If the list becomes empty during the process, it prints "BitAryo". Otherwise, it prints "BitLGM" if the last remaining element is even, and "BitAryo" if it is odd. The function does not return anything; the output is printed directly. Potential edge cases include when \( n = 1 \) and the single integer is zero, in which case the function should print "BitAryo".

