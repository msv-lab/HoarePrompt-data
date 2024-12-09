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
            
        #State of the program after the loop has been executed: `n` is 0, `i` is equal to the number of loop iterations, `a` contains the recorded highest powers of 2 used in each iteration.
        if (len(a) < k) :
            print('No')
        else :
            a = a[:k]
            a.sort(reverse=True)
            print('Yes')
            print(' '.join(map(str, a)))
        #State of the program after the if-else block has been executed: *`n` is 0 and `i` is equal to the number of loop iterations. If the length of `a` is less than `k`, then `a` contains the recorded highest powers of 2 used in each iteration. Otherwise, `a` contains k sorted highest powers of 2 in descending order, and 'Yes' has been printed.
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 10^18 and `k` is a positive integer such that 1 ≤ `k` ≤ 10^5. If `n` is less than `k`, then 'No' has been printed. Otherwise, if `n` is 0, `i` equals the number of loop iterations; if the length of `a` is less than `k`, then `a` contains the recorded highest powers of 2 used in each iteration. If the length of `a` is equal to or greater than `k`, then `a` contains `k` sorted highest powers of 2 in descending order and 'Yes' has been printed.
#Overall this is what the function does:The function accepts two positive integers, `n` (1 ≤ n ≤ 10^18) and `k` (1 ≤ k ≤ 10^5), and checks if it is possible to express `n` as a sum of exactly `k` distinct powers of 2. If `n` is less than `k`, it outputs 'No'. If enough distinct powers can be formed, it prints 'Yes' and the `k` largest powers of 2 used, sorted in descending order. If not enough distinct powers can be formed, it prints 'No'. The function does not return any values, but directly prints the results.

