#State of the program right berfore the function call: The function takes no arguments, but the input is provided through two variables n and k, where n is a non-negative integer (1 ≤ n ≤ 10^18) and k is a positive integer (1 ≤ k ≤ 10^5), representing the required sum and the length of the sequence, respectively.
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
            
        #State of the program after the loop has been executed: `n` is either 0 or a positive value less than the last `2
        if (len(a) < k) :
            print('No')
        else :
            a = a[:k]
            a.sort(reverse=True)
            print('Yes')
            print(' '.join(map(str, a)))
        #State of the program after the if-else block has been executed: *`n` is either 0 or a positive value less than 2, `a` is a list, `k` is a value. If the length of `a` is less than `k`, 'No' has been printed. If the length of `a` is equal to `k`, `a` is sorted in descending order, 'Yes' has been printed, and the contents of `a` have been printed.
    #State of the program after the if-else block has been executed: `n` is a non-negative integer, `k` is a positive integer, if `n` is less than `k`, 'No' has been printed. If `n` is not less than `k`, then `n` is either 0 or a positive value, and `a` is a list. If the length of `a` is less than `k`, 'No' has been printed. If the length of `a` is equal to `k`, `a` is sorted in descending order, 'Yes' has been printed, and the contents of `a` have been printed.
#Overall this is what the function does:The function accepts two integers `n` and `k` through the standard input, attempts to construct a list of `k` integers representing the powers of 2 that sum up to `n`, and prints 'Yes' along with the list in descending order if successful, or 'No' otherwise. If `n` is less than `k`, it prints 'No'. The function assumes `n` is a non-negative integer and `k` is a positive integer, but does not perform any input validation.

