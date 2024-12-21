#State of the program right berfore the function call: n is a non-negative integer less than or equal to 10^18, and k is a positive integer less than or equal to 10^5.
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
            
        #State of the program after the loop has been executed: `n` is 0 if the loop executed at least once, `a` contains a list of `x` values where `x` was the bit length of `n` minus 1 at each iteration, `i` is equal to or greater than the bit length of the original `n` minus 1, and `k` remains the input integer.
        if (len(a) < k) :
            print('No')
        else :
            a = a[:k]
            a.sort(reverse=True)
            print('Yes')
            print(' '.join(map(str, a)))
        #State of the program after the if-else block has been executed: *`n` is 0 if the loop executed at least once, `a` contains a list of `x` values where `x` was the bit length of `n` minus 1 at each iteration, `i` is equal to or greater than the bit length of the original `n` minus 1, and `k` remains the input integer. If the length of `a` is less than `k`, 'No' has been printed. Otherwise, `a` is a sorted list in descending order of `k` values, 'Yes' has been printed, and the elements of `a` have been printed.
    #State of the program after the if-else block has been executed: `n` is an input integer, `k` is an input integer. If `n` is less than `k`, the string 'No' has been printed. Otherwise, `n` is 0 if the loop executed at least once, `a` contains a list of `x` values where `x` was the bit length of `n` minus 1 at each iteration, `i` is equal to or greater than the bit length of the original `n` minus 1, and `k` remains the input integer. If the length of `a` is less than `k`, 'No' has been printed. Otherwise, `a` is a sorted list in descending order of `k` values, 'Yes' has been printed, and the elements of `a` have been printed.
#Overall this is what the function does:The function accepts two input integers, `n` and `k`, where `n` is a non-negative integer less than or equal to 10^18 and `k` is a positive integer less than or equal to 10^5. It determines whether `n` can be represented as the sum of `k` distinct powers of 2. If `n` is less than `k` or if `n` cannot be represented as the sum of `k` distinct powers of 2, the function prints 'No'. Otherwise, it prints 'Yes' and the `k` largest powers of 2 that sum up to `n` in descending order. The function modifies the input variables `n` and `k` are not modified outside of the function, but the variables `a` and `i` are used internally to store the powers of 2 and the iteration count, respectively. After the function concludes, `n` is either unchanged or reduced to 0 if the loop executed at least once, `a` contains a sorted list of `k` powers of 2 that sum up to `n`, and `k` remains unchanged. The function does not return any value but prints the result to the console.

