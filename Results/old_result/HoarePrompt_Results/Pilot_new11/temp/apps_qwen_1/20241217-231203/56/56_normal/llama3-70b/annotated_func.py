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
            
        #State of the program after the loop has been executed: `n` is 0, `a` is a list containing the bit lengths of the powers of 2 subtracted from the original `n` during each iteration, `i` is the number of iterations (which is the number of bits in the binary representation of the original `n` minus 1), `x` is the last bit length appended to `a`.
        if (len(a) < k) :
            print('No')
        else :
            a = a[:k]
            a.sort(reverse=True)
            print('Yes')
            print(' '.join(map(str, a)))
        #State of the program after the if-else block has been executed: *`n` is 0, `a` is a list containing the bit lengths of the powers of 2 subtracted from the original `n` during each iteration, `i` is the number of iterations (which is the number of bits in the binary representation of the original `n` minus 1), `x` is the last bit length appended to `a`. If the length of `a` is less than `k`, the function continues with the current `a`. Otherwise, `a` is truncated to the first `k` elements and `i` is set to -1.
    #State of the program after the if-else block has been executed: *`n` is an integer between 1 and \(10^{18}\), `k` is an integer between 1 and \(10^{5}\). If `n` is less than `k`, then 'No' is printed to the console. Otherwise, `n` is 0, `a` is a list containing the bit lengths of the powers of 2 subtracted from the original `n` during each iteration, `i` is the number of iterations (which is the number of bits in the binary representation of the original `n` minus 1), and `x` is the last bit length appended to `a`. If the length of `a` is less than `k`, the function continues with the current `a`. Otherwise, `a` is truncated to the first `k` elements and `i` is set to -1.
#Overall this is what the function does:The function accepts two integers \(n\) and \(k\), where \(1 \leq n \leq 10^{18}\) and \(1 \leq k \leq 10^{5}\). It determines whether it is possible to construct a sequence of exactly \(k\) distinct integers, each being a power of 2, whose sum equals \(n\). If such a sequence exists, the function prints 'Yes' followed by the sequence of integers. If not, it prints 'No'. Specifically:

1. The function first checks if \(n\) is less than \(k\). If true, it prints 'No' immediately.
2. Otherwise, it constructs a list `a` containing the bit lengths of the powers of 2 subtracted from \(n\) until \(n\) becomes 0.
3. If the length of `a` is less than \(k\), it prints 'No'.
4. If the length of `a` is at least \(k\), it truncates `a` to its first \(k\) elements and sorts these elements in descending order before printing 'Yes' followed by the sorted list of integers.

