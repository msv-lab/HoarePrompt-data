#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^18, k is a positive integer such that 1 ≤ k ≤ 10^5.
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
            
        #State of the program after the loop has been executed: `n` is a non-negative integer (possibly 0) now, `k` is the original positive integer, `a` is a list containing the values of `x` collected during the iterations, `i` is the total number of iterations executed (which corresponds to how many times `x` was appended to `a`), and for each iteration, `x` was equal to the bit length of the previous value of `n` minus 1.
        if (len(a) < k) :
            print('No')
        else :
            a = a[:k]
            a.sort(reverse=True)
            print('Yes')
            print(' '.join(map(str, a)))
        #State of the program after the if-else block has been executed: *`n` is a non-negative integer (possibly 0), `k` is the original positive integer, and `a` is a list containing the values of `x` collected during the iterations. If the length of `a` is less than `k`, `a` retains its current values and `i` represents the total number of iterations executed. Otherwise, `a` contains the first `k` values sorted in descending order, `i` is the total number of iterations executed, and 'Yes' has been printed to the console as a space-separated string of the values in `a`.
    #State of the program after the if-else block has been executed: *`n` is a positive integer equal to the input value and `k` is a positive integer equal to the input value. If `n` is less than `k`, then 'No' has been printed. If `n` is greater than or equal to `k`, the list `a` retains its current values if its length is less than `k`. Otherwise, `a` contains the first `k` values sorted in descending order, and 'Yes' has been printed to the console as a space-separated string of the values in `a`.
#Overall this is what the function does:The function `func` takes two positive integers, `n` and `k`, as input. It first checks if `n` is less than `k`, printing 'No' and terminating if this is the case. If `n` is greater than or equal to `k`, it initializes an empty list `a` and performs a loop where it decrements `n` by powers of two corresponding to the highest set bit until `n` becomes 0 or no higher bits can be found. The collected values (indexes of the bits) are stored in the list `a`. After the loop, if the list `a` contains fewer than `k` elements, it outputs 'No'. If it has at least `k` elements, it truncates `a` to the first `k` elements, sorts them in descending order, and prints 'Yes' followed by the space-separated values from `a`. The final state of `n` will be non-negative (possibly 0), retaining its original input value after function execution; `k` will also remain unchanged; if 'Yes' is printed, a contains the first `k` values sorted in descending order. If 'No' is printed at any point, a will not be printed. Overall, the function checks conditions and combats the binary representation of `n` while managing a list of bit positions until a defined output is achieved based on `k`.

