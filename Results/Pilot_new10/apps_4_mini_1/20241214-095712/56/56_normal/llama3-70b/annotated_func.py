#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^18, and k is a positive integer such that 1 ≤ k ≤ 10^5.
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
            
        #State of the program after the loop has been executed: `n` is non-negative, `i` is the total number of iterations executed, `a` contains values corresponding to the highest set bits encountered during each iteration, and `k` remains an integer such that 1 ≤ `k` ≤ 10^5.
        if (len(a) < k) :
            print('No')
        else :
            a = a[:k]
            a.sort(reverse=True)
            print('Yes')
            print(' '.join(map(str, a)))
        #State of the program after the if-else block has been executed: *`n` is non-negative, `i` is the total number of iterations executed, and `k` is an integer such that 1 ≤ `k` ≤ 10^5. If the length of `a` is less than `k`, then values corresponding to the highest set bits encountered during each iteration are added to `a`. If the length of `a` is equal to `k`, then `a` remains sorted in descending order and is printed as space-separated values.
    #State of the program after the if-else block has been executed: *`n` is an input integer such that 1 ≤ `n` ≤ 10^18 and `k` is an input integer such that 1 ≤ `k` ≤ 10^5. If `n` is less than `k`, the output is 'No'. If `n` is greater than or equal to `k`, `n` is non-negative and `i` is the total number of iterations executed. If the length of `a` is less than `k`, values corresponding to the highest set bits encountered during each iteration are added to `a`. If the length of `a` is equal to `k`, then `a` remains sorted in descending order and is printed as space-separated values.
#Overall this is what the function does:The function accepts two positive integers `n` (where \(1 \leq n \leq 10^{18}\)) and `k` (where \(1 \leq k \leq 10^{5}\)). It checks if `n` is smaller than `k` and in that case, it prints 'No'. If `n` is greater than or equal to `k`, it attempts to find the highest set bits from `n` and adds them to a list `a`. If the length of `a` is less than `k`, it prints 'No'. If the length of `a` is greater than or equal to `k`, it sorts `a` in descending order, prints 'Yes', followed by the first `k` elements of `a` as space-separated values.

