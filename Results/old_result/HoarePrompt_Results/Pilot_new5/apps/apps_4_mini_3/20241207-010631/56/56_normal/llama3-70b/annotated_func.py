#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^18), k is a positive integer (1 ≤ k ≤ 10^5), and the integers in the answer sequence fit the range [-10^18, 10^18].
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
            
        #State of the program after the loop has been executed: `n` is less than or equal to 0, `i` is the number of iterations executed, `a` is a list containing the last `i` values of `n.bit_length() - 1` for each successful iteration, and `k` remains a positive integer.
        if (len(a) < k) :
            print('No')
        else :
            a = a[:k]
            a.sort(reverse=True)
            print('Yes')
            print(' '.join(map(str, a)))
        #State of the program after the if-else block has been executed: *`n` is less than or equal to 0, `i` is the number of iterations executed, and `k` remains a positive integer. If the length of `a` is less than `k`, then 'No' has been printed. If the length of `a` is equal to `k`, then `a` is the sorted list of the first `k` elements from the previous list of last `i` values of `n.bit_length() - 1` in descending order.
    #State of the program after the if-else block has been executed: *`n` and `k` are positive integers. If `n` is less than `k`, then 'No' has been printed. If `n` is less than or equal to 0, `i` is the number of iterations executed, and `k` remains a positive integer. If the length of `a` is less than `k`, 'No' has been printed. If the length of `a` is equal to `k`, then `a` is the sorted list of the first `k` elements from the previous list of last `i` values of `n.bit_length() - 1` in descending order.
#Overall this is what the function does:The function accepts two positive integers, `n` and `k`, and checks if it can generate a sequence of `k` integers based on the binary representation of `n`. If `n` is less than `k`, it outputs 'No'. If not, it generates integers derived from the bit length of `n`, ensuring that the length of the generated list is at least `k`. If the generated list has fewer than `k` integers, it outputs 'No'. If it has at least `k` integers, it sorts this list in descending order and prints 'Yes' followed by the first `k` integers from this list. The integers fit within the range [-10^18, 10^18], and the constraints on `n` and `k` are 1 ≤ n ≤ 10^18 and 1 ≤ k ≤ 10^5.

