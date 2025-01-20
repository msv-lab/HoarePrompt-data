#State of the program right berfore the function call: n is an integer where 1 ≤ n ≤ 3, and a is a list of n integers where 0 ≤ a_i < 300.
def func():
    n = int(input())

a = list(map(int, input().split()))
    while len(a) > 1:
        if min(a) == 0:
            a.remove(0)
        else:
            x = min(a)
            a = [(i - x) for i in a]
        
    #State of the program after the loop has been executed: `n` is an integer where 1 ≤ n ≤ 3, `a` is a list of 1 integer where 0 ≤ a_i < 300. The final list `a` contains the GCD of the original elements if they were not all zeros, or it contains `[0]` if the original list was all zeros.
    if a :
        print('BitLGM' if a[0] % 2 == 0 else 'BitAryo')
    else :
        print('BitAryo')
    #State of the program after the if-else block has been executed: *`n` is an integer where 1 ≤ n ≤ 3, `a` is a list of 1 integer where 0 ≤ a_i < 300. If `a` is not empty and `a[0]` is not zero, the output is 'BitLGM' if `a[0]` is even, or 'BitAryo' if `a[0]` is odd. If `a` is empty or all elements are zero, the final list `a` contains `[0]`.
#Overall this is what the function does:The function reads an integer `n` (where 1 ≤ n ≤ 3) and a list `a` of `n` integers (where 0 ≤ a_i < 300). It then processes the list `a` to reduce it to a single element. This element is the greatest common divisor (GCD) of the original non-zero elements of the list, or 0 if all elements were zero. After processing, the function prints 'BitLGM' if the final element is even, or 'BitAryo' if the final element is odd. If the list becomes empty during processing, the function prints 'BitAryo'. The final state of the program is that `n` remains unchanged, and `a` is a list containing a single integer (either the GCD of the original non-zero elements or 0), and the output is either 'BitLGM' or 'BitAryo' based on the parity of this final element.

