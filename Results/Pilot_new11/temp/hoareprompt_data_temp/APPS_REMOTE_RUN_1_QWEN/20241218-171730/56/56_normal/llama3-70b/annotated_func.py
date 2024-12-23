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
            
        #State of the program after the loop has been executed: `n` is 0, `a` is a list containing the sequence of integers where each integer is the highest power of 2 subtracted from `n` until `n` becomes 0; `i` is the number of iterations performed, which is the length of the list `a`; `k` is an integer obtained from input() and remains unchanged; `x` is the last value of `x` calculated during the final iteration, which is `bit_length(n) - 1` when `n` was just above 0.
        if (len(a) < k) :
            print('No')
        else :
            a = a[:k]
            a.sort(reverse=True)
            print('Yes')
            print(' '.join(map(str, a)))
        #State of the program after the if-else block has been executed: *`n` is 0, `a` is either a list containing the sequence of integers where each integer is the highest power of 2 subtracted from `n` until `n` becomes 0, with the length of `a` being less than `k`, or a sorted list in descending order. `i` is the length of the original list `a`, `k` is an integer obtained from input() and remains unchanged, `x` is either the last value of `x` calculated during the final iteration (which is `bit_length(n) - 1` when `n` was just above 0) or `i - 1`, and the function prints 'Yes' if the length of `a` is not less than `k`.
    #State of the program after the if-else block has been executed: *`n` is an integer obtained from input(), `k` is an integer obtained from input(), and 1 ≤ `n` ≤ 10^18, 1 ≤ `k` ≤ 10^5. If `n` is less than `k`, 'No' is printed. Otherwise, `n` is represented as a list `a` of integers where each integer is the highest power of 2 subtracted from `n` until `n` becomes 0, with the length of `a` being less than `k`. The list `a` is sorted in descending order, `i` is the length of the original list `a`, `k` remains unchanged, and 'Yes' is printed if the length of `a` is not less than `k`.
#Overall this is what the function does:The function processes two inputs, `n` and `k`, where `n` is a positive integer (1 ≤ n ≤ 10^18) and `k` is a positive integer (1 ≤ k ≤ 10^5). It first checks if `n` is less than `k`. If true, it prints 'No'. Otherwise, it iterates to find the highest powers of 2 that can be subtracted from `n` until `n` becomes 0, storing these values in a list `a`. After the iteration, it checks if the length of `a` is less than `k`. If true, it prints 'No'. Otherwise, it sorts the list `a` in descending order and prints 'Yes' followed by the elements of `a` in the sorted order. The function does not accept any parameters and does not return anything. An edge case is when `n` is exactly equal to `2

