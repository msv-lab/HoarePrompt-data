#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, n is an integer such that 3 ≤ n ≤ 10^5. Additionally, the sum of all n values across all test cases does not exceed 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        mid = n // 2
        
        a = []
        
        for i in range(1, n // 2 + 1):
            a.append(i)
            a.append(mid + i)
        
        if n % 2 != 0:
            a.append(n)
        
        for i in range(n):
            print(a[i], end=' ')
        
        print('\n', end='')
        
    #State of the program after the  for loop has been executed: `t` is a non-negative integer, `n` is a non-negative integer, `mid` is `n // 2`, `a` is a list containing `[1, mid+1, 2, mid+2, ..., n//2, mid+n//2]` if `n` is even, otherwise `a` is a list containing `[1, mid+1, 2, mid+2, ..., (n-1)//2, mid+(n-1)//2, n]`, and all elements in `a` are printed in sequence without newlines, the output includes `t` sets of such lists separated by newlines.
#Overall this is what the function does:The function accepts an integer `t`, representing the number of test cases. For each test case, it processes an integer `n`, ensuring that `3 ≤ n ≤ 10^5`. It then generates a list `a` containing integers from 1 to `n` such that the list is symmetric around the middle value of `n`. If `n` is even, the list contains pairs of numbers symmetrically placed around the middle; if `n` is odd, the middle number `n` is included in the list. After constructing the list, the function prints each element of the list in sequence without newlines, followed by a newline after each test case. The output consists of `t` sets of such lists, each set separated by a newline.

