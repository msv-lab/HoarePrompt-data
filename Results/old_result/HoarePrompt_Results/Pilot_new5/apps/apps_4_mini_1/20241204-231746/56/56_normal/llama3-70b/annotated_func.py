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
            
        #State of the program after the loop has been executed: `n` is 0 or less, `i` is equal to the number of times the loop executed; `a` contains all the values of `x` collected during each iteration, where each `x` is equal to `n.bit_length() - 1` at that time. The original value of `n` must have been sufficient to allow the loop to execute until `i` reached its final value.
        if (len(a) < k) :
            print('No')
        else :
            a = a[:k]
            a.sort(reverse=True)
            print('Yes')
            print(' '.join(map(str, a)))
        #State of the program after the if-else block has been executed: *`n` is 0 or less, `i` is equal to the number of times the loop executed, and `a` contains all the values of `x` collected during each iteration, where each `x` is equal to `n.bit_length() - 1` at that time. If the length of `a` is less than `k`, then 'No' is printed. Otherwise, 'Yes' is printed, `a` is sorted in reverse order, and the length of `a` is equal to `k`, with the output of ' '.join(map(str, a)) being the space-separated string of elements in `a`.
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 10^18 and `k` is a positive integer such that 1 ≤ `k` ≤ 10^5. If `n` is less than `k`, the output is 'No'. Otherwise, if `n` is greater than or equal to `k`, `i` is equal to the number of times the loop executed, `a` contains all the values of `x` collected during each iteration (where each `x` is equal to `n.bit_length() - 1` at that time), and if the length of `a` is less than `k`, 'No' is printed. If the length of `a` is equal to or greater than `k`, 'Yes' is printed, `a` is sorted in reverse order, and the output is a space-separated string of the elements in `a`.
#Overall this is what the function does:The function reads two positive integers `n` and `k` from input. It first checks if `n` is less than `k`, printing 'No' if so. If `n` is greater than or equal to `k`, it collects values of `x` (where `x` is determined by the bit length of `n`) until `n` becomes zero or the loop conditions are no longer met. If the number of collected values is less than `k`, it prints 'No'. If there are at least `k` values, it sorts them in descending order, prints 'Yes', and outputs the first `k` values as a space-separated string. The function does not return any values; it only produces print outputs.

