#State of the program right berfore the function call: n is a non-negative integer less than or equal to 10^18 and k is a non-negative integer less than or equal to 10^5.
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
            
        #State of the program after the loop has been executed: `n` is the remaining value after subtracting the largest powers of 2 that can be represented by the bits in the original value of `n`, `i` is the number of times the most significant bit in `n` can be removed until `x` is less than or equal to `i`, `a` contains the positions of the most significant bits in `n` at each iteration, until the loop breaks.
        if (len(a) < k) :
            print('No')
        else :
            a = a[:k]
            a.sort(reverse=True)
            print('Yes')
            print(' '.join(map(str, a)))
        #State of the program after the if-else block has been executed: `n` is the remaining value after subtracting the largest powers of 2 that can be represented by the bits in the original value of `n`, `i` is the number of times the most significant bit in `n` can be removed until `n` is less than or equal to `i`, `a` contains the positions of the most significant bits in `n` at each iteration, if the length of `a` is less than `k`, the string 'No' has been printed, otherwise, 'Yes' has been printed along with the content of `a` which contains the first `k` positions of the most significant bits in `n` in descending order.
    #State of the program after the if-else block has been executed: `n` and `k` are input integers. If `n` is less than `k`, 'No' has been printed. Otherwise, `n` is the remaining value after subtracting the largest powers of 2 that can be represented by the bits in the original value of `n`, and `i` is the number of times the most significant bit in `n` can be removed until `n` is less than or equal to `i`. Additionally, `a` contains the positions of the most significant bits in `n` at each iteration. If the length of `a` is less than `k`, 'No' has been printed. Otherwise, 'Yes' has been printed along with the content of `a`, which contains the first `k` positions of the most significant bits in `n` in descending order.
#Overall this is what the function does:This function takes two non-negative integers `n` and `k` as input, where `n` is less than or equal to 10^18 and `k` is less than or equal to 10^5. It checks if `n` is less than `k` and prints 'No' if true. Otherwise, it calculates the positions of the most significant bits in `n` by iteratively subtracting the largest power of 2 that can be represented by the bits in `n`. The function stores these positions in a list `a`. If the length of `a` is less than `k`, it prints 'No'. Otherwise, it sorts the first `k` elements of `a` in descending order and prints 'Yes' along with the sorted positions. The function does not return any value; instead, it prints the results directly to the console. After execution, the state of the program will be one of two possible outcomes: either 'No' will have been printed if `n` is less than `k` or if the number of most significant bits in `n` is less than `k`, or 'Yes' will have been printed along with the first `k` positions of the most significant bits in `n` in descending order if the conditions are met.

