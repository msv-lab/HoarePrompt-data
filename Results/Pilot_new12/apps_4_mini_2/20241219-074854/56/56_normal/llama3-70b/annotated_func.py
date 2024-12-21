#State of the program right berfore the function call: n is a positive integer up to 10^18, k is a positive integer up to 100,000.
def func():
    n, k = map(int, input().split())
    if (n < k) :
        print('No')
    else :
        a = []
        i = 0
        while n > 0:
            x = n.bit_length() - 1
            
            if x <= i:
                break
            
            a.append(x)
            
            n -= 2 ** x
            
            i += 1
            
        #State of the program after the loop has been executed: `n` is 0, `i` is the number of iterations executed until `n` could no longer provide a positive value to continue, and `a` contains the list of `x` values corresponding to each iteration of the loop.
        if (len(a) < k) :
            print('No')
        else :
            a = a[:k]
            a.sort(reverse=True)
            print('Yes')
            print(' '.join(map(str, a)))
        #State of the program after the if-else block has been executed: *`n` is 0, and `i` is the number of iterations executed until `n` could no longer provide a positive value to continue. If the length of `a` is less than `k`, then `a` contains `x` values corresponding to each iteration of the loop. Otherwise, `a` contains the first `k` elements sorted in descending order, and these elements are printed as a space-separated string.
    #State of the program after the if-else block has been executed: *`n` is a positive integer up to 10^18 and `k` is a positive integer up to 100,000. If `n` is less than `k`, 'No' has been printed. Otherwise, if `n` is 0, `i` represents the number of iterations executed until `n` could no longer provide a positive value to continue. If the length of `a` is less than `k`, then `a` contains `i` values corresponding to each iteration of the loop. If the length of `a` is greater than or equal to `k`, then `a` contains the first `k` elements sorted in descending order, which are printed as a space-separated string.
#Overall this is what the function does:The function reads two integers, `n` (a positive integer up to \(10^{18}\)) and `k` (a positive integer up to 100,000). It first checks if `n` is less than `k`, printing 'No' if true. If `n` is greater than or equal to `k`, the function enters a loop that attempts to decompose `n` into powers of two, storing the indices of these powers in a list `a`. The loop continues until `n` is reduced to 0 or no further powers can be used. After the loop, if the length of `a` is less than `k`, it prints 'No'. If the length of `a` is at least `k`, it truncates `a` to the first `k` values, sorts them in descending order, and prints 'Yes' followed by the sorted elements as a space-separated string. The state of the program after execution ensures that either a rejection with 'No' is communicated, or, if accepted, the first `k` components of `n` are successfully returned in a sorted format.

